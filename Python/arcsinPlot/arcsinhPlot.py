import numpy as np 

def setArcsinh(method, *args, dim=1, **kwargs):
	if not hasattr(dim,"__itr__"):
		dim = range(dim)
	args = list(args)
	for ii in dim:
		args[ii] = np.arcsinh(args[ii])
	return method(*args,**kwargs)