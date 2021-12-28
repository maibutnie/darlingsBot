import telebot
from telebot import types
import pyowm 
import time
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('3a67c5c3b5d76d479a049e2fc8de64b4', config_dict)

def weather(message, bot):
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place('Москва')
    weather = observation.weather
    temp = weather.temperature("celsius")["temp"]
    temp = round(temp)
    veter = weather.wind()['speed']
    print(time.ctime(), "UID:", message.from_user.id, "Сообщение:", message.text.title(), "Температура:", temp)
    answer = f"В городе " + message.text + " сейчас " + str(weather.detailed_status) + "." + "\n"
    answer += f"Температура около: " + str(temp) + " С." + "\n"
    answer += f'Скорость ветра примерно: ' + str(veter) + 'м\c.' + '\n'
    if veter <= 0.2:
        answer += f'На улице нет ветра.'
    if veter > 0.2 and veter <= 1.5:
        answer += f'На улице тихий ветер.'
    if veter > 1.5 and veter <= 6:
        answer += f'На улице легкий ветер.'
    if veter > 6 and veter <= 10:
        answer += f'На улице слабый ветер.'
    if veter > 11 and veter <= 16:
        answer += f'На улице крепкий ветер.'
    if veter > 16 and veter <= 30:
        answer += f'На улице очень сильный ветер, буря.'
    bot.send_message(message.chat.id, answer)
    bot.send_message(message.chat.id, 'https://yandex.ru/pogoda/moscow?lat=55.753215&lon=37.622504')