##########################################################
# testStreamline.py
# Author: Akito D. Kawamura
# This program tests my streamline.py for 3D.
#
# This program is published under BSD 3-Clause License.
# This program is a beta version.
# Please use this program under your responsibility.
##########################################################

import streamline as strl 
import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

v0 = 1.0
B0 = 1.0

sx = 10
sy = 10
sz = 10
dx = 1.0
dy = 1.0
dz = 1.0

xx = np.arange(sx) * dx - sx * dx * 0.5
yy = np.arange(sy) * dy - sy * dy * 0.5
zz = np.arange(sz) * dz - sz * dz * 0.5
mesh_yy, mesh_zz, mesh_xx = np.meshgrid(zz,yy,xx)

Bx = np.zeros((sz,sy,sx))
By = B0*np.sin(np.pi*mesh_xx*0.5)
Bz = B0*np.cos(np.pi*mesh_xx*0.5)

vx = v0 * 0.5 * np.ones((sz,sy,sx))
vy = v0 * 0.5 * np.sin(np.pi*mesh_xx*0.5)
vz = v0 * 0.5 * np.cos(np.pi*mesh_xx*0.5)

mySeed =  np.array([-4.0, 0.0, 0.0])

fig = plt.figure(figsize=(8,8))
ax = fig.gca(projection='3d')
qvr = ax.quiver(mesh_xx,mesh_yy,mesh_zz,vx,vy,vz)

tt = 0.2

new_pos = mySeed
strl_x, strl_y, strl_z = strl.getStreamline(xx,yy,zz,Bx,By,Bz, seed=new_pos)
#print("strl = {0}, {1}".format(strl_x,strl_y))
ax.plot(strl_x,strl_y,strl_z, "r--")
for ii in range(50):
	old_pos = new_pos
	# Linear Interpolation
	id_x_l = np.where((old_pos[0]>=xx))[0][-1]
	id_y_l = np.where((old_pos[1]>=yy))[0][-1]
	id_z_l = np.where((old_pos[2]>=zz))[0][-1]
	id_x_h = np.where((old_pos[0]<xx))[0][0]
	id_y_h = np.where((old_pos[1]<yy))[0][0]
	id_z_h = np.where((old_pos[2]<zz))[0][0]

	dx = xx[id_x_h]-xx[id_x_l]
	dy = yy[id_y_h]-yy[id_y_l]
	dz = zz[id_z_h]-zz[id_z_l]

	wg_x_l = (xx[id_x_h]-old_pos[0])/dx
	wg_y_l = (yy[id_y_h]-old_pos[1])/dy
	wg_z_l = (zz[id_z_h]-old_pos[2])/dy

	weight = np.array([wg_x_l,1.-wg_x_l])
	weight = np.array([wg_y_l*weight,(1.-wg_y_l)*weight])
	weight = np.array([wg_z_l*weight,(1.-wg_z_l)*weight])

	curr_vx = np.sum(vx[id_z_l:id_z_h+1,id_y_l:id_y_h+1,id_x_l:id_x_h+1]*weight)
	curr_vy = np.sum(vy[id_z_l:id_z_h+1,id_y_l:id_y_h+1,id_x_l:id_x_h+1]*weight)
	curr_vz = np.sum(vz[id_z_l:id_z_h+1,id_y_l:id_y_h+1,id_x_l:id_x_h+1]*weight)

	# update position and plot
	new_pos = old_pos + tt * np.array([curr_vx,curr_vy,curr_vz])
	strl_x, strl_y, strl_z = strl.getStreamline(xx,yy,zz,Bx,By,Bz, seed=new_pos)
	ax.plot(strl_x,strl_y,strl_z, "g--")
	ax.plot([new_pos[0],old_pos[0]],[new_pos[1],old_pos[1]],[new_pos[2],old_pos[2]],"ro")
	#ax.streamplot(xx,yy,vx,vy)
	plt.pause(0.1)
plt.show()
