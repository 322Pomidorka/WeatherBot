import asyncio
import requests
from aiogram import Bot, types, Dispatcher
from aiogram.filters.command import Command
from config import tg_bot_token, open_weather_token

bot = Bot(token=tg_bot_token)
dp = Dispatcher()

@dp.message(Command('start'))
async def start_command(message: types.Message):
    await message.answer("Введите название города, чтобы узнать погоду")

@dp.message()
async def get_weather(message: types.Message):
    try:
        res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric")
        data = res.json()

        city = data["name"]
        temperature = data["main"]["temp"]
        wind = data["wind"]["speed"]

        await message.answer(f"Погода в {city}: \nТемпература: {temperature}\nВетер: {wind} м\с")
    except:
       await message.answer("Неверно введён город!")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())