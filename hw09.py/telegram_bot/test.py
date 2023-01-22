from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import json
import telebot
import requests 
from geopy import geocoders
from os import environ
from pprint import pprint
import datetime
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token='5848608598:AAENncA4M6cdJ9v4dbr19zvY8BmLlmJxMPc')
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply(f'hello')

@dp.message_handler()
async def start_command(message: types.Message):
    def geo_pos_lon(city: str):
        geolocator = geocoders.Nominatim(user_agent="telebot")
        longitude = str(geolocator.geocode(city).longitude)
        return longitude
    def geo_pos_lat(city: str):
        geolocator = geocoders.Nominatim(user_agent="telebot")
        latitude = str(geolocator.geocode(city).latitude)
        return latitude


    def yandex_weather(latitude, longitude: str):

        url_yandex = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid=f01a1bfcbc7d67e70eae5d35cbd0d6ba'
        print(url_yandex)
        response = requests.get(url_yandex)
        data = json.loads(response.content)

        city = data['name']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
    
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset = datetime.datetime.fromtimestamp(data['sys']['sunset'])

        message = f'Weather in {city}\n Temperature: {temperature}\n Humidity: {humidity}\n Pressure: {pressure}\n Wind: {wind}\n Sunrise: {sunrise}\n Sunset: {sunset}'
        return(message)


    def main():
        city = message.text
        latitude = geo_pos_lat(city)
        # print(latitude)

        longitude = geo_pos_lon(city)
        # print(longitude)
        msg = yandex_weather(latitude, longitude)
        return (msg)
    weather = main()
    await message.reply(f'{weather}')

if __name__ == '__main__':
    executor.start_polling(dp)