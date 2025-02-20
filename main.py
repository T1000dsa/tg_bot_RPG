# venv/Scripts/activate | deactivate; venv -> 1 | 0
# pip install -U aiogram; -U when venv: 1 | -U if venv == True
# git add <file> | git add .
# git commit -m "disciption"
# git push origin main
# python3 -m venv venv
# venv/Scripts/activate.bat
# . venv/bin/activate
# virtualenv .env
# git ls-files | xargs wc -l

# DOTO separate users data
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config_data.config import Config, load_config
from handlers_data import other_handlers, user_handlers
from config_data import commands_menu
from aiogram.fsm.strategy import FSMStrategy
from middlewares_data.middlewares import SomeMiddleware
from aiogram.fsm.storage.memory import MemoryStorage

# Инициализируем логгер
logger = logging.getLogger(__name__)

# Функция конфигурирования и запуска бота
async def main():
    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')
    storage = MemoryStorage()

    # Загружаем конфиг в переменную config
    config: Config = load_config()

    # Инициализируем бот и диспетчер
    bot = Bot(
        token=config.tg_bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher(sfsm_strategy=FSMStrategy.CHAT, storage=storage)

    # Настраиваем главное меню бота
    await commands_menu.set_main_menu(bot)

    # Регистрируем роутеры в диспетчере
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    #dp.update.outer_middleware(SomeMiddleware())

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())