###############################################
# FactoSum.py
# Author: Akito D. Kawamura (aDAVISk)
# Published under BSD 3-clause license
# Last Update: 2019/02/17
###############################################

import numpy as np

def testCast(method, *args, **kwargs):
	return method(*args, **kwargs)

def multiply(x, y):
	return x * y

testCast(print,"Hello")

print(testCast(multiply,3,4))

a = testCast(np.zeros, (2,2), dtype=int)

print(a)
