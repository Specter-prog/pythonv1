from bs4 import BeautifulSoup as bs 
import requests 

URL = 'https://www.kivano.kg/mobilnye-telefony'

response = requests.get(URL)
html = response.text
soup = bs(html, 'lxml')
telephone_list = soup.find_all('div', class_='item product_listbox oh')

telephones = []

for telephone in telephone_list:
    telephones.append(telephone.find('div', 'class=listbox_title oh')).text

print(telephones)