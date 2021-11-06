from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.emoji import emojize

from tgbot.keyboards.factory.items import items_data, item_buy

items_keyboard = InlineKeyboardMarkup(row_width=2,
                                      inline_keyboard=[
                                          [
                                              InlineKeyboardButton(
                                                  text="Купить товар",
                                                  callback_data=item_buy.new(item_id=1)
                                              ),
                                          ],
                                          [
                                              InlineKeyboardButton(
                                                  text=emojize("👍"),
                                                  callback_data=items_data.new(item_name="like")
                                              ),
                                              InlineKeyboardButton(
                                                  text="👎",
                                                  callback_data="items_data:dislike"
                                              )
                                          ],
                                          [
                                              InlineKeyboardButton(
                                                  text="Поделиться с другом",
                                                  query="https://t.me/senabotmanage",
                                                  switch_inline_query="1"
                                              )
                                          ]
                                      ])
