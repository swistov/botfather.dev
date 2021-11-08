import logging
from asyncio import sleep

from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery

from tgbot.keyboards.admin_panel import kbd_admin_panel
from tgbot.keyboards.factory.ft_admin_panel import item_panel


async def start_admin_panel(message: Message):
    await message.answer(f"Добро пожаловать в панель администратора", reply_markup=kbd_admin_panel)


async def start_not_admin_panel(message: Message):
    answer = await message.answer("Вы не администратор")
    await sleep(5)
    await message.delete()
    await answer.delete()


async def add_new_item(call: CallbackQuery, callback_data: dict):
    logging.info(call)
    logging.info(callback_data)


def register_admin_panels(dp: Dispatcher):
    dp.register_message_handler(start_admin_panel, commands=["panel"], is_admin=True)
    dp.register_message_handler(start_not_admin_panel, commands=["panel"])
    dp.register_callback_query_handler(add_new_item, item_panel.filter(item_name="new_item"))
