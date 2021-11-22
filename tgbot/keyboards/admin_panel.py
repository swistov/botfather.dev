from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton,
)

from tgbot.keyboards.factory.ft_admin_panel import item_panel

kbd_admin_panel = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Добавить товар", callback_data=item_panel.new("new_item")
            ),
            InlineKeyboardButton(
                text="Информация о товаре", callback_data="item:item_info"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Получить ID фотографии", callback_data="item:get_photo_id"
            ),
            InlineKeyboardButton(
                text="Получить свой ID", callback_data="item:get_my_id"
            ),
        ],
    ],
)

kbd_admin_apply_panel = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Сохранить товар"),
            KeyboardButton(text="Опубликовать товар"),
        ],
    ],
    resize_keyboard=True,
)
