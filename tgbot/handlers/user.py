from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from tgbot.misc.states import ExamState


async def user_start(message: Message):
    await message.reply("Hello, user!")


async def user_form(message: Message):
    await message.answer("Привет. Как твоё имя?")
    await ExamState.first()


async def get_user_email(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data["name"] = message.text
    await message.answer("Какая у тебя почта?")
    await ExamState.next()


async def get_user_phone(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data["email"] = message.text
    await message.answer("Укажи свой телефон")
    await ExamState.next()


async def print_user_data(message: Message, state: FSMContext):
    data = await state.get_data()

    text = [
        "Привет! Ты ввел следующие данные:",
        "",
        f'Имя - {data.get("name")}',
        "",
        f'Email - {data.get("email")}',
        "",
        f"Телефон: - {message.text}",
    ]
    await message.answer("\n".join(text))
    await state.finish()


async def get_photo_id(m: Message):
    await m.reply(f"Photo {m.photo[-1].file_id}")


def register_user(dp: Dispatcher):
    # dp.register_message_handler(user_start, commands=["start"], state="*")
    dp.register_message_handler(user_form, commands=["form"], state="*")
    dp.register_message_handler(get_user_email, state=ExamState.NAME)
    dp.register_message_handler(get_user_phone, state=ExamState.EMAIL)
    dp.register_message_handler(print_user_data, state=ExamState.PHONE)
    dp.register_message_handler(get_photo_id, content_types=types.ContentType.PHOTO)
