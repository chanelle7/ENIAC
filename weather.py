import re
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Pulling the raw HTML for the entire page
res = requests.get('https://14ers.com/php14ers/ajax_weather1.php?location=Redcloud+Peak&lat=37.940880&lon=-107.421654')
html = BeautifulSoup(res.text, 'html.parser')
weather = []

## Puts all the  mountain weather data into a very messy list
for divtag in html.find_all('table', {'class': 'forecastDays'}):
	weather.append('Redcloud Peak')
	for atag in divtag.find_all('td'):
		weather.append(atag.get_text(strip=True))

[print(x) for x in weather]


