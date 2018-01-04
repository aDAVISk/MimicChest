#########################################################################
# FILE: MyMarble.pyplot 												#
# AUTHOR: Akito D. Kawamura (@aDAVISk)									#
#																		#
# Special Thanks to the following webpages								#
#   http://matplotlib.org/basemap/users/examples.html					#
#   http://matplotlib.org/examples/pylab_examples/contourf_demo.html	#
#   http://basemaptutorial.readthedocs.io/en/latest/subplots.html		#
#   and other websites for minor problems I faced.						#
#########################################################################
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np 

# File name of the resulting plot
ofname="MyMarble.png"

# Generating a marble color map
delta=1 # integer degree
nlats=180/delta+1
nlons=360/delta+1
ddeg = np.pi*delta/180
lats = (0.5*np.pi-ddeg*np.indices((nlats,nlons))[0,:,:])
lons = (ddeg*np.indices((nlats,nlons))[1,:,:])
wave = np.sin(3.*lats+3.*lons)
levels = np.arange(-0.5,0.5,0.1)

mycmap = plt.cm.get_cmap("spectral")

myfig=plt.figure()

ax1 = myfig.add_subplot(121)
mymap = Basemap(projection="ortho", lat_0=0,lon_0=0,resolution="l")
mymap.drawmapboundary()
mymap.drawmeridians(np.arange(0,360,30))
mymap.drawparallels(np.arange(-90,90,30))
x, y = mymap(lons*180./np.pi,lats*180./np.pi)
cs = mymap.contourf(x,y,wave,levels, cmap=mycmap)
ax1.set_title("side view")

ax2 = myfig.add_subplot(122)
mymap = Basemap(projection="ortho", lat_0=90,lon_0=0,resolution="l")
mymap.drawmapboundary()
mymap.drawmeridians(np.arange(0,360,30))
mymap.drawparallels(np.arange(-90,90,30))
x, y = mymap(lons*180./np.pi,lats*180./np.pi)
cs = mymap.contourf(x,y,wave,levels,cmap=mycmap)
ax2.set_title("top view")

plt.suptitle("My marble from two Viewpoints")
mycax = myfig.add_axes([0.1,0.1,0.8,0.03])
myfig.colorbar(cs, cax=mycax, orientation="horizontal")

plt.savefig(ofname) # Sace before show() and then close
print("The plot is saved to {0:s}".format(ofname))
plt.show()
