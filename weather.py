import requests
import datetime


class Get_Weather():
    def __init__(self, city):
        self.city = city

    def get_any_city(self, city, openweather_token):
        data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={openweather_token}'
                            f'&units=metric')
        data = data.json()
        get_city = data['name']
        cur_temp = int(data['main']['temp'])
        feels_like = int(data['main']['feels_like'])
        humidity = data['main']['humidity']
        pressure = int((data['main']['pressure']) / 1.33317)
        wind = data['wind']['speed']
        sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        return f'Город: {get_city}\nТемпература, °C: {cur_temp}\nОщущается, °C: {feels_like}' \
               f'\nВлажность, %: {humidity}\nДавление, мм рт ст: {pressure}\nВетер, м/с: {wind}\nРассвет:' \
               f' {sunrise} МСК\nЗакат: {sunset} МСК'