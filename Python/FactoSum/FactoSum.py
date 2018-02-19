###############################################
# FactoSum.py
# Author: Akito D. Kawamura (aDAVISk)
# Published under BSD 3-clause license
# Last Update: 2018/02/19
###############################################


import numpy as np
import scipy.misc
maxVal = np.int64(100000) #np.int64(2147483647) #2**31-1


ii=np.int64(1)
print("Start Test\n\n")
while ii <= maxVal:
	print("\r{0}".format(ii),end="")
	jj = np.int64(ii / 10)
	kk = ii % 10
	FactoSum = 0
	while jj > 0:
		FactoSum += scipy.misc.factorial(kk, exact=True)
		kk = jj % 10
		jj = np.int64(jj/10)
	FactoSum += scipy.misc.factorial(kk, exact=True)
	if FactoSum == ii:
		print("\r{0}".format(ii))
	ii+=1
print("\rTest Ended at {0}".format(maxVal))
