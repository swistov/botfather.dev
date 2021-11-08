import logging
from asyncio import sleep

from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from tgbot.keyboards.admin_panel import kbd_admin_panel
from tgbot.keyboards.factory.ft_admin_panel import item_panel
from tgbot.misc.items import AddNewItem


async def start_admin_panel(message: Message):
    await message.answer(f"Добро пожаловать в панель администратора", reply_markup=kbd_admin_panel)


async def start_not_admin_panel(message: Message):
    answer = await message.answer("Вы не администратор")
    await sleep(5)
    await message.delete()
    await answer.delete()


async def add_new_item(call: CallbackQuery):
    await call.message.answer("Привет. Что бы добавить товар введи его название")
    await AddNewItem.first()


async def get_item_photo(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data["name"] = message.text
    await message.answer("Пришли фото товара")
    logging.info("1")
    await AddNewItem.next()
    logging.info("2")


async def get_item_price(message: Message, state: FSMContext):
    logging.info("3")
    item_photo = message.photo[-1].file_id
    async with state.proxy() as data:
        data["photo"] = item_photo
    await message.answer("Введи цену товара")
    await state.finish()


def register_admin_panels(dp: Dispatcher):
    dp.register_message_handler(start_admin_panel, commands=["panel"], is_admin=True)
    dp.register_message_handler(start_not_admin_panel, commands=["panel"])
    dp.register_callback_query_handler(add_new_item, item_panel.filter(item_name="new_item"))
    dp.register_message_handler(get_item_photo, state=AddNewItem.NAME)
    dp.register_message_handler(get_item_price, state=AddNewItem.PHOTO)
