from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from tgbot.keyboards.factory.start_admin import start_admin

krb_start_admin = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🎛️ Панель администратора", callback_data=start_admin.new("panel")
            ),
            InlineKeyboardButton(
                text="📫 Письмо разработчикам", callback_data="admin_menu:letter"
            ),
        ]
    ],
)
