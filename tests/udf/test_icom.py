import numpy as np

from libertem.api import Context
from libertem.udf.com import CoMParams

from libertem_icom.udf.icom import ICoMUDF


def test_icom_smoke():
    ctx = Context.make_with('inline')
    ds = ctx.load('memory', data=np.random.random((3, 4, 5, 6)))

    params = CoMParams(
        cy=1,
        cx=2,
        r=3,
    )
    udf = ICoMUDF(params)

    ctx.run_udf(dataset=ds, udf=udf)
