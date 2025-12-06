import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

BOT_TOKEN = "8524038504:AAFwLug-98RMALtoqHd04CrojBIVlbV7Ql4"  

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Жду от тебя команды или используй /help для списка команд")

@dp.message(Command("hi"))
async def cmd_hi(message: types.Message):
    await message.answer("Привет! Бро ")

@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    help_text = """
    Доступные команды:
    /start - Начать работу
    /hi - Поприветствовать
    /help - Справка
    /random - Случайное число
    /about - О боте
        """
    await message.answer(help_text)

@dp.message(Command("about"))
async def cmd_about(message: types.Message):
    await message.answer("Мой первый Telegram-бот с помощью aiogram 3.x")


@dp.message(Command("random"))
async def cmd_random(message: types.Message):
    number = random.randint(1, 100)
    await message.answer(f"Случайное число: {number}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

    