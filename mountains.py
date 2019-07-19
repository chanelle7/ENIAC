import re
import requests
from bs4 import BeautifulSoup

response = requests.get('https://14ers.com/routes.php')
html = BeautifulSoup(response.text, 'html.parser')
#results = html.table.tr.get_text()
#results = html.find_all('tr')
#item = []
#for r in results:
#	item.append(r.get_text(strip=True))
#print(item)
routes = []
for tag in html.find_all('div', {'class': 'niceborder'}):
	for a in tag.find_all('a',href=True):
		routes.append(a['href'])
print(routes)



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
