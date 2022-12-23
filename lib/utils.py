from aiogram import Bot, types
from aiogram.dispatcher import filters
from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from aiogram import Dispatcher
import asyncio
import pandas as pd
import tune_the_model as ttm
import asyncio
import os
import time
import json
import random
import re
r = re.compile("[а-яА-Я]+")


async def is_int(a):
    try:
        b = int(a)
        return True
    except:
        return False
