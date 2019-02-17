###############################################
# FactoSum.py
# Author: Akito D. Kawamura (aDAVISk)
# Published under BSD 3-clause license
# Last Update: 2019/02/17
###############################################

import numpy as np

def testWrap(method, *args, **kwargs):
	return method(*args, **kwargs)

def multiply(x, y):
	return x * y

testWrap(print,"Hello")

print(testWrap(multiply,3,4))

a = testWrap(np.zeros, (2,2), dtype=int)

print(a)
