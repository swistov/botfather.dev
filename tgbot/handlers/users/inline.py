from typing import List

from aiogram import Dispatcher
from aiogram import types
from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from aiogram.dispatcher.filters import CommandStart

from apps.product.models import Item
from tgbot.config import allowed_users
from asgiref.sync import sync_to_async


@sync_to_async
def get_items() -> List[Item]:
    return Item.objects.filter(is_published=True)


async def empty_query(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id="unknown",
                title="Введите какой-то запрос",
                input_message_content=types.InputTextMessageContent(
                    message_text="Не обязательно жать при этом кнопку"
                ),
            )
        ],
        cache_time=5,
    )


async def some_query(query: types.InlineQuery):
    print(query.query.title())

    items = get_items
    # for i in items.:
    #     print(i)
    print(dir(items))


async def connect_user(message: types.Message):
    allowed_users.append(message.from_user.id)
    await message.answer(
        "Вы подключены.",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="Войти в инлайн режим",
                        switch_inline_query_current_chat="Капрос",
                    )
                ]
            ]
        ),
    )


def register_user_inline(dp: Dispatcher):
    dp.register_inline_handler(empty_query, text="")
    dp.register_inline_handler(some_query)
    dp.register_message_handler(connect_user, CommandStart(deep_link="connect_user"))
