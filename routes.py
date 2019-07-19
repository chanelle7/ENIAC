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

