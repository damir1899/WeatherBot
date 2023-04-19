import requests
from datetime import datetime
from os import getenv, system
from dotenv import load_dotenv
import emoji
load_dotenv()


# d5bb44d0fa8e39e2339c9019d833d826
WEATHER_API = getenv('WEATHER_API')

def WeatherService(get_city, API=WEATHER_API):
    """
    Бот-метеоролог мгновенно показывает погоду в любом городе, предоставляя актуальную информацию о температуре воздуха, влажности и вероятности дождя. 
    Это помогает планировать дела эффективнее и быть в курсе погодных событий в режиме реального времени.
    
    get_city = 'Almaty'
    API = WEATHER_API

    WeatherService(get_city: str, API: StrApiKey) -> str
    """

    url = f'https://api.openweathermap.org/data/2.5/weather?q={get_city}&appid={API}&units=metric'

    response = requests.get(url)
    data = response.json()
    
    try:

        Pr_Day = datetime.fromtimestamp(data['sys']['sunset']) - datetime.fromtimestamp(data['sys']['sunrise'])
        
        Informations = f"""Погода - Damir
        {emoji.emojize(':world_map:')}Страна: {data["sys"]['country']}
        {emoji.emojize(':cityscape:')}Город: {data['name']} - {data['weather'][0]['description']} {data['clouds']['all']}%
        {emoji.emojize(':desert:')} Температура: {data['main']['temp']}°C
        {emoji.emojize(':hot_springs:')}Ощущается: {data['main']['feels_like']}°C
        {emoji.emojize(':droplet:')}Влажность: {data['main']['humidity']}%
        {emoji.emojize(':wind_face:')}Давление воздуха: {data['main']['pressure']} гПа
        {emoji.emojize(':leaf_fluttering_in_wind:')}Скорость ветра: {data['wind']['speed']} м/с
        {emoji.emojize(':triangular_flag:')}Направление ветра: {data['wind']['deg']}°
        {emoji.emojize(':sunrise_over_mountains:')}Восход солнца: {datetime.fromtimestamp(data['sys']['sunrise'])}
        {emoji.emojize(':sun:')}Продолжительность дня: {Pr_Day}
        {emoji.emojize(':sunset:')}Заход солнца: {datetime.fromtimestamp(data['sys']['sunset'])}
        """
        system("clear")
        return Informations
    except:
        return 'Нет такого города'
