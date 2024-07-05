import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery
import random
from gtts import gTTS
import os

import keyboardsht21 as kb

API_TOKEN = ''  # Замените на ваш токен

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
   await message.answer(f'Приветики, {message.from_user.first_name}', reply_markup=kb.main)
@dp.message(F.text == "Hi")
async def test_button(message: Message):
   await message.answer(f'Привет, {message.from_user.first_name}',reply_markup=kb.main )

@dp.message(F.text == "Good bye")
async def test_button(message: Message):
   await message.answer(f'До свидания, {message.from_user.first_name}',reply_markup=kb.main )
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())