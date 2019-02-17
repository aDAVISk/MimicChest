##########################################################
# arcsinhPlot.py
# Author: Akito D. Kawamura
# Convert a method capable to plot in arcsinh-scale.  
#
# This program is published under BSD 3-Clause License.
# This program is a beta version.
# Please use this program under your responsibility.
##########################################################

import numpy as np 

def setArcsinh(method, *args, dim=1, **kwargs):
	if not hasattr(dim,"__itr__"):
		dim = range(dim)
	args = list(args)
	for ii in dim:
		args[ii] = np.arcsinh(args[ii])
	return method(*args,**kwargs)
