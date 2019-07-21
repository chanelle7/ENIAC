import re
import datetime
convert = {1:0,2:12,3:24,4:36,5:48,6:60,7:72,8:84,9:96,10:108}
data = ['Mt. Antero', 'TodayHigh: 60°F5-10mphChance Showers And Thunderstorms',
 'TonightLow: 43°F10-15mphChance Showers And Thunderstorms then Mostly Cloudy',
 'MondayHigh: 53°F5-10mphMostly Sunny then Chance Showers And Thunderstorms',
 'MondayNightLow: 41°F5-15mphShowers And Thunderstorms Likely then Partly Cloudy',
 'TuesdayHigh: 52°F10mphMostly Sunny then Chance Showers And Thunderstorms',
 'TuesdayNightLow: 42°F5-10mphShowers And Thunderstorms Likely then Mostly Cloudy',
 'WednesdayHigh: 55°F10-15mphPartly Sunny then Showers And Thunderstorms',
 'WednesdayNightLow: 42°F10-15mphShowers And Thunderstorms Likely then Mostly Cloudy',
 'ThursdayHigh: 53°F15mphPartly Sunny then Showers And Thunderstorms',
 'ThursdayNightLow: 42°F10-15mphShowers And Thunderstorms then Mostly Cloudy',
 '', '']

ind = 0
for i in data:
	full_string = re.search("(.+:)( \d+)(°F)(\d+-?\d+)(mph)(.+)",i)
	day = re.search("(.+:)",i)
	dttmp = []
	if day:
		today = datetime.date.today()
		degree = full_string.group(2)
		j = datetime.datetime(today.year, today.month, today.day)
		string = day.span()
		day = day.group(1)
		date = (j + datetime.timedelta(hours=convert[ind]))
		dttmp.append([date, degree])
	else:
		pass
	ind = ind+1
	print(dttmp)


