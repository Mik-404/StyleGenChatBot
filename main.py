from lib import message_processing, logs, handler_filters, db
import settings
from lib.utils import *

import random

bot = Bot(token=settings.TOKEN)
dp = Dispatcher(bot)

generator = message_processing.ProcessingModel()
INFO_group = {}


@dp.message_handler(handler_filters.FilterBot())
async def style_gen(message: types.Message):
    logging = logs.BotLogReplicas(message)
    logging.start_processing()
    try:
        if '@' + settings.BOT_NAME in message.text and len(message.text.split()) <= 2:
            if len(message.text.split()) == 2:
                msg_type = message.text.split()[1]
            else:
                db.db_check_contain(INFO_group, message.chat.id)
                msg_type = db.db_get_style(message.chat.id, INFO_group)
            msg_text = message.reply_to_message.text
            answer_gen = generator.generate(msg_type, msg_text)
            await message.answer(answer_gen)
            logging.success_finish()
        else:
            logging.wrong_request_from_user()
    except Exception as e:
        logging.error(e)


@dp.message_handler(commands=['set_style'], content_types=types.ContentType.TEXT)
async def set_style(message: types.Message):
    logging = logs.BotLogReplicas(message)
    logging.start_processing()
    try:
        if '@' + settings.BOT_NAME in message.text \
                and (len(message.text.split()) == 2 or len(message.text.split()) == 3) \
                and message.text.split()[-1] in settings.STYLES:
            style_type = message.text.split()[-1]
            db.db_set_style(INFO_group, message.chat.id, style_type)
            await message.answer(f'Ок, мы сменили стиль на {INFO_group[str(message.chat.id)]["style"]}')
            logging.success_finish()
        else:
            logging.wrong_request_from_user()
    except Exception as e:
        logging.error(e)


@dp.message_handler(commands=['set_prob'], content_types=types.ContentType.TEXT)
async def change_variety(message: types.Message):
    logging = logs.BotLogReplicas(message)
    logging.start_processing()
    try:
        if '@' + settings.BOT_NAME in message.text \
                and (len(message.text.split()) == 2 or len(message.text.split()) == 3) \
                and is_int(message.text.split()[-1]) and 100 >= int(message.text.split()[-1]) >= 0:
            new_prob = message.text.split()[-1]
            db.db_set_prob(INFO_group, message.chat.id, new_prob)
            await message.answer(f'Ок, мы сменили вероятность на {INFO_group[str(message.chat.id)]["p"]}')
            logging.success_finish()
        else:
            logging.wrong_request_from_user()
    except Exception as e:
        logging.error(e)


@dp.message_handler(content_types=types.ContentType.TEXT)
async def style_gen2(message: types.Message):
    db.db_check_contain(INFO_group, message.chat.id)
    if random.randint(1, 100) < int(INFO_group[str(message.chat.id)]["p"]):
        logging = logs.BotLogReplicas(message)
        logging.start_processing()
        try:
            msg_type = db.db_get_style(message.chat.id, INFO_group)
            msg_text = message.text
            answer_gen = generator.generate(msg_type, msg_text)
            await message.answer(answer_gen)
            logging.success_finish()
        except Exception as e:
            logging.error(e)


def start_bot():
    global INFO_group
    logs.startlogging()
    INFO_group = db.db_init_()
    executor.start_polling(dp, skip_updates=True)
    db.db_close_(INFO_group)
    logs.finishlogging()


if __name__ == "__main__":
    start_bot()
