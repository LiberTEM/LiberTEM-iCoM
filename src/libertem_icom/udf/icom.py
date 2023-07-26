import numpy as np
from libertem.udf.com import CoMUDF


def iDPC(y_centers, x_centers, xp):
    realy = x_centers.shape[0]
    realx = x_centers.shape[1]

    ky = xp.linspace(-0.5, 0.5, realy, endpoint=False).reshape((-1, 1))
    kx = xp.linspace(-0.5, 0.5, realx, endpoint=False).reshape((1, -1))

    # We shift the arrays instead of the FFT results since they are smaller
    # and it is convenient to have the zero frequency at (0, 0)
    s_kx = xp.fft.ifftshift(kx)
    s_ky = xp.fft.ifftshift(ky)

    half_x = int(xp.ceil((realx + 1) / 2))

    # Instead of converting the complex result to a Hermitian,
    # we just take the FFT for real values that doesn't even calculate
    # those values

    fft_DPC_Y = xp.fft.rfft2(y_centers)
    fft_DPC_X = xp.fft.rfft2(x_centers)

    divider = (s_kx[:, :half_x]**2 + s_ky**2)
    # Avoid div0
    divider[0, 0] = 1

    fft_iDPC = s_kx[:, :half_x] * fft_DPC_X + s_ky * fft_DPC_Y
    fft_iDPC = fft_iDPC / 2 / xp.pi / 1j / divider
    # We can't calculate the absolute phase anyway
    fft_iDPC[0, 0] = 0

    return xp.fft.irfft2(fft_iDPC)


class ICoMUDF(CoMUDF):
    def get_result_buffers(self):
        result = super().get_result_buffers()
        dtype = np.result_type(self.meta.input_dtype, np.float32)
        result['potential'] = self.buffer(
            kind='nav', dtype=dtype, use='result_only'
        )
        return result

    def get_field_results(self, field_y, field_x):
        result = super().get_field_results(field_y, field_x)
        result['potential'] = iDPC(y_centers=field_y, x_centers=field_x, xp=self.xp)
        return result
