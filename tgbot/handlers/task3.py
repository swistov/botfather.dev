import logging

from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery

from tgbot.keyboards.factory.task3_data import task3_data
from tgbot.keyboards.task3 import task3_keyboard


async def inline_buttons_1(message: Message):
    text = ["Edit @Sberleadbot info.",
            "Name: Бот для Заданий на Курсе Udemy",
            "Description: ?",
            "About: ?",
            "Botpic: ? no botpic",
            "Commands: no commands yet"]
    await message.answer('\n'.join(text), reply_markup=task3_keyboard)


async def get_edit_name(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"{call.data=}")
    logging.info(f"DICT {callback_data=}")
    await call.message.answer("Ёпта")


def register_task3(dp: Dispatcher):
    dp.register_message_handler(inline_buttons_1, commands=["inline_buttons_1"])
    dp.register_callback_query_handler(get_edit_name, task3_data.filter(item_name="edit_name"))
