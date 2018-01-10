########################################################
# KSGoesXrs.py
# Author: Akito D. Kawamura
# This program will compare two Goes X-ray reports
# with Kolmogorov-Smirnov Test.
# 
# This program uses ReadGoesXrsReport from 
# https://github.com/aDAVISk/PythonForSpaceWeather/tree/master/ReadGoesXrsReport 
# and Goes Xrs Report from 
# https://www.ngdc.noaa.gov/stp/space-weather/solar-data/solar-features/solar-flares/x-rays/goes/xrs/ 
# 
# This program is published under BSD 3-Clause License
# Please use this program under your responsibility.
########################################################

from ReadGoesXrsReport import *
import scipy.stats as sts

flares1 = ReadGoesXrsReport("./goes-xrs-report_2003.txt")
flares2 = ReadGoesXrsReport("./goes-xrs-report_2008.txt")
flux1 = [flares1[ii].flux for ii in range(len(flares1))]
flux2 = [flares2[ii].flux for ii in range(len(flares2))]
D, p = sts.ks_2samp(flux1,flux2)
print("p = {0}".format(p))
