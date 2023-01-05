import numpy as np
import re

def _sub(string,start=0,stop=-1) -> str:
	return string[start:stop]

def _detect(pattern: str, string: str, flags=0) -> bool:
	return False if re.search(pattern=pattern,string=string,flags=flags) is None else True

def _replace(pattern: str, repl: str, string: str, count:int = 0):
	return re.sub(pattern=pattern,repl=repl,string=string, count=count)

def _grep(pattern: str, string: str, flags=0):
	bl = _detect(pattern=pattern,string=string,flags=flags)
	return list(np.array(string)[bl])