import telebot
from bs4 import BeautifulSoup as bs
import requests 

bot = telebot.TeleBot('7967907899:AAEhAJCShjxjBOilUE5oP4ejHwa-1FBMYrg')

keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
button1 = telebot.types.KeyboardButton('Новости')
button2 = telebot.types.KeyboardButton('Quit')
keyboard.add(button1, button2)

@bot.message_handler(commands = ['start'], content_types = ['text'])
def start_message(message):
    url = 'https://kaktus.media/?lable=8&date=2025-03-17&order=time'
    html = requests.get(url)
    soup = bs(html.text, 'lxml')
    info = soup.find_all('div', class_ = 'Tag--Article')
    for i, data in enumerate(info[:20], start = 1):
        title = data.text.strip()
        bot.send_message(message.chat.id, f'{i}. {title}', reply_markup = keyboard)
        

bot.polling(non_stop=True)