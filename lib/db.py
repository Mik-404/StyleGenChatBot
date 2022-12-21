from lib.utils import *
from lib import logs
import settings


def db_get_style(chat_id, INFO_group, stl=None):
    if stl:
        if stl == 'random':
            return list(settings.MODELS.keys())[random.randint(1, len(settings.MODELS)) - 1]
        else:
            return stl
    logs.DatabaseLog().start_get_style_processing(chat_id)
    chat_id = str(chat_id)
    type_msg = INFO_group[chat_id]['style']
    if type_msg == 'random':
        type_msg = list(settings.MODELS.keys())[random.randint(1, len(settings.MODELS)) - 1]
    return type_msg


def db_set_style(INFO_group, chat_id, new_style):
    logs.DatabaseLog().start_set_style_processing(chat_id, new_style)
    chat_id = str(chat_id)
    if chat_id not in INFO_group.keys():
        INFO_group[chat_id] = settings.BASE_SETTING_CHAT_IN_DATABASE
    INFO_group[chat_id]["style"] = new_style


def db_set_prob(INFO_group, chat_id, prob):
    logs.DatabaseLog().start_set_prob_processing(chat_id, prob)
    chat_id = str(chat_id)
    if chat_id not in INFO_group.keys():
        INFO_group[chat_id] = settings.BASE_SETTING_CHAT_IN_DATABASE
    INFO_group[chat_id]["p"] = prob


def db_check_contain(INFO_group, chat_id):
    chat_id = str(chat_id)
    if chat_id not in INFO_group.keys():
        logs.DatabaseLog().start_create_new_entry(chat_id)
        INFO_group[chat_id] = settings.BASE_SETTING_CHAT_IN_DATABASE


def db_init_():
    try:
        with open(settings.ADDR + '/' + settings.DATABASE_NAME, 'r') as f:
            return json.load(f)
    except Exception as e:
        with open(settings.ADDR + '/' + settings.DATABASE_NAME, 'w') as f:
            f.write('{}')
        print(e)
        return {}


def db_close_(INFO_group):
    try:
        with open(settings.ADDR + '/' + settings.DATABASE_NAME, "w") as f:
            json.dump(INFO_group, f)
    except Exception as e:
        print(e)
