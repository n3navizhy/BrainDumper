import asyncio
import os
import aiohttp
from dotenv import load_dotenv
from  aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from ollama_service import get_ollama_response
from aiogram.client.session.aiohttp import AiohttpSession
load_dotenv()
TOKEN = os.getenv('TOKEN')
PROXY_URL = os.getenv('PROXY_URL')

async def main():

    session = AiohttpSession(  proxy=PROXY_URL,  # Вот так нужно передавать прокси
        timeout=60
    )

    bot = Bot(token=TOKEN, session=session)
    dp = Dispatcher()

    @dp.message(Command("start"))
    async def process_start_command(message: types.Message):
        await message.reply("Привет! Напиши мне что-нибудь!")

    @dp.message(F.text)  # Обработчик любого текста
    async def echo_message(message: types.Message):
        await message.reply("🤖 Думаю...")
        response = await asyncio.to_thread(get_ollama_response, message.text)
        await message.reply(response)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
