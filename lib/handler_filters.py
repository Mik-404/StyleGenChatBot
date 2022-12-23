from lib.utils import *
from lib import logs
import settings


class FilterBot(BoundFilter):
    async def check(self, message: types.Message):
        try:
            if message.reply_to_message and '@' + settings.BOT_NAME in message.text:
                return True
        except Exception as e:
            await logs.BotLogReplicas(message).filter_reply_crashed(e)


class CommandFilter(BoundFilter):
    async def check(self, message: types.Message):
        try:
            if message.entities:
                for feature in message.entities:
                    if feature.type == "mention" and not '@' + settings.BOT_NAME in message.text:
                        return False
                return True
            return True
        except Exception as e:
            await logs.BotLogReplicas(message).filter_reply_crashed(e)


class FilterOtherCommands(BoundFilter):
    async def check(self, message: types.Message):
        try:
            if message.entities:
                for feature in message.entities:
                    if feature.type == "bot_command":
                        return False
            return True
        except Exception as e:
            await logs.BotLogReplicas(message).filter_command_crashed_message(e)
