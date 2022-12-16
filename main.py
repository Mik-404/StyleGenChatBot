from aiogram import Bot, types
from aiogram.dispatcher import filters
from aiogram.utils import executor
from aiogram import Dispatcher
import asyncio
import handler_filters
import processing_of_message
import settings
import logs


bot = Bot(token=settings.TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(handler_filters.ReplyFilterBot())
async def style_gen(message: types.Message):
    try:
        logs.log_(f"--New message detected: {message.text[0 : min (len(message.text), 100)]}")
        if '@' + settings.BOT_NAME in message.text and len(message.text.split()) == 2:
            if message.text.split()[1] in settings.features:
                answer_gen = processing_of_message.ProcessingOfMessage(message.text, message.text.split()[1])
                await message.answer(answer_gen.answer_text())
                logs.log_(f"--Message successful processed: {message.text[0: min(len(message.text), 100)]}")
                return
        logs.log_(f"--User is stupid: {message.text[0: min(len(message.text), 100)]}")
    except Exception as e:
        logs.log_(f"--Message was crashed: {message.text[0: min(len(message.text), 100)]}")
        logs.log_(f"   {e}")

def start_bot():
    logs.clear_log_()
    logs.log_("Bot started...")
    executor.start_polling(dp, skip_updates=True)
    logs.log_("Bot died...")


if __name__ == "__main__":
    start_bot()
