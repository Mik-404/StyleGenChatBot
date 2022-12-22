from lib import logs, handler_filters, db, texts, process_center
import settings
from lib.utils import *

bot = Bot(token=settings.TOKEN)
dp = Dispatcher(bot)

INFO_group = {}


@dp.message_handler(handler_filters.FilterBot())
async def style_gen(message: types.Message):
    logging = logs.BotLogReplicas(message)
    await logging.start_appeal_processing()
    try:
        if '@' + settings.BOT_NAME in message.text and len(message.text.split()) == 2 \
                and message.text.split()[-1] in settings.STYLES:
            await db.db_check_contain(INFO_group, message.chat.id)
            msg_type = db.db_get_style(message.chat.id, INFO_group, message.text.split()[-1])
            msg_text = message.reply_to_message.text
            answer_gen = await process_center.distribution_center(msg_type, msg_text)
            await message.reply(answer_gen)
            await logging.success_finish_processing()
        elif '@' + settings.BOT_NAME in message.text and len(message.text.split()) == 1:
            await db.db_check_contain(INFO_group, message.chat.id)
            msg_type = db.db_get_style(message.chat.id, INFO_group)
            msg_text = message.reply_to_message.text
            answer_gen = await process_center.distribution_center(msg_type, msg_text)
            await message.reply(answer_gen)
            await logging.success_finish_processing()
        else:
            await message.reply(texts.wrong_appeal_to_bot)
            await logging.wrong_request_from_user()
    except Exception as e:
        await logging.error_processing(e)


@dp.message_handler(commands=['set_style'], content_types=types.ContentType.TEXT)
async def set_style(message: types.Message):
    logging = logs.BotLogReplicas(message)
    await logging.start_set_style_processing()
    try:
        if '@' + settings.BOT_NAME in message.text \
                and (len(message.text.split()) == 2 or len(message.text.split()) == 3) \
                and message.text.split()[-1] in settings.STYLES:
            style_type = message.text.split()[-1]
            await db.db_set_style(INFO_group, message.chat.id, style_type)
            await message.reply(texts.set_style_success.format(INFO_group[str(message.chat.id)]["style"]))
            await logging.success_finish_processing()
        else:
            await message.reply(texts.wrong_command_to_bot)
            await logging.wrong_request_from_user()
    except Exception as e:
        await logging.error_processing(e)


@dp.message_handler(commands=['set_prob'], content_types=types.ContentType.TEXT)
async def change_variety(message: types.Message):
    logging = logs.BotLogReplicas(message)
    await logging.start_set_prob_processing()
    try:
        if '@' + settings.BOT_NAME in message.text \
                and (len(message.text.split()) == 2 or len(message.text.split()) == 3) \
                and await is_int(message.text.split()[-1]) and 100 >= int(message.text.split()[-1]) >= 0:
            new_prob = message.text.split()[-1]
            await db.db_set_prob(INFO_group, message.chat.id, new_prob)
            await message.reply(texts.set_prob_success.format(INFO_group[str(message.chat.id)]["p"]))
            await logging.success_finish_processing()
        else:
            await message.reply(texts.wrong_command_to_bot)
            await logging.wrong_request_from_user()
    except Exception as e:
        await logging.error_processing(e)


@dp.message_handler(commands=['help'], content_types=types.ContentType.TEXT)
async def help_for_user(message: types.Message):
    await message.reply(texts.help_massage)


@dp.message_handler(commands=['status'], content_types=types.ContentType.TEXT)
async def get_status(message: types.Message):
    await db.db_check_contain(INFO_group, message.chat.id)
    await message.reply(texts.status_info.format(INFO_group[str(message.chat.id)]["style"],
                                                 INFO_group[str(message.chat.id)]["p"]))


@dp.message_handler(handler_filters.FilterOtherCommands(), content_types=types.ContentType.TEXT)
async def style_gen2(message: types.Message):
    await db.db_check_contain(INFO_group, message.chat.id)
    if random.randint(1, 100) < int(INFO_group[str(message.chat.id)]["p"]) \
            and len([w for w in filter(r.match, message.text.split())]) > 2:
        logging = logs.BotLogReplicas(message)
        await logging.start_random_message_processing()
        try:
            msg_type = await db.db_get_style(message.chat.id, INFO_group)
            msg_text = message.text
            answer_gen = await process_center.distribution_center(msg_type, msg_text)

            await message.reply(answer_gen)
            await logging.success_finish_processing()
        except Exception as e:
            await logging.error_processing(e)


def start_bot():
    global INFO_group
    logs.startlogging()
    INFO_group = db.db_init_()
    executor.start_polling(dp, skip_updates=True)
    db.db_close_(INFO_group)
    logs.finishlogging()


if __name__ == "__main__":
    start_bot()
