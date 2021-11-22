from aiogram.dispatcher.filters.state import StatesGroup, State


class ExamState(StatesGroup):
    NAME = State()
    EMAIL = State()
    PHONE = State()
