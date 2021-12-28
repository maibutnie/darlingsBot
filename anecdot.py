from pyowm import OWM
from pyowm.utils.config import get_default_config
import telebot
import requests
import json

def anecdot(message, bot):
    res = requests.get('http://rzhunemogu.ru/RandJSON.aspx?CType=1')
    try:
        strk=json.JSONDecoder(strict=False).decode(res.content.decode('windows-1251'))
        bot.send_message(message.chat.id, ' анекдот \n {}'.format(strk['content']))
    except:
        strk = {'content':'что-то пошло не так :( попробуй еще раз'}
        bot.send_message(message.chat.id, strk['content'])
