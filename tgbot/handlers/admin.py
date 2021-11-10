from aiogram import Dispatcher
from aiogram.types import Message


async def admin_start(message: Message):
    await message.reply(
        "👑 Привет, администратор!\n"
        "Выбери нужную команду: 📜\n\n"
        f"🎛️ Панель администратора /panel\n"
        f"📫 Письмо разработчикам /letter"
    )


async def get_my_id(message: Message):
    await message.answer(message.from_user.id)


def register_admin(dp: Dispatcher):
    dp.register_message_handler(
        admin_start, commands=["start"], state="*", is_admin=True
    )
    dp.register_message_handler(get_my_id, commands=["myid"], state="*", is_admin=True)
