import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode

from config.config import TOKEN, maintenance_mode
from utils.set_bot_commands import set_commands
from handlers import help_handler, start_handler, new_members_handler, stop_handler, \
    language_filter, add_allowed_words, delete_allowed_words, maintenance, swear_words_control
from databases.database import create_db
from databases.words_storage import create_storage
# from server.background import keep_alive


logger = logging.getLogger(__name__)
bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage(), maintenance_mode=maintenance_mode)


async def main() -> None:
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    logger.info("Starting Bot...")

    await create_db()
    await create_storage()

    dp.include_routers(
        # maintenance.update_maintenance_router,
        maintenance.maintenance_router,
        start_handler.start_router,
        help_handler.help_router,
        new_members_handler.new_member_router,
        stop_handler.stop_router,
        add_allowed_words.add_allowed_words_router,
        delete_allowed_words.delete_allowed_words_router,
        swear_words_control.swear_words_router,
        language_filter.lang_router, 
    )

    await set_commands(bot)

    # await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, handle_signals=False)


if __name__ == "__main__":
    try:
        # keep_alive()
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped!")
