import logging
from asyncio import sleep

import dp as dp
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery, ContentType, ReplyKeyboardRemove
from aiogram.utils.markdown import hcode
from asgiref.sync import sync_to_async

from apps.product.models import Item, Category
from tgbot.keyboards.admin_panel import kbd_admin_panel, kbd_admin_apply_panel
from tgbot.keyboards.factory.ft_admin_panel import item_panel
from tgbot.misc.items import AddNewItem


async def start_admin_panel(message: Message):
    await message.answer(
        "Добро пожаловать в панель администратора", reply_markup=kbd_admin_panel
    )


async def start_not_admin_panel(message: Message):
    answer = await message.answer("Вы не администратор")
    await sleep(5)
    await message.delete()
    await answer.delete()


async def get_my_id(call: CallbackQuery):
    await call.message.answer(f"Ваш ID: {hcode(call.from_user.id)}")


async def add_new_item(call: CallbackQuery):
    await call.message.answer("Привет. Что бы добавить товар введи его название")
    await AddNewItem.first()


async def get_item_photo(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data["name"] = message.text
    await AddNewItem.next()
    await message.answer("Пришли фото товара")


async def get_item_price(message: Message, state: FSMContext):
    item_photo = message.photo[-1].file_id
    async with state.proxy() as data:
        data["photo"] = item_photo
    await AddNewItem.next()
    await message.answer("Введи цену товара")


async def get_item_description(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data["price"] = message.text
    await AddNewItem.next()
    await message.answer("Введи описание товара")


async def get_item_finish(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data["description"] = message.text
    data = await state.get_data()
    await AddNewItem.last()
    await message.answer(
        f"{hcode('Вы указали следующие данные:')}\n"
        f"Название: {data.get('name')}\n"
        f"ID фото: {data.get('photo')}\n"
        f"Цена: {data.get('price')}\n"
        f"Описание: {data.get('description')}",
        reply_markup=kbd_admin_apply_panel,
    )


async def save_or_publish_item(message: Message, state: FSMContext):
    data = await state.get_data()
    is_published = False
    if message.text == "Опубликовать товар":
        is_published = True
    category = await sync_to_async(Category.objects.get)(pk=1)
    item = await sync_to_async(Item.objects.update_or_create)(
        name=data.get("name"),
        photo=data.get("photo"),
        price=data.get("price"),
        description=data.get("description"),
        category=category,
        is_published=is_published,
    )
    if item:
        await message.answer("Товар добавлен", reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer(
            "Ошибка при добавлении", reply_markup=ReplyKeyboardRemove()
        )
    logging.info(f"Добавлен новый товар {item}")
    await state.finish()


async def get_all_published_items(message: Message):
    items = await sync_to_async(list)(
        Item.objects.filter(is_published=True).only("name", "price")
    )
    for i in items:
        print(i.price)
    return await message.answer("OK")


def register_admin_panels(dp: Dispatcher):
    dp.register_message_handler(get_all_published_items, commands="items")
    dp.register_message_handler(start_not_admin_panel, commands=["panel"], state="*")

    # Добавление нового товара
    dp.register_callback_query_handler(
        add_new_item, item_panel.filter(item_name="new_item")
    )
    dp.register_message_handler(get_item_photo, state=AddNewItem.NAME)
    dp.register_message_handler(
        get_item_price, state=AddNewItem.PHOTO, content_types=ContentType.PHOTO
    )
    dp.register_message_handler(get_item_description, state=AddNewItem.PRICE)
    dp.register_message_handler(get_item_finish, state=AddNewItem.DESCRIPTION)
    dp.register_message_handler(
        save_or_publish_item, text=["Сохранить товар"], state=AddNewItem.SAVE
    )
    dp.register_message_handler(
        save_or_publish_item, text=["Опубликовать товар"], state=AddNewItem.SAVE
    )

    # Получение ID
    dp.register_callback_query_handler(
        get_my_id, item_panel.filter(item_name="get_my_id")
    )
