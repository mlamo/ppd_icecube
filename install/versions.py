#!/usr/bin/env python
import numpy
import matplotlib
import pandas
import healpy
import jupyter
matplotlib.__version__ = matplotlib._get_version()
for module in [\
        numpy,
        healpy, 
        pandas, 
        jupyter,
        matplotlib,
        ]:
    print('{__name__:>15s}: {__version__}'.format(**vars(module)))
