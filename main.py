import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from ollama_service import get_ollama_response
load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def process_start_command(message: types.Message):
    await message.reply("Привет! Напиши мне что-нибудь!")

@dp.message(F.text)  # Обработчик любого текста
async def echo_message(message: types.Message):
    await message.reply("🤖 Думаю...")
    response = get_ollama_response(message.text)
    await message.reply(response)
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
