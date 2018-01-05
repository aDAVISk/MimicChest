###############################################
# ImshowNum.py
# Author: Akito D. Kawamura (aDAVISk)
# Published under BSD 3-clause license
# Last Update: 2018/01/05
###############################################

import numpy as np 
import matplotlib.pyplot as plt

sx = 20
sy = 15
vmax = 100

count = (vmax*np.random.rand(sy,sx)).astype(np.int)

fig = plt.figure(figsize=(12,9),dpi=100)
ax = fig.add_subplot(1,1,1)
im = ax.imshow(count, interpolation='none', vmax=vmax,vmin=0, cmap='rainbow',origin='lower')
fig.colorbar(im, ticks=range(0,vmax+1,10))
for jj in range(sy):
	for ii in range(sx):
		ax.text(ii,jj,count[jj,ii],ha='center',va='center')
plt.show()
#plt.pause(10)
