from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery

from tgbot.keyboards.admin_panel import kbd_admin_panel
from tgbot.keyboards.factory.start_admin import start_admin
from tgbot.keyboards.start_admin import krb_start_admin


async def admin_start(message: Message):
    await message.reply(
        "👑 Привет, администратор!\nВыбери нужную команду: 📜\n\n",
        reply_markup=krb_start_admin,
    )


async def get_my_id(message: Message):
    await message.answer(message.from_user.id)


async def get_admin_panel(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(
        "Добро пожаловать в панель администратора", reply_markup=kbd_admin_panel
    )


async def letter_for_admin(call: CallbackQuery):
    await call.message.answer("Я пока не умею это делать")


def register_admin(dp: Dispatcher):
    dp.register_message_handler(
        admin_start, commands=["start"], state="*", is_admin=True
    )
    dp.register_message_handler(get_my_id, commands=["myid"], state="*", is_admin=True)
    dp.register_callback_query_handler(
        get_admin_panel, start_admin.filter(panel_item="panel")
    )
    dp.register_callback_query_handler(
        letter_for_admin, start_admin.filter(panel_item="letter")
    )
