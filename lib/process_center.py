import settings
from lib import texts, message_processing
from lib.utils import *

sem = asyncio.Semaphore(settings.REQUESTS_TO_TTM)
generator = message_processing.ProcessingModel()


async def distribution_center(message_type, message_text):
    try:
        if not sem.locked():
            async with sem:
                loop = asyncio.get_event_loop()
                for i in range(2):
                    future = loop.create_future()
                    loop.create_task(generator.generate(message_type, message_text, future))
                    await future
                    gen = future.result()
                    if gen != '-':
                        return gen
                return texts.so_har_msg
        else:
            return texts.too_many_reauests
    except:
        return texts.too_many_reauests
