from aiogram.dispatcher.filters import BoundFilter
from aiogram import Bot, types
import logs


class ReplyFilterBot(BoundFilter):
    async def check(self, message: types.Message):
        try:
            if message.is_forward() or message.reply_to_message:
                return True
        except Exception:
            logs.log_(f"--Message was crashed: {message.text[0: min(len(message.text), 100)]} in reply checking...")
            logs.log_(f"   {e}")