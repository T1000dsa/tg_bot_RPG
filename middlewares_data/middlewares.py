import logging
from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

logger = logging.getLogger(__name__)


class SomeMiddleware(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:

        logger.debug('Вошли в миддлварь SomeMiddleware')

        data = event.model_dump()
        print(data['message']['chat']['id'])

        result = await handler(event, data)

        logger.debug('Выходим из миддлвари SomeMiddleware')

        return result