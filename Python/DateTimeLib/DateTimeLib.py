from datetime import datetime, timedelta

def decimal2datetime(decYear):
	# Convert decimal year (float) to datetime object
	try:
		size = len(decYear)
	except TypeError:
		year = int(decYear)
		base = datetime(year,1,1)
		return base+(base.replace(year=year+1)-base)*(decYear-year)
	date = []
	for ii in range(size):
		year = int(decYear[ii])
		base = datetime(year,1,1)
		date.append(base+(base.replace(year=year+1)-base)*(decYear[ii]-year))
	return
# end of decimal2datetime

def decimal2date(decYear):
	# Convert decimal year (float) to date ("YYYY-MM-DD HH:MM:SS.SSSSSS")
	try:
		size = len(decYear)
	except TypeError:
		year = int(decYear)
		base = datetime(year,1,1)
		return "{0}".format(base+(base.replace(year=year+1)-base)*(decYear-year))
	date = []
	for ii in range(size):
		year = int(decYear[ii])
		base = datetime(year,1,1)
		date.append("{0}".format(base+(base.replace(year=year+1)-base)*(decYear[ii]-year)))
	return
# end of decimal2date