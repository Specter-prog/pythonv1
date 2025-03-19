from bs4 import BeautifulSoup as bs
import requests 
import json

response = requests.get(url='https://www.mashina.kg/')
html = response.text
soup = bs(html, 'lxml')

models = []
prices = []
images = []
descriptions = []

car_list = soup.find_all('div', class_='list-view')

for car in car_list:
    models.append(car.find('div', class_='main-title').text.strip())
    prices.append(car.find('span', class_='currency-2').text.strip())
    images.append(car.find('div', class_='main-image').find('img').get('src'))
   # descriptions.append(car.find('div', class_='characteristics').text.strip())

car_data = []
for model, price, image in zip(models, prices, images):
    car_data.append({
        'Model:':model,
        'Price:':price,
        'Image':image,
    })

with open('car_models.json', 'w') as jsonfile:
    json.dump(car_data, jsonfile)


