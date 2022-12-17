from lib.utils import *
from lib import logs


class FilterBot(BoundFilter):
    async def check(self, message: types.Message):
        try:
            if message.is_forward() or message.reply_to_message:
                return True
        except Exception as e:
            logs.log_(f"--Message was crashed: {message.text[0: min(len(message.text), 100)]} in reply checking...")
            logs.log_(f"   {e}")