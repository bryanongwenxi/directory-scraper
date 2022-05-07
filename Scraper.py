from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.sgdi.gov.sg/ministries/mti/statutory-boards/jtc/departments/eog').text
print(html_text)

