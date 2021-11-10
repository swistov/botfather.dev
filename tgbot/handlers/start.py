from aiogram import Dispatcher
from aiogram.types import Message


async def first_start_message(message: Message):
    await message.answer(
        "Привет 🙌. Я SeNaBot 😊 \n"
        "Я помогаю моим владельцам пока они готовят новинки для тебя.\n"
        "Могу помочь тебе подобрать и купить новые вещи 🛒 "
        ", а так же расскажу когда появятся новые 👗 👟 🧥 👕 👔\n"
        "Но я ничего не знаю о тебе. Расскажешь?"
    )


def register_start_panel(dp: Dispatcher):
    dp.register_message_handler(first_start_message, commands="start")
