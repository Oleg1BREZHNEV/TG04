#Для создания бота с простым меню и кнопками "Привет" и "Пока"
# с использованием библиотеки `aiogram` версии 3.x, вам
# потребуется следующий код:

#1. Установите библиотеку `aiogram` версии 3.x:



import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import CommandStart


from pydantic import BaseModel
from pydantic_core import ValidationError


class KeyboardButton(BaseModel):
    text: str


class ReplyKeyboardMarkup(BaseModel):
    keyboard: list
    resize_keyboard: bool = True


try:
    # Создаем кнопки
    button1 = KeyboardButton(text="Button 1")
    button2 = KeyboardButton(text="Button 2")

    # Создаем клавиатуру
    keyboard = ReplyKeyboardMarkup(keyboard=[[button1.dict(), button2.dict()]], resize_keyboard=True)
    print(keyboard)
except ValidationError as e:
    print(e)

API_TOKEN = ''  # Замените на ваш токен

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

   # Создаем клавиатуру
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_hi = KeyboardButton(text="Привет")
button_bye = KeyboardButton(text="Пока")
keyboard.add(button_hi, button_bye)

@dp.message(CommandStart())
async def send_welcome(message: types.Message):
    await message.answer("Выберите действие:", reply_markup=keyboard)

@dp.message(lambda message: message.text == "Привет")
async def say_hello(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}!")

@dp.message(lambda message: message.text == "Пока")
async def say_goodbye(message: types.Message):
    await message.answer(f"До свидания, {message.from_user.first_name}!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


#В этом коде:
#- Мы создаем бота и диспетчера с использованием `aiogram`.
#- Создаем клавиатуру с кнопками "Привет" и "Пока".
#- Обрабатываем команду `/start`, которая отправляет пользователю
# клавиатуру с кнопками.
#- Обрабатываем нажатия на кнопки "Привет" и "Пока", отправляя
# соответствующие ответы с именем пользователя.

#Не забудьте заменить `YOUR_API_TOKEN_HERE` на токен вашего бота,
# который вы можете получить у @BotFather в Telegram.

