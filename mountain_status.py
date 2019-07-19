import re
import requests
from bs4 import BeautifulSoup

# Pulling the raw HTML for the entire page
res = requests.get('https://14ers.com/php14ers/peakstatus_main.php')
html = BeautifulSoup(res.text, 'html.parser')
status = []

for div in html.find_all('table',{'class':'peakTable'}):
	for atag in div.find_all('a', href=True):
		mt = re.search('14ers', atag['href'])
		if mt:
			status.append(atag.get_text(strip=True))
			if len(atag.span['class']) == 1:
				status.append('No Updates')
			else:
				status.append(atag.span['class'][1])


