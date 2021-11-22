import asyncio
import logging
from aiogram.types import BotCommand

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from django.core.management import BaseCommand

from tgbot.config import load_config
from tgbot.filters.admin import AdminFilter
from tgbot.handlers.admin import register_admin
from tgbot.handlers.admin_panel import register_admin_panels
from tgbot.handlers.start import register_start_panel
from tgbot.handlers.users.inline import register_user_inline
from tgbot.middlewares.db import DbMiddleware


class Command(BaseCommand):
    def handle(self, *args, **options):
        logger = logging.getLogger(__name__)

        def register_all_middlewares(dp):
            dp.setup_middleware(DbMiddleware())

        def register_all_filters(dp):
            dp.filters_factory.bind(AdminFilter)

        def register_all_handlers(dp):
            register_user_inline(dp)
            register_admin(dp)
            register_admin_panels(dp)
            register_start_panel(dp)

        # Регистрация команд, отображаемых в интерфейсе Telegram
        async def set_commands(bot: Bot):
            commands = [
                BotCommand(command="/start", description="Начать общение"),
                BotCommand(command="/help", description="Помощь"),
            ]
            await bot.set_my_commands(commands)

        async def main():
            logging.basicConfig(
                level=logging.INFO,
                format=u"%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s",
            )
            logger.info("Starting bot")

            config = load_config(".env")
            storage = RedisStorage2() if config.tg_bot.use_redis else MemoryStorage()

            bot = Bot(token=config.tg_bot.token, parse_mode="HTML")
            dp = Dispatcher(bot, storage=storage)

            bot["config"] = config
            await set_commands(bot)

            register_all_middlewares(dp)
            register_all_filters(dp)
            register_all_handlers(dp)

            try:
                await dp.start_polling()
            finally:
                await dp.storage.close()
                await dp.storage.wait_closed()

        try:
            asyncio.run(main())
        except (KeyboardInterrupt, SystemExit):
            logger.error("Bot stopped!")
