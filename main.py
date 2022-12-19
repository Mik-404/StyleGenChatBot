from lib import message_processing, logs, handler_filters
import settings
from lib.utils import *

bot = Bot(token=settings.TOKEN)
dp = Dispatcher(bot)

generator = message_processing.ProcessingModel({
    'rude': 'samples/rude.csv',
    'yoda': 'samples/yoda.csv'
})

@dp.message_handler(handler_filters.FilterBot())
async def style_gen(message: types.Message):
    logging = logs.botLogReplicas(message)
    logging.start_processing()
    try:
        if '@' + settings.BOT_NAME in message.text and len(message.text.split()) == 2:
            msg_type = message.text.split()[1]
            msg_text = message.reply_to_message.text
            answer_gen = generator.generate(msg_type, msg_text)
            await message.answer(answer_gen)
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
