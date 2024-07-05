from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


main = ReplyKeyboardMarkup(keyboard=[
   [KeyboardButton(text="Hi"),
   KeyboardButton(text="Good bye")]],resize_keyboard=True)

#Создаём клавиатуру ,которая будет прикреплена к сообщению
inline_keyboard_test = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Видео", url='https://www.youtube.com/watch?v=Oy52AQOlomw')]

])
test = ["кнопка 1", "кнопка 2", "кнопка 3", "кнопка 4"]
inline_keyboard_test = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Каталог", callback_data='catalog')],
   [InlineKeyboardButton(text="Новости", callback_data='news')],
   [InlineKeyboardButton(text="Профиль", callback_data='person')]
])

async def test_keyboard():
   keyboard = InlineKeyboardBuilder()
   for key in test:
      keyboard.add(KeyboardButton(text=key))
   return keyboard.adjust(2).as_markup()
