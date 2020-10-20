# telegram_bot

from pyowm import OWM
from pyowm.utils import config
from pyowm.utils.config import get_config_from
from pyowm.utils import timestamps
import telebot


config_dict = config.get_default_config_for_subscription_type('professional')
owm = OWM('e18d14ff3baa928f5fba8208972bce80', config_dict)
owm.supported_languages
config_dict['language'] = 'ru'
mgr = owm.weather_manager()

bot = telebot.TeleBot("1317459860:AAEMWHhmoK-rKZDn_yyDQ-IOAJXm08OlNGM")
@bot.message_handler(content_types=['text'])

def send_echo(message):
    #bot.reply_to((message, message.text))
    #bot.send_message(message.chat.id, message.text)

    observation = mgr.weather_at_place(message.text)
    w = observation.weather

    #weather = 'Сейчас: ' + str(w.detailed_status) +'\n''Температура: ' + str(w.temperature('celsius')) +'\n''Ощущается: ' + str(w. heat_index) +'\n''Ветер: ' + str(w.wind())+'\n''Дождь: ' + str(w.rain)+'\n''Снег: ' + str(w.snow)+'\n''Облачность: ' + str(w.clouds)+'\n''Влажность: ' + str(w.humidity)+'\n''Атмосферное давление: ' + str(w.pressure)
    #answer = weather
    
    
    answer = 'Сейчас: ' + str(w.detailed_status)+'\n'
    answer += 'Температура: ' + str(w.temperature('celsius'))+'\n'
    answer += 'Ощущается: ' + str(w. heat_index)+'\n'
    answer += 'Ветер:' + str(w.wind())+'\n'
    answer += 'Дождь: ' + str(w.rain)+'\n'
    answer += 'Снег: ' + str(w.snow)+'\n'
    answer += 'Облачность: ' + str(w.clouds)+'\n'
    answer += 'Влажность: ' + str(w.humidity)+'\n'
    answer += 'Атмосферное давление: ' + str(w.pressure)+'\n'
    answer = 'Восход солнца: ' + str(w.sunrise_time(timeformat='iso'))
    answer = 'Закат солнца: ' + str(w.sunset_time(timeformat='iso'))
    bot.send_message(message.chat.id, answer)

bot.polling(none_stop=True)
import calendar
