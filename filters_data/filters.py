import logging
from config_data.config import Config, load_config
from aiogram.filters import BaseFilter
from aiogram.types import TelegramObject
from aiogram.types import Message

logger = logging.getLogger(__name__)

config: Config = load_config()

class IsAdmin(BaseFilter):
    def __init__(self) -> None:
        self.admin_ids = config.tg_bot.admin_ids

    async def __call__(self, message: Message) -> bool:
        if message.from_user.id in self.admin_ids:
            logger.info("someone from admin's has took the data from database")
            return True
        else:
            logger.info("someone tried to took data from database")
            return False
