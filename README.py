
from aiogram import Bot, Dispatcher, executor,types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup,KeyboardButton
from aiogram.dispatcher.filters import Text
from button import kb

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton(text="Узнать о различных направлениях стажировки в Росатоме.")
b2 = KeyboardButton(text="Получить ответы на часто задаваемые вопросы от потенциальных стажеров.")
b3 = KeyboardButton(text="Подписаться на уведомления о новых открытых вакансиях для стажировки.")
b4 = KeyboardButton(text="Задать вопросы и получить консультации от HR-специалистов компании.")
b5 = KeyboardButton(text="Получить ссылки на ресурсы для подготовки к собеседованиям и тестированиям.")
kb.add(b1).add(b2).add(b3).add(b4).add(b5)

bot = Bot("7173143373:AAHoMvWfO0rofRQHaYcAo-28R4AzBbkQdLc")
dp = Dispatcher(bot)


async def on_startup(_):
    print("я быдл запущен")


dis = "Привет! Я бот Росатом Стажировка и я здесь, чтобы помочь тебе узнать все о стажировке в компании Росатом. Я предоставлю информацию о доступных стажировочных программах, требованиях к кандидатам, сроках проведения стажировки и многом другом."


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text=dis,
                           reply_markup=kb)

inf_ctag = ""





if __name__ == "__main__":
    executor.start_polling(dispatcher = dp, skip_updates=True, on_startup=on_startup)
