######################################################
# getBodyPos.py
# author: Akito D. Kawamura (aDAVISk)
# This program will get the geocentric position 
# of a celestial body in our solar system.  
#
# License: BSD 3-Clause License
# (see LICENSE file for more detail)
#
# WARNING: This program do not accept date before
# common era (BCE a.k.a. AD) in iso format. To use 
# ephemeris="jpl", jplephem package is required.
# This program may not give acculate answer for dates
# before 1900.
#######################################################
import astropy.coordinates as astcoor
from astropy.coordinates import solar_system_ephemeris
import numpy as np 
from astropy.time import Time
from astropy.time import TimeDelta
from datetime import datetime


BodyList = solar_system_ephemeris.bodies
print("BodyList = {0}\n".format(BodyList))

myBody = BodyList[1]

myTime = Time("2018-01-01 00:00:00.000",format="iso")

myPos = astcoor.get_body(myBody,myTime,ephemeris="jpl")
print("Position of {0} = {1}\n".format(myBody,myPos))
