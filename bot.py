import random
import telebot
from telebot.types import File, Message, Sticker, MessageAutoDeleteTimerChanged
import fileReader as fr
import anecdot
import weather 
from pyowm import OWM
from pyowm.utils.config import get_default_config

bot = telebot.TeleBot('5096656471:AAGNIeQOigwuxiA6Vuz34iFRj4nPqd_OAgU')

agreetings = fr.FileReader('agreetings.txt').ReadFile()
stikres = fr.FileReader('stikers.txt').ReadFile()

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower().find('привет') != -1:
        bot.send_message(message.chat.id, random.choice(agreetings))
    elif message.text.lower().find('пока') != -1:
        bot.send_message(message.chat.id, 'УРРРРРААААА ОТДЫЫЫЫЫХ')
    elif message.text.lower().find('как дела') != -1:
        bot.send_message(message.chat.id, 'было лучше, пока ты не написал')
    elif message.text.lower().find('анекдот') != -1:
        anecdot.anecdot(message,bot)
    elif message.text.lower().find('погода') != -1:
        weather.weather(message, bot)
    elif message.text == '\start':
        bot.send_message(message.chat.id, 'Я расстроен, что ты тут \n Команды: \n', 'привет,\n пока,\n как дела,\n анекдот,\n погода')
    elif message.text == '\help':
        bot.send_message(message.chat.id, 'Команды: \n', 'привет,\n пока,\n как дела,\n анекдот,\n погода')
    else:
        bot.send_message(message.chat.id, 'от тебя веет вайбом водолея, может начнешь нормально общаться?')


@bot.message_handler(content_types=["photo","video","sticker", "file"])
def tell_stickers(message):
    bot.send_sticker(message.chat.id, random.choice(stikres))
    
bot.polling() 
    