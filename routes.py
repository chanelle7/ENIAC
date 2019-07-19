import requests
from bs4 import BeautifulSoup

response = requests.get('https://14ers.com/routelist.php?peak=Grays+Peak+and+Torreys+Peak')
html = BeautifulSoup(response.text, 'html.parser')
routes = []
for a in html.find_all('div', {'class': 'niceborder'}):
#for a in html.find_all('a',href=True):
	routes.append(a['href'])
print(routes)
