import asyncio
import copy

import settings
from lib import texts, message_processing
from lib.utils import *

sem = asyncio.Semaphore(settings.REQUESTS_TO_TTM)
generator = message_processing.ProcessingModel()


async def distribution_center(message_type, message_text):
    if not sem.locked():
        async with sem:
            loop = asyncio.get_event_loop()
            future = loop.create_future()
            loop.create_task(generator.generate(message_type, message_text, future))
            await future
            gen = future.result()
            return gen
    else:
        return texts.too_many_reauests
