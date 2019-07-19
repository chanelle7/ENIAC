import re
import requests
from bs4 import BeautifulSoup

# Pulling the raw HTML for the entire page
res = requests.get('https://14ers.com/php14ers/peakusage.php')
html = BeautifulSoup(res.text, 'html.parser')
crowd_size = []

# Pulling general crowd size data

for divtag in html.find_all('table', {'class': 'MainText1'}):
	for atag in divtag.find_all('tr'):
		crowd_size.append(atag.get_text(strip=True))

