
#import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command,CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
BOT_TOKEN = ''

# Настройка логирования
#logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command('start'))
async def send_welcome(message: types.Message):
    await message.reply("Привет! Отправь команду /links, чтобы получить ссылки на новости, музыку и видео.")

# Обработчик команды /links
@dp.message(Command('links'))
async def send_links(message: types.Message):
    # Создаем инлайн-кнопки с URL-ссылками
    keyboard = InlineKeyboardMarkup(row_width=1)
    buttons = [
        InlineKeyboardButton(text="Новости", url="https://www.bbc.com/news/world-60525350"),
        InlineKeyboardButton(text="Музыка", url="https://open.spotify.com/track/7GhIk7Il098yCjg4BQjzvb"),
        InlineKeyboardButton(text="Видео", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    ]
    keyboard.add(*buttons)

    await message.reply("Выберите одну из ссылок ниже:", reply_markup=keyboard)
async def main():
    await dp.start_polling(bot)
# Запуск бота
if __name__ == '__main__':
    asyncio.run(main())



