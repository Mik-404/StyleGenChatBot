from lib.utils import *
from lib import logs


class FilterBot(BoundFilter):
    async def check(self, message: types.Message):
        try:
            if message.is_forward() or message.reply_to_message:
                return True
        except Exception as e:
            logs.BotLogReplicas(message).filter_reply_crashed(e)


class FilterOtherCommands(BoundFilter):
    async def check(self, message: types.Message):
        try:
            if message.entities:
                for feature in message.entities:
                    if feature.type == "bot_command":
                        return False
            return True
        except Exception as e:
            logs.BotLogReplicas(message).filter_command_crashed_message(e)
