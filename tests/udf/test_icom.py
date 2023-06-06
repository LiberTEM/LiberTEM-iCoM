import numpy as np

from libertem.api import Context
from libertem.udf.com import COMParams

from libertem_icom.udf.icom import ICOMUDF


def test_icom_smoke():
    ctx = Context.make_with('inline')
    ds = ctx.load('memory', data=np.random.random((3, 4, 5, 6)))

    params = COMParams(
        cy=1,
        cx=2,
        r=3,
    )
    udf = ICOMUDF(params)

    ctx.run_udf(dataset=ds, udf=udf)
