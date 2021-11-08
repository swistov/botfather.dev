from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from tgbot.keyboards.factory.ft_admin_panel import item_panel

kbd_admin_panel = InlineKeyboardMarkup(row_width=2,
                                       inline_keyboard=[
                                           [
                                               InlineKeyboardButton(
                                                   text="Добавить товар",
                                                   callback_data=item_panel.new("new_item")
                                               ),
                                               InlineKeyboardButton(
                                                   text="Информация о товаре",
                                                   callback_data="item:item_info"
                                               )
                                           ],
                                       ])
