# LiberTEM-iCoM
Integrated center of mass / differential phase contrast following
https://doi.org/10.1038/s41598-018-20377-2

> **_NOTE:_** The patent https://data.epo.org/gpi/EP2866245B1 and related
> patents could be relevant for application of this method.

This package provides `libertem_icom.udf.icom.ICoMUDF`, an extension of libertem.udf.com.CoMUDF
with a result buffer for phase contrast with the integrated center of mass method.

The iDPC implementation is available as a separate function in `libertem_icom.udf.icom.iDPC`.

> **_NOTE:_** The method is experimental and not fully validated to produce quantitative results yet.

Installation
------------

After being released (not yet): `pip install libertem-icom`

Before release / development version: Clone repository and `pip install -e .` in repository root folder.

Usage
-----

See Jupyter notebook `examples/center_of_mass.ipynb`!
