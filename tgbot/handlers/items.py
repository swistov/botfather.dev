from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery, InputMedia
from asgiref.sync import sync_to_async

from apps.account.models import User, Referral
from tgbot.keyboards.factory.items import items_data, item_buy
from tgbot.keyboards.items import items_keyboard


async def start_items(m: Message):
    await m.answer_photo("AgACAgIAAxkBAAIBJ2GARfHoAsNa9YjUlWzvUZVuEd8rAAKBtjEbHXgAAUg3gs3S5QUnlQEAAwIAA3gAAyEE",
                         caption="Мандарин", reply_markup=items_keyboard)

    results = await sync_to_async(User.objects.create)(user_id=3, name="Nick", username="sw")
    await m.answer(results)


async def like_dislike(call: CallbackQuery):
    answer = {"like": "понравился", "dislike": "не понравился"}
    text = f"Тебе {answer[call.data.split(':')[1]]} этот товар"
    await call.answer(text=text, show_alert=False)


async def buy_item(call: CallbackQuery, callback_data: dict):
    item_id = callback_data.get("item_id")
    photo = call.message.photo[-1].file_id
    file = InputMedia(media=photo, caption=f"Покупай товар номер {item_id}")
    await call.message.edit_media(file)


def register_items_task3(dp: Dispatcher):
    dp.register_message_handler(start_items, commands=["items"])
    dp.register_callback_query_handler(like_dislike, items_data.filter(item_name=["dislike", "like"]))
    dp.register_callback_query_handler(buy_item, item_buy.filter(item_id="1"))
