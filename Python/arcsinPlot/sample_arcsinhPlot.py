from arcsinhPlot import setArcsinh

import numpy as np
import matplotlib.pyplot as plt


x = np.arange(-10,10.1,0.1)
y = np.arange(-10,10.1,0.1)

mesh_x, mesh_y = np.meshgrid(x,y)

#z = np.log10(mesh_x**2 + mesh_y**2)
z = np.sinc(np.sqrt(mesh_x**2+mesh_y**2))

lvl = np.arange(-1,1.1,0.1)

base = 10
num = 2
tick_base = (np.ones(num)*base)**np.arange(num)
tick = np.hstack((-1*tick_base[-1::-1],0,tick_base)) 
print(tick)

fig, axs = plt.subplots(2,2,figsize=(10,10),dpi=100)

axs[0,0].plot(x[::10],y[::10], "*-")
axs[0,0].set_aspect('equal', 'box')
axs[0,0].set_xticks(tick)
axs[0,0].set_xticklabels(tick)
axs[0,0].set_yticks(tick)
axs[0,0].set_yticklabels(tick)
axs[0,0].set_title("y=x in linear scale")

setArcsinh(axs[0,1].plot,x[::10],y[::10],"*-",dim=2)
axs[0,1].set_aspect('equal', 'box')
setArcsinh(axs[0,1].set_xticks,tick)
axs[0,1].set_xticklabels(tick)
setArcsinh(axs[0,1].set_yticks,tick)
axs[0,1].set_yticklabels(tick)
axs[0,1].set_title("y=x in arcsinh scale")

axs[1,0].contourf(x,y,z,lvl)
axs[1,0].set_aspect('equal', 'box')
axs[1,0].set_xticks(tick)
axs[1,0].set_xticklabels(tick)
axs[1,0].set_yticks(tick)
axs[1,0].set_yticklabels(tick)
axs[1,0].set_title("z=sinc(r) in linear scale")

setArcsinh(axs[1,1].contourf,x,y,z,lvl,dim=2)
axs[1,1].set_aspect('equal', 'box')
setArcsinh(axs[1,1].set_xticks,tick)
axs[1,1].set_xticklabels(tick)
setArcsinh(axs[1,1].set_yticks,tick)
axs[1,1].set_yticklabels(tick)
axs[1,1].set_title("z=sinc(r) in arcsinh scale")

plt.show()
