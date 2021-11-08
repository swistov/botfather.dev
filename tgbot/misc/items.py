from aiogram.dispatcher.filters.state import StatesGroup, State


class AddNewItem(StatesGroup):
    NAME = State()
    PHOTO = State()
    PRICE = State()
    DESCRIPTION = State()
