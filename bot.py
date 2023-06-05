import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config_data.config import load_config, Config, set_main_menu
from handlers import other_handlers, user_handlers


logger = logging.getLogger(__name__)


async def main() -> None:

    logging.basicConfig(level=logging.INFO,
                        format='%(filename)s:%(lineno)d #%(levelname)-8s '
                                '[%(asctime)s] - %(name)s - %(message)s',)
                        # filename=u'botlog.log') 
    
    logger.info('Starting bot')

    config: Config = load_config('../.env')

    storage: MemoryStorage = MemoryStorage()

    bot: Bot = Bot(token=config.tg_bot.token,
                    parse_mode='HTML')
    dp: Dispatcher = Dispatcher(storage=storage)

    await set_main_menu(bot)

    admin_ids: list[int] = config.tg_bot.admin_ids

    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
