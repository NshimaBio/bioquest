import functools
import numpy as np
from ._stringpy import count,grep,detect,replace,sub

# string
subs = np.vectorize(sub,otypes=[str])
replaces = np.vectorize(replace,otypes=[str])
detects = np.vectorize(detect,otypes=[bool])
remove = functools.partial(replace,repl='')
removes = np.vectorize(remove,otypes=[str])
counts = np.vectorize(count,otypes=[int])
greps = np.vectorize(grep,otypes=[str])