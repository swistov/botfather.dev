from aiogram import Dispatcher
from aiogram import types
from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from aiogram.dispatcher.filters import CommandStart

from tgbot.config import allowed_users


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
    user = query.from_user.id
    if user not in allowed_users:
        await query.answer(
            results=[],
            switch_pm_text="Бот недоступен. Подключить бота",
            switch_pm_parameter="connect_user",
            cache_time=5,
        )
        return

    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id="1",
                title="Название которое отображается в инлайн режиме",
                input_message_content=types.InputTextMessageContent(
                    message_text="Тут какой-то текст, который будет отправлен при нажатии"
                ),
                url="https://core.teleram.com/bots/api#inlinequeryresult",
                thumb_url="https://www.barcelona-tourist-guide.com/images/int/attractions/beaches/L550/barcelona-beach-9086.jpg",
                description="Описание, в инлайн режиме",
            ),
            types.InlineQueryResultVideo(
                id="4",
                video_url="https://youtu.be/eHCrFVWZl1E",
                caption="Подпись к видео",
                title="Какие-то видео",
                description="Какое-то описание",
                thumb_url="https://n1s1.hsmedia.ru/d5/57/a3/d557a36dc6928e2472751e67185d8104/728x542_1_7eac6bb60077470db369251729188c08@1000x745_0xac120003_19217115901587132885.jpg",
                mime_type="video/mp4",
            ),
        ]
    )


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
