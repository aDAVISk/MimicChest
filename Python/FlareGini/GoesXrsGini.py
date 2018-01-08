from ReadGoesXrsReport import *
from time import sleep
import matplotlib.pyplot as plt
import numpy as np
import math

#flares = ReadGoesXrsReport("./goes-xrs-report_1983.txt")
flares = ReadGoesXrsReport("./goes-xrs-report_2003.txt")

ss = len(flares)

flares.sort(key=lambda FlareEvent: FlareEvent.flux)

fluxInt = np.zeros(ss)
ClassFirst = np.zeros(5, dtype=int)

FlareClassIdx = {"A":0, "B":1, "C":2, "M":3, "X":4}
FlareClassKeys = ["A", "B", "C", "M", "X"]

for ii in range(ss):
	fluxInt[ii] = fluxInt[ii-1]+flares[ii].flux
	#print("{0}".format(fluxInt[ii]))
	if ClassFirst[FlareClassIdx[flares[ii].clss]] == 0:
		ClassFirst[FlareClassIdx[flares[ii].clss]] = ii + 1
ClassFirst -= 1

gini = 1 - np.sum(fluxInt)/(fluxInt[ss-1]*ss/2)
fig, ax = plt.subplots()

for ii in range(5):
	if ClassFirst[ii] >= 0:
		ax.plot([ClassFirst[ii],ClassFirst[ii]],[0,fluxInt[ss-1]], ls=":", color="gray")
		nextIdx = ClassFirst[ii]+40
		if ii < 4:
			nextIdx = ClassFirst[ii+1] 
		ax.text((ClassFirst[ii]+nextIdx)/2-10,fluxInt[ss-1]*0.4,FlareClassKeys[ii])

ax.plot([0,ss],[0,fluxInt[ss-1]], color="gray")

ax.plot(range(1,ss+1),fluxInt, color="black")

ax.set(title="Flare Flux Distribution (2003): Gini Coefficient = {0:4.2f}".format(gini),\
		xlabel="number of events", ylabel="Integrated Maximum Flux(Watt/m**2)", \
		xlim=[0,ss],ylim=[0,fluxInt[ss-1]])

pltbox = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
angle = math.atan(pltbox.height/pltbox.width)*180/math.pi
ax.text(ss/2,fluxInt[ss-1]*0.61,"Line of Equality", ha="center", rotation=angle)
ax.text(ss/2,fluxInt[int(ss/2)]*3,"Lorenz Curve of Integrated Flux", ha="center", rotation=10)

plt.show()

