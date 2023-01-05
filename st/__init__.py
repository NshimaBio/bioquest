import functools
import numpy as np
from . import _stringpy
# string
sub = np.vectorize(_stringpy._sub,otypes=[str])
replace = np.vectorize(_stringpy._replace,otypes=[str])
detect = np.vectorize(_stringpy._detect,otypes=[bool])
remove = functools.partial(replace,repl='')
