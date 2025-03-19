import telebot
from telebot import types

bot = telebot.TeleBot('7754418456:AAG55luuOnpVoT0016B4Ef0AHN48akmpn6s')

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True) # если нсколько кнопок вы можете использовать row_width = 2

button1 = types.KeyboardButton('Инфо о себе')

keyboard.add(button1)

@bot.message_handler(commands=['start', 'hi'])
def start_message(message):
    message2 = bot.send_message(message.chat.id, 'Привет, напиши ифнормацию о себе, я сохраню это в файлах')
    bot.register_next_step_handler(message, save_info)

def save_info(message):
    try:
        with open('user_info.txt', 'a') as file:
            info = message.text
            file.write(info+'\n')
    except:
        bot.send_message(message.chat.id, 'Чтото пошло не так, попробуй заново!')
    else:
        bot.send_message(message.chat.id, 'Все успешно сохранилось!!!', reply_markup=keyboard)
    finally:
        print('ОК')

@bot.message_handler(content_types=['text'])
def send_info(message):
    if message.text == 'Инфо о себе'.lower():
        with open('user_info.txt', 'r') as file:
            bot.send_document(message.chat.id, file)
    else:
        bot.send_message(message.chat.id, 'Нажмиете на кнопку!', reply_markup=keyboard)
    
bot.polling(non_stop=True, interval=0)