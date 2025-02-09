from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User



class Parel(BaseMiddleware):
    def __init__(self,user_new:int=None):
        self.user_new = user_new

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        
        user: User = data.get('event_from_user')
        print(user.id, self.user_new)
        if user is not None:
            if user.id == self.user_new:
                return await handler(event, data)
            elif user.id != self.user_new:
                return 

        return handler(event, data)