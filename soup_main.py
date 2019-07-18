import re
import requests
from bs4 import BeautifulSoup


response = requests.get('https://www.14ers.com/')
text = BeautifulSoup(response.text, 'html.parser')

mountaindata = text.find_all('td')

mountaintext = [tag.string for tag in mountaindata if tag.string != None and tag.string.strip() != '']
newdata = [text.strip() for text in mountaintext]

class Mountain():
	def __init__(self, name, elevation):
		self.name = name
		self.elevation = elevation

	def __repr__(self):
		return self.name + ':' + self.elevation


def mountainstodf(mountains):
	mountainlst = []
	for i in range(0, len(mountains), 2):
		elevation = (re.match('14,\d{3}', mountains[i + 1]).group(0).replace(',', ''))
		mountainlst.append(Mountain(mountains[i], int(elevation)))
	return mountainlst

mountains = mountainstodf(newdata)

mountaindict = {x.name: x.elevation for x in mountains}

print(mountaindict)




