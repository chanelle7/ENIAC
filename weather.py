
import re
import datetime

wmtndata = ['Mt. Belford',
           'TodayHigh: 59°F5-10mphChance Showers And Thunderstorms',
           'TonightLow: 40°F10-20mphChance Showers And Thunderstorms then Partly Cloudy',
           'MondayHigh: 48°F5-15mphMostly Sunny then Showers And Thunderstorms Likely',
           'MondayNightLow: 38°F5-10mphShowers And Thunderstorms Likely then Partly Cloudy',
           'TuesdayHigh: 47°F5-10mphMostly Sunny then Chance Showers And Thunderstorms',
           'TuesdayNightLow: 39°F5-10mphShowers And Thunderstorms Likely then Mostly Cloudy',
           'WednesdayHigh: 52°F10-15mphPartly Sunny then Showers And Thunderstorms',
           'WednesdayNightLow: 40°F10-15mphShowers And Thunderstorms Likely then Mostly Cloudy',
           'ThursdayHigh: 50°F15mphSlight Chance Showers And Thunderstorms then Showers And Thunderstorms',
           'ThursdayNightLow: 39°F10-15mphShowers And Thunderstorms Likely then Mostly Cloudy',
           '', ''], ['Mt. Bierstadt',
                     'TodayHigh: 57°F6-10mphChance Showers And Thunderstorms',
                     'TonightLow: 37°F7mphShowers And Thunderstorms Likely then Slight Chance Showers And Thunderstorms',
                     'MondayHigh: 51°F6-16mphShowers And Thunderstorms Likely',
                     'MondayNightLow: 36°F10-14mphChance Showers And Thunderstorms then Partly Cloudy',
                     'TuesdayHigh: 55°F14-18mphMostly Sunny then Showers And Thunderstorms Likely',
                     'TuesdayNightLow: 38°F9-14mphChance Showers And Thunderstorms then Partly Cloudy',
                     'WednesdayHigh: 55°F16mphMostly Sunny then Showers And Thunderstorms Likely',
                     'WednesdayNightLow: 39°F13mphChance Showers And Thunderstorms then Mostly Cloudy',
                     'ThursdayHigh: 51°F14mphShowers And Thunderstorms',
                     'ThursdayNightLow: 37°F9-14mphShowers And Thunderstorms Likely then Mostly Cloudy',
                     '', '']


def clean_weather(eachmtn):
	ind = 0
	dttmp = []
	full_weather = {}
	for item in eachmtn:
		full_string = re.search("(.+:) (\d+)°F(\d+)-?(\d+)?(mph)(.+)",item)
		day = re.search("(.+:)",item)
		if day:
			today = datetime.date.today()
			j = datetime.datetime(today.year, today.month, today.day)
			degree = full_string.group(2)
			windslow = full_string.group(3)
			windshigh = full_string.group(4) if full_string.group(4) else full_string.group(3)
			desc = full_string.group(6)
			wdate = (j + datetime.timedelta(hours=convert[ind])).strftime('%m-%d-%Y %H:%M:%S')
			dttmp.append((wdate,degree, windslow, windshigh, desc))
		ind = ind+1
	full_weather[eachmtn[0]] =tuple(dttmp)
	return full_weather


def mountain_weather(allmtn):
	weather_data = {}
	for mtn in allmtn:
		weather_data.update(clean_weather(mtn))
	return weather_data


final_weather = (mountain_weather(wmtndata))




