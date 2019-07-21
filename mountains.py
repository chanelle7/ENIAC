import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy

#
# response = requests.get('https://14ers.com/routes.php')
# html = BeautifulSoup(response.text, 'html.parser')
#
#
# def get_mountains():
# 	mountain_data = []
# 	td = html.find_all('tr')
# 	mountain_data = ([row.get_text(strip=True) for row in td if row.get_text(strip=True)[:6] != 'Routes'])
# 	return mountain_data
#
# mountain_data = get_mountains()
#
#
# # Working on getting this into a proper data frame for later
# def clean_mountain_data(mountain_data):
# 	mountain_detail = []
# 	reg = "(.+)(14,\d{3})(')(\d+|\*?)(.+)"
# 	for i in range(0, len(mountain_data)):
# 		match = re.match(reg,str(mountain_data[i]))
# 		mountain = []
# 		mountain.append(match.group(1))
# 		mountain.append(int(match.group(2).replace(',','')))
# 		mountain.append(int(match.group(4).replace('*','-1')))
# 		mountain.append(match.group(5))
# 		mountain_detail.append(mountain)
# 	return mountain_detail
#
# mountains = clean_mountain_data(mountain_data)
# df = pd.DataFrame(mountains,columns=['Peak','Elevation','Rank','Range']) #.set_index('Peak')
#print(df['Peak'])

# def get_route_list(html):
# 	route_pages = set()
# 	for divtag in html.find_all('div', {'class': 'niceborder'}):
# 		for atag in divtag.find_all('a',href=True):
# TODO: Do I need the .union here - didn't need it above
# 			route_pages = route_pages.union({atag['href'] for tag in atag if atag['href'][0:6] == 'routel'})
# 	return route_pages
#
# #route_pages = get_route_list()
#
# def get_routes(route_pages):
# 	routes = set({})
# 	for link in route_pages:
# 		response = requests.get('https://14ers.com/' + link)
# 		html = BeautifulSoup(response.text, 'html.parser')
# 		table_body = html.find_all('tr')
# 		[routes.add(x.get_text(strip=True)) for x in table_body if x.get_text(strip=True)[:4] != 'Trip']
#
# #routes = get_routes()
#
# def get_crowdsize():
# 	crowd_size = []
# 	response = requests.get('https://14ers.com/php14ers/peakusage.php')
# 	html = BeautifulSoup(response.text, 'html.parser')
# 	for divtag in html.find_all('table', {'class': 'MainText1'}):
# 		[crowd_size.append(atag.get_text(strip=True)) for atag in divtag.find_all('tr')]
#
# #crowd_size = get_crowdsize()
#
# def get_status():
# 	status = []
# 	response = requests.get('https://14ers.com/php14ers/peakstatus_main.php')
# 	html = BeautifulSoup(response.text, 'html.parser')
# 	for div in html.find_all('table', {'class': 'peakTable'}):
# 		for atag in div.find_all('a', href=True):
# 			mt = re.search('14ers', atag['href'])
# 			if mt:
# 				status.append(atag.get_text(strip=True))
# 				if len(atag.span['class']) == 1:
# 					status.append('No Updates')
# 				else:
# 					status.append(atag.span['class'][1])
# 	return status

# Pulling the raw HTML for the entire page
def get_weather_urls():
	response = requests.get('https://www.14ers.com/php14ers/weather.php')
	html = BeautifulSoup(response.text, 'html.parser')
	name = "(.+)(,)( )(Mt.)"
	urls = dict({})
	for div in html.find_all('optgroup', {'label': 'Colorado 14ers'}):
		for atag in div.find_all('option'):
			url = 'https://www.14ers.com/php14ers/ajax_weather1.php?' + atag['value']
			match = re.search(name, str(atag.text))
			if match:
					mtn_name = re.search(name, str(atag.text)).group(4) + ' ' + re.search(name, str(atag.text)).group(1)
			else:
					mtn_name = atag.text
			urls[mtn_name] = url
	return urls

def get_mountain_weather():
	mtn_url = get_weather_urls()
	reg = "(.+)(:)( \d+)(°F)(\d+-?\d+)(mph)(.+)"
	all_weather = []
	for mtn_name,url in mtn_url.items():
		response = requests.get(url)
		html = BeautifulSoup(response.text, 'html.parser')
		weather = [mtn_name]
		for divtag in html.find_all('table', {'class': 'forecastDays'}):
			for atag in divtag.find_all('td'):
				weather.append(atag.get_text(strip=True))
		all_weather.append(weather)
	return all_weather

print(get_mountain_weather())


def clean_weather():
	raw = get_mountain_weather()
	for i in raw:
		print(i)




# #status  = get_status()
#
# class Mountain():
#
# 	def __init__(self, name, elevation):
# 		self.name = name
# 		self.elevation = elevation
#
# 	def __repr__(self):
# 		return self.name + ':' + self.elevation
#
#
#
# # mountaindict = {x.name: x.elevation for x in mountains}
#
# # print(mountaindict)
#
#
#
#
# # if __name__ == '__main__':
# # 	get_mountains()
# # 	get_route_list()
# # 	get_routes()
# # 	get_crowdsize()
# # 	get_status()
