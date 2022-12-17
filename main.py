from lib import processing_of_message, logs, handler_filters
import settings
from lib.utils import *

bot = Bot(token=settings.TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(handler_filters.FilterBot())
async def style_gen(message: types.Message):
    logging = logs.botLogReplicas(message)
    logging.start_processing()
    try:
        if '@' + settings.BOT_NAME in message.text and len(message.text.split()) == 2 and int(message.text.split()[1]) in settings.features:
            answer_gen = processing_of_message.ProcessingOfMessage(message.reply_to_message.text, message.text.split()[1])
            await message.answer(answer_gen.answer_text())
            logging.success_finish()
        else:
            logging.wrong_request_from_user()
    except Exception as e:
        logging.error(e)


def start_bot():
    logs.startlogging()
    executor.start_polling(dp, skip_updates=True)
    logs.finishlogging()


if __name__ == "__main__":
    start_bot()
