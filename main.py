import logging
import random
from os import getenv, system
from datetime import datetime
import asyncio

# Downloaded
from aiogram import Bot
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.types import *
from core.weather import WeatherService

TOKEN = getenv('TOKEN')
ADMIN = getenv('ADMIN')

system('clear')
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)

Menu = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Kazakhstan'),
    KeyboardButton('Kyrgyzstan'),
    KeyboardButton('Uzbekistan'),
    
)

city_kz = ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton('Алматы'),
        KeyboardButton('Астана'),
        KeyboardButton('Атырау'),
        KeyboardButton('Актау'),
        KeyboardButton('Орал'),
        KeyboardButton('Усть-Каменогорск'),
        KeyboardButton('Павлодар'),
        KeyboardButton('Талдыкорган'),
        KeyboardButton('Жетысай'),
        KeyboardButton('Кокшетау'),
        KeyboardButton('Жезказган'),
        KeyboardButton('Караганда'),
        KeyboardButton('Семей'),
        KeyboardButton('Коктума'),
        KeyboardButton('Menu')
    )

city_kg = ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton('Алматы'),
        KeyboardButton('Астана'),
        KeyboardButton('Атырау'),
        KeyboardButton('Актау'),
        KeyboardButton('Орал'),
        KeyboardButton('Усть-Каменогорск'),
        KeyboardButton('Павлодар'),
        KeyboardButton('Талдыкорган'),
        KeyboardButton('Жетысай'),
        KeyboardButton('Кокшетау'),
        KeyboardButton('Жезказган'),
        KeyboardButton('Караганда'),
        KeyboardButton('Семей'),
        KeyboardButton('Коктума'),
        KeyboardButton('Menu')
    )

city_uz = ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton('Алматы'),
        KeyboardButton('Астана'),
        KeyboardButton('Атырау'),
        KeyboardButton('Актау'),
        KeyboardButton('Орал'),
        KeyboardButton('Усть-Каменогорск'),
        KeyboardButton('Павлодар'),
        KeyboardButton('Талдыкорган'),
        KeyboardButton('Жетысай'),
        KeyboardButton('Кокшетау'),
        KeyboardButton('Жезказган'),
        KeyboardButton('Караганда'),
        KeyboardButton('Семей'),
        KeyboardButton('Коктума'),
        KeyboardButton('Menu')
    )


@dp.message_handler(commands=['start'])
async def start(message: Message):
    
    text = '''Бот-метеоролог мгновенно показывает погоду в любом городе, предоставляя актуальную информацию о температуре воздуха, влажности и вероятности дождя. Это помогает планировать дела эффективнее и быть в курсе погодных событий в режиме реального времени.'''
    photo = open('core/image2.jpg', 'rb')
    await message.answer_photo(photo, text, reply_markup=Menu)
    

@dp.message_handler(content_types=ContentType.TEXT)
async def users_answer(message: Message):
    if message.text.lower() == 'menu':
        await message.answer('Выберите страну', reply_markup=Menu)
    elif message.text.lower() == 'kazakhstan':
        await message.answer('Выберите город', reply_markup=city_kz)
    elif message.text.lower() == 'kyrgyzstan':
        await message.answer('Выберите город', reply_markup=city_kg)
    elif message.text.lower() == 'uzbekistan':
        await message.answer('Выберите город', reply_markup=city_uz)
    else:
        photo = open('core/image.jpg', 'rb')
        text = WeatherService(message.text)
        await message.reply_photo(photo, text)
        
async def schedule_message(message: Message):
    send_time = datetime.time(hour=17, minute=43, second=50)
    while True:
        current_time = datetime.datetime.now().time()
        if current_time == send_time:
            photo = open('core/image.jpg', 'rb')
            text = WeatherService(get_city='Almaty')
            await message.reply_photo(photo, text)
        else:
            await asyncio.sleep(10)

schedule_message()
    

if __name__=='__main__':
    try:
        executor.start_polling(dp)
    except(KeyboardInterrupt, SystemExit):
        pass


    