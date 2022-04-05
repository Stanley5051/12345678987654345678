import telebot
from config import TOKEN, currency
from extensions import APIException, Convertor
import traceback
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def help(message: telebot.types.Message):
    text = "Привееет, рад видеть 🤗! Чо как оно в целом?\n Я обладаю очень полезным, в наше безумное время, навыком 😎 \
    Я умею рассчитывать стоимость иностранных валют! \
Как это сделать я объясню тут: /help \n \
Тыкай сюда, что бы увидеть список валют: /values"


    bot.reply_to(message, text)

@bot.message_handler(commands=['help'])
def help(message: telebot.types.Message):
    text = "Я умею Конвертировать валюты! Круто да? Для этого тебе надо ввести \n  \
<имя валюты, цену которой ты хочешь узнать, в именительном падеже> \n\
<имя валюты, в которой надо узнать цену первой валюты, тоже в именительном падеже> \n\
<количество первой валюты>\n \
И я тебе разъясню почём фунт лиха 😃  \n \
Тыкай сюда что бы увидеть список валют: /values"

    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Имеем дело с:'
    for key in currency.keys():
        text = '\n'.join((text, key,  ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    values = message.text.split()
    try:
        if len(values) != 3:
            raise APIException('Уоу! должно быть задано три параметра 🥴 /help')

        answer = Convertor.get_price(*values)
    except APIException as e:
        bot.reply_to(message, f"Какая-то ошибка в команде 🤔 :\n{e}")
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        bot.reply_to(message, f"А это, друг мой, неизвестная ошибка 😳 :\n{e}")
    else:
        bot.reply_to(message, answer)

APIException

Convertor

bot.polling()
