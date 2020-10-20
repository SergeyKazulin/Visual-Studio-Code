from time import timezone
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils.config import get_config_from
from pyowm.utils import timestamps



config_dict = config.get_default_config_for_subscription_type('professional')
owm = OWM('e18d14ff3baa928f5fba8208972bce80', config_dict)
owm.supported_languages
config_dict['language'] = 'ru'
mgr = owm.weather_manager()
#place = input("Ваше местоположение(city, country): ")

observation = mgr.weather_at_place('Vitebsk, BY')

reg = owm.city_id_registry()
list_of_locations = reg.locations_for('Vitebsk', country='BY')
vitebsk = list_of_locations[0]  
lat = vitebsk.lat
lon = vitebsk.lon

#daily_forecast = mgr.forecast_at_place('Vitebsk,BY', 'daily').forecast

w = observation.weather

print(f'Витебск. Долгота: {lat} Широта: {lon}')
#print(w.temperature('celsius'), w.detailed_status, w.wind(), w.rain, w.clouds, w.humidity, w. heat_index)
print('Сейчас: ' + str(w.detailed_status))
print('Температура: ' + str(w.temperature('celsius')))
#print('Ощущается: ' + str(w. heat_index))
print('Ветер:' + str(w.wind()))
print('Дождь: ' + str(w.rain))
print('Снег: ' + str(w.snow))
print('Облачность: ' + str(w.clouds))
print('Влажность: ' + str(w.humidity))
print('Атмосферное давление: ' + str(w.pressure))
print('Восход солнца: ' + str(w.sunrise_time(timeformat='iso')))
print('Закат солнца: ' + str(w.sunset_time(timeformat='iso')))
#print()
#print(f'Прогноз: {daily_forecast}')
       