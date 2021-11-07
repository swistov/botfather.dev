import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from sqlmodel import Session, SQLModel, create_engine, select

from tgbot.config import load_config
from tgbot.filters.admin import AdminFilter
from tgbot.handlers.admin import register_admin
from tgbot.handlers.items import register_items_task3
from tgbot.handlers.task3 import register_task3
from tgbot.handlers.user import register_user
from tgbot.middlewares.db import DbMiddleware
from tgbot.models.products import Product, User

logger = logging.getLogger(__name__)


def register_all_middlewares(dp):
    dp.setup_middleware(DbMiddleware())


def register_all_filters(dp):
    dp.filters_factory.bind(AdminFilter)


def register_all_handlers(dp):
    register_admin(dp)
    register_user(dp)
    register_task3(dp)
    register_items_task3(dp)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")
    config = load_config(".env")

    storage = RedisStorage2() if config.tg_bot.use_redis else MemoryStorage()
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher(bot, storage=storage)

    bot['config'] = config

    register_all_middlewares(dp)
    register_all_filters(dp)
    register_all_handlers(dp)

    # DB
    sqlite_file_name = "database.db"
    sqlite_url = f"sqlite:///{sqlite_file_name}"
    engine = create_engine(sqlite_url, echo=True)
    SQLModel.metadata.create_all(engine)

    def create_user():
        user = User(name="Test")
        with Session(engine) as s:
            s.add(user)
            s.commit()

    def create_heroes():
        hero_1 = Product(name="Deadpond", secret_name="Dive Wilson", user_id=1)
        hero_2 = Product(name="Spider-Boy", secret_name="Pedro Parqueador", user_id=1)
        hero_3 = Product(name="Rusty-Man", secret_name="Tommy Sharp", age=48, user_id=1)
        with Session(engine) as session:
            session.add(hero_1)
            session.add(hero_2)
            session.add(hero_3)

            session.commit()

    create_user()
    create_heroes()

    def select_heroes():
        with Session(engine) as session:
            statement = select(Product).where(Product.name == "Deadpond")
            results = session.exec(statement)
            for hero in results:
                logging.info(f"HERO: {hero}")

    select_heroes()
    # start
    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()
        with Session(engine) as session:
            session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
