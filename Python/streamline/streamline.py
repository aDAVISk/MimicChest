##########################################################
# streamline.py
# Author: Akito D. Kawamura
# calculate positions of 2D/3D stream line to be plotted.  
#
# This program is published under BSD 3-Clause License.
# This program is a beta version.
# Please use this program under your responsibility.
##########################################################
import numpy as np

def getStreamline(*arg, seed=np.zeros(3), drct="Both", dd_rec=0.5, ignore=True):
	num = len(arg)
	if num == 4:
		return getStreamline2d(arg[0],arg[1],arg[2],arg[3],seed=seed[0:2],drct=drct, dd_rec=0.5, ignore=ignore)
	elif num == 6:
		return getStreamline3d(arg[0],arg[1],arg[2],arg[3],arg[4],arg[5],seed=seed,drct=drct, dd_rec=0.5, ignore=ignore)
	else:
		raise TypeError("Method 'get_streamline' takes 4 or 6 arguments.")
	for ii in range(num):
		print(arg[ii])
#end of getStreamline

def getStreamline3d(x,y,z,vx,vy,vz,seed=np.zeros(3), drct="Both", dd_rec=0.5, ignore=True):
	nums = (len(x),len(y),len(z))
	if nums != np.shape(vx) != np.shape(vy) != np.shape(vz):
		raise TypeError("Sizes of arguments do not agree.")
	if (not ignore) or (x[0] > seed[0] >= x[-1]) or (y[0] > seed[1] >= y[-1]) or (z[0] > seed[2] >= z[-1]):
		raise ValueError("The seed point is out of the boundary.")

	strl_x_f = [seed[0]]
	strl_y_f = [seed[1]]
	strl_z_f = [seed[2]]

	strl_x_b = [seed[0]]
	strl_y_b = [seed[1]]
	strl_z_b = [seed[2]]

	vv_norm = 1.0/max(np.max(np.abs(vx)),np.max(np.abs(vy)),np.max(np.abs(vz)))
	flim = 0.01
	tt_coeff = 0.1
	tt_lim = 0.1

	if drct == "Both" or drct == "Forward":
		curr_x = seed[0]
		curr_y = seed[1]
		curr_z = seed[2]
		while True:
			try:
				id_x_l = np.where((curr_x>=x))[0][-1]
				id_y_l = np.where((curr_y>=y))[0][-1]
				id_z_l = np.where((curr_z>=z))[0][-1]
				id_x_h = np.where((curr_x<x))[0][0]
				id_y_h = np.where((curr_y<y))[0][0]
				id_z_h = np.where((curr_z<z))[0][0]
			except IndexError:	# Out of the boundary
				break

			dx = x[id_x_h]-x[id_x_l]
			dy = y[id_y_h]-y[id_y_l]
			dz = z[id_z_h]-z[id_z_l]
			dd = max(abs(strl_x_f[-1]-curr_x)/dx,abs(strl_y_f[-1]-curr_y)/dy,abs(strl_z_f[-1]-curr_z)/dz)
			if dd >= dd_rec:
				strl_x_f.append(curr_x)
				strl_y_f.append(curr_y)
				strl_z_f.append(curr_z)

			wg_x_l = (x[id_x_h]-curr_x)/dx
			wg_y_l = (y[id_y_h]-curr_y)/dy
			wg_z_l = (z[id_z_h]-curr_z)/dy

			weight = np.array([wg_x_l,1.-wg_x_l])
			weight = np.array([wg_y_l*weight,(1.-wg_y_l)*weight])
			weight = np.array([wg_z_l*weight,(1.-wg_z_l)*weight])

			curr_vx = np.sum(vx[id_z_l:id_z_h+1,id_y_l:id_y_h+1,id_x_l:id_x_h+1]*weight)
			curr_vy = np.sum(vy[id_z_l:id_z_h+1,id_y_l:id_y_h+1,id_x_l:id_x_h+1]*weight)
			curr_vz = np.sum(vz[id_z_l:id_z_h+1,id_y_l:id_y_h+1,id_x_l:id_x_h+1]*weight)

			ff = max([abs(curr_vx), abs(curr_vy), abs(curr_vz)])/dd_rec
			if ff < flim:	# slower than limit
				break

			tt = min(tt_lim, tt_coeff / ff)
			curr_x += tt * curr_vx
			curr_y += tt * curr_vy
			curr_z += tt * curr_vz

	if drct == "Both" or drct == "Backward":
		curr_x = seed[0]
		curr_y = seed[1]
		curr_z = seed[2]
		while True:
			try:
				id_x_l = np.where((curr_x>=x))[0][-1]
				id_y_l = np.where((curr_y>=y))[0][-1]
				id_z_l = np.where((curr_z>=z))[0][-1]
				id_x_h = np.where((curr_x<x))[0][0]
				id_y_h = np.where((curr_y<y))[0][0]
				id_z_h = np.where((curr_z<z))[0][0]
			except IndexError:	# Out of the boundary
				break

			dx = x[id_x_h]-x[id_x_l]
			dy = y[id_y_h]-y[id_y_l]
			dz = z[id_z_h]-z[id_z_l]
			dd = max(abs(strl_x_b[-1]-curr_x)/dx,abs(strl_x_b[-1]-curr_y)/dy,abs(strl_x_b[-1]-curr_z)/dz)
			if dd >= dd_rec:
				strl_x_b.append(curr_x)
				strl_y_b.append(curr_y)
				strl_z_b.append(curr_z)

			wg_x_l = (x[id_x_h]-curr_x)/dx
			wg_y_l = (y[id_y_h]-curr_y)/dy
			wg_z_l = (z[id_z_h]-curr_z)/dy

			weight = np.array([wg_x_l,1.-wg_x_l])
			weight = np.array([wg_y_l*weight,(1.-wg_y_l)*weight])
			weight = np.array([wg_z_l*weight,(1.-wg_z_l)*weight])

			curr_vx = np.sum(vx[id_z_l:id_z_h+1,id_y_l:id_y_h+1,id_x_l:id_x_h+1]*weight)
			curr_vy = np.sum(vy[id_z_l:id_z_h+1,id_y_l:id_y_h+1,id_x_l:id_x_h+1]*weight)
			curr_vz = np.sum(vz[id_z_l:id_z_h+1,id_y_l:id_y_h+1,id_x_l:id_x_h+1]*weight)

			ff = max([abs(curr_vx), abs(curr_vy), abs(curr_vz)])/dd_rec
			#if ff < flim:	# slower than limit
			#	break

			tt = min(tt_lim, tt_coeff / ff)
			curr_x -= tt * curr_vx
			curr_y -= tt * curr_vy
			curr_z -= tt * curr_vz

	if drct == "Both":
		strl_x = np.array(strl_x_b[-1:0:-1] + strl_x_f)
		strl_y = np.array(strl_y_b[-1:0:-1] + strl_y_f)
		strl_z = np.array(strl_z_b[-1:0:-1] + strl_z_f)
		return strl_x, strl_y, strl_z
	if drct == "Forward":
		return np.array(strl_x_f), np.array(strl_y_f), np.array(strl_z_f)
	if drct == "Backward":
		return np.array(strl_x_b), np.array(strl_y_b), np.array(strl_z_b)
	if not ignore:
		raise ValueError("Something wrong happened at get_streamline3d().")
	return np.array([0.0]), np.array([0.0]), np.array([0.0])
#end of getStreamline3d

def getStreamline2d(x,y,vx,vy,seed=np.zeros(2), drct="Both", dd_rec=0.1, ignore=True):
	nums = (len(x),len(y))
	if nums != np.shape(vx) != np.shape(vy):
		raise TypeError("Sizes of arguments do not agree.")
	if (not ignore) or (x[0] > seed[0] >= x[-1]) or (y[0] > seed[1] >= y[-1]):
		raise ValueError("The seed point is out of the boundary.")

	strl_x_f = [seed[0]]
	strl_y_f = [seed[1]]

	strl_x_b = [seed[0]]
	strl_y_b = [seed[1]]

	vv_norm = 1.0/max(np.max(np.abs(vx)),np.max(np.abs(vy)))
	flim = 0.01
	tt_coeff = 0.1
	tt_lim = 0.1
	stop_param = 10

	if drct == "Both" or drct == "Forward":
		curr_x = seed[0]
		curr_y = seed[1]
		stop_cnt = -1
		while True:
			try:
				id_x_l = np.where((curr_x>=x))[0][-1]
				id_y_l = np.where((curr_y>=y))[0][-1]
				id_x_h = np.where((curr_x<x))[0][0]
				id_y_h = np.where((curr_y<y))[0][0]
			except IndexError:	# Out of the boundary
				#print("Out of the boundary break")
				break

			dx = x[id_x_h]-x[id_x_l]
			dy = y[id_y_h]-y[id_y_l]
			dd = max(abs(strl_x_f[-1]-curr_x)/dx,abs(strl_y_f[-1]-curr_y)/dy)
			if dd >= dd_rec:
				strl_x_f.append(curr_x)
				strl_y_f.append(curr_y)
				stop_cnt = 0
			else:
				if stop_cnt > stop_param:
					#print("Iteration limit break")
					break
				stop_cnt+=1

			wg_x_l = (x[id_x_h]-curr_x)/dx
			wg_y_l = (y[id_y_h]-curr_y)/dy

			weight = np.array([wg_x_l,1.-wg_x_l])
			weight = np.array([wg_y_l*weight,(1.-wg_y_l)*weight])
			curr_vx = np.sum(vx[id_y_l:id_y_h+1,id_x_l:id_x_h+1]*weight)*vv_norm
			curr_vy = np.sum(vy[id_y_l:id_y_h+1,id_x_l:id_x_h+1]*weight)*vv_norm

			ff = max([abs(curr_vx), abs(curr_vy)])/dd_rec
			if ff < flim:	# slower than limit
				#print("Slow limit break: v = ({0}, {1})".format(curr_vx,curr_vy))
				#print("vx = {0}".format(vx[id_y_l:id_y_h+1,id_x_l:id_x_h+1]))
				#print("vy = {0}".format(vy[id_y_l:id_y_h+1,id_x_l:id_x_h+1]))
				break

			tt = min(tt_lim, tt_coeff / ff)
			curr_x += tt * curr_vx
			curr_y += tt * curr_vy

	if drct == "Both" or drct == "Backward":
		curr_x = seed[0]
		curr_y = seed[1]
		stop_cnt = -1
		while True:
			try:
				id_x_l = np.where((curr_x>=x))[0][-1]
				id_y_l = np.where((curr_y>=y))[0][-1]
				id_x_h = np.where((curr_x<x))[0][0]
				id_y_h = np.where((curr_y<y))[0][0]
			except IndexError:	# Out of the boundary
				#print("Out of the boundary break")
				break

			dx = x[id_x_h]-x[id_x_l]
			dy = y[id_y_h]-y[id_y_l]
			dd = max(abs(strl_x_b[-1]-curr_x)/dx,abs(strl_y_b[-1]-curr_y)/dy)
			if dd >= dd_rec:
				strl_x_b.append(curr_x)
				strl_y_b.append(curr_y)
				stop_cnt = 0
			else:
				if stop_cnt > stop_param:
					#print("Iteration limit break")
					break
				stop_cnt+=1

			wg_x_l = (x[id_x_h]-curr_x)/dx
			wg_y_l = (y[id_y_h]-curr_y)/dy

			weight = np.array([wg_x_l,1.-wg_x_l])
			weight = np.array([wg_y_l*weight,(1.-wg_y_l)*weight])

			curr_vx = np.sum(vx[id_y_l:id_y_h+1,id_x_l:id_x_h+1]*weight)*vv_norm
			curr_vy = np.sum(vy[id_y_l:id_y_h+1,id_x_l:id_x_h+1]*weight)*vv_norm

			ff = max([abs(curr_vx), abs(curr_vy)])/dd_rec
			if ff < flim:	# slower than limit
				#print("Slow limit break: v = ({0}, {1})".format(curr_vx,curr_vy))
				break

			tt = min(tt_lim, tt_coeff / ff)
			curr_x -= tt * curr_vx
			curr_y -= tt * curr_vy

	if drct == "Both":
		strl_x = np.array(strl_x_b[-1:0:-1] + strl_x_f)
		strl_y = np.array(strl_y_b[-1:0:-1] + strl_y_f)
		return strl_x, strl_y
	if drct == "Forward":
		return np.array(strl_x_f), np.array(strl_y_f)
	if drct == "Backward":
		return np.array(strl_x_b), np.array(strl_y_b)
	if not ignore:
		raise ValueError("Something wrong happened at get_streamline3d().")
	return np.array([0.0]), np.array([0.0])
#end of getStreamline2d
