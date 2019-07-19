import re
import requests
from bs4 import BeautifulSoup

# Pulling the inital HTML for the entire page
response = requests.get('https://14ers.com/routes.php')
html = BeautifulSoup(response.text, 'html.parser')


class get_raw_data():
		def get_mountains(self):
			mountain_data = []
			td = html.find_all('tr')
			[mountain_data.append(row.get_text(strip=True)) for row in td]
			return mountain_data

		mountain_data = get_mountains()
		print(mountain_data)

		def get_route_list(self):
			route_pages = set()
			for divtag in html.find_all('div', {'class': 'niceborder'}):
				for atag in divtag.find_all('a',href=True):
					route_pages = route_pages.union({atag['href'] for tag in atag if atag['href'][0:6] == 'routel'})
			return route_pages

		#route_pages = get_route_list()

		def get_routes(self):
			routes = set({})
			for link in route_pages:
				response = requests.get('https://14ers.com/' + link)
				html = BeautifulSoup(response.text, 'html.parser')
				table_body = html.find_all('tr')
				[routes.add(x.get_text(strip=True)) for x in table_body if x.get_text(strip=True)[:4] != 'Trip']

		#routes = get_routes()

		def get_crowdsize(self):
			crowd_size = []
			response = requests.get('https://14ers.com/php14ers/peakusage.php')
			html = BeautifulSoup(response.text, 'html.parser')
			for divtag in html.find_all('table', {'class': 'MainText1'}):
				[crowd_size.append(atag.get_text(strip=True)) for atag in divtag.find_all('tr')]

		#crowd_size = get_crowdsize()

		def get_status(self):
			status = []
			response = requests.get('https://14ers.com/php14ers/peakstatus_main.php')
			html = BeautifulSoup(response.text, 'html.parser')
			for div in html.find_all('table', {'class': 'peakTable'}):
				for atag in div.find_all('a', href=True):
					mt = re.search('14ers', atag['href'])
					if mt:
						status.append(atag.get_text(strip=True))
						if len(atag.span['class']) == 1:
							status.append('No Updates')
						else:
							status.append(atag.span['class'][1])
			return status

			#status  = get_status()

class Mountain():
	def __init__(self, name, elevation):
		self.name = name
		self.elevation = elevation
	def __repr__(self):
		return self.name + ':' + self.elevation
def TransformMountain(mtdata):
	mountain = []
	for i in range(0, len(mtdata), 2):
		elevation = re.match('14,\d{3}', mtdata[i + 1]).group(0).replace(',', '')
		mountain.append(mountain(mtdata[i], int(elevation)))
	return mountain


# if __name__ == '__main__':
# 	get_mountains()
# 	get_route_list()
# 	get_routes()
# 	get_crowdsize()
# 	get_status()
#
#























#
#
# mountains = mountainstodf(data)

# mountaindict = {x.name: x.elevation for x in mountains}

# print(mountaindict)
