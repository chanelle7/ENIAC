import requests
from bs4 import BeautifulSoup

response = requests.get('https://14ers.com/routelist.php?peak=Grays+Peak+and+Torreys+Peak')
soup = BeautifulSoup(response.text, 'html.parser')
table_body = soup.find_all('tr')
mtd = []
## Puts all the meta route data into a very messy list
[mtd.append(x.get_text(strip=True)) for x in table_body]
[print(x) for x in mtd]









