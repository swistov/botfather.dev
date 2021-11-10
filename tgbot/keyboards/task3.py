from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from tgbot.keyboards.factory.task3_data import task3_data

task3_keyboard = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Edit Name", callback_data=task3_data.new(item_name="edit_name")
            ),
            InlineKeyboardButton(
                text="Edit Description", callback_data="task:edit_description"
            ),
        ],
        [
            InlineKeyboardButton(text="Edit About", callback_data="task:edit_about"),
            InlineKeyboardButton(text="Edit Botpic", callback_data="task:edit_botpic"),
        ],
        [
            InlineKeyboardButton(
                text="Edit Commands", callback_data="task:edit_commands"
            ),
            InlineKeyboardButton(
                text="<<Back to Bot", callback_data="task:edit_back_to_bot"
            ),
        ],
    ],
)
