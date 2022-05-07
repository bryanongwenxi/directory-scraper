from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.sgdi.gov.sg/ministries/mti/statutory-boards/jtc/departments/eog').text
soup = BeautifulSoup(html_text, 'lxml')
names = soup.find_all('span', class_ = 'left')

print(names)