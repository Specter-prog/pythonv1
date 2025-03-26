from bs4 import BeautifulSoup as bs
import requests
import json
from time import sleep

while True:
    url = 'https://www.kivano.kg/mobilnye-telefony'
    response = requests.get(url)
    html = response.text
    soup = bs(html, 'lxml')
    phones = soup.find_all('div', class_='item product_listbox oh')

    phone_data = []
    for phone in phones:
        name = phone.find('img').get('alt')
        price = phone.find('div', class_='listbox_price').text.strip()
        image = phone.find('img').get('src')
        phone_data.append({'Model Name': name, 'Price': price, 'Image': url + image})

    with open('phones.json', 'w') as jsonfile:
        json.dump(phone_data, jsonfile, indent = 4, ensure_ascii = False)
    sleep(3600)
