import re
import requests
from bs4 import BeautifulSoup

# Pulling the raw HTML for the entire page
res = requests.get('https://14ers.com/routes.php')
html = BeautifulSoup(res.text, 'html.parser')


# Getting table data for the mountain data
td = html.find_all('tr')
mtd = []
## Puts all the meta mountain data into a very messy list
for row in td:
	mtd.append(row.get_text(strip=True))



## Pulling the links for all of the routes to use at a later time in order to scrape the route data automatically
routes = []
for divtag in html.find_all('div', {'class': 'niceborder'}):
	for atag in divtag.find_all('a',href=True):
		if atag['href'][0:6] == 'routel':
			routes.append(atag['href'])
































# class Mountain():
# 	def __init__(self, name, elevation):
# 		self.name = name
# 		self.elevation = elevation
#
# 	def __repr__(self):
# 		return self.name + ':' + self.elevation
#
#
# def TransformMountain(mtdata):
# 	mountain = []
# 	for i in range(0, len(mtdata), 2):
# 		elevation = re.match('14,\d{3}', mtdata[i + 1]).group(0).replace(',', '')
# 		mountain.append(mountain(mtdata[i], int(elevation)))
# 	return mountain
#
#
# mountains = mountainstodf(data)

# mountaindict = {x.name: x.elevation for x in mountains}

# print(mountaindict)
