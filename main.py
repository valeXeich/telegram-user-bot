import os
import asyncio

from pyrogram import Client
from pyrogram.errors import RPCError
from dotenv import load_dotenv

from utils.tasks import send_message
from utils.db import init_models

load_dotenv()

API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
BOT_NAME = os.getenv('BOT_NAME')

app = Client(BOT_NAME, API_ID, API_HASH) # Логин

async def main():
    async with app:
        await init_models() # Создание таблиц
        while True:
            try:
                await send_message(app) # Рассылка по базе
                await asyncio.sleep(60) # Делать рассылку каждую минуту
            except RPCError:
                break

        
if __name__ == "__main__":
    asyncio.run(main())