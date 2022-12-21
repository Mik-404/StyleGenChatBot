import settings
from lib.utils import *

last_message_ID = 1


def add_new_message_content(message: types.Message, ID_message):
    with open(settings.ADDR + '/' + settings.MESSAGE_LOGS_NAME, 'a+', encoding="utf-8") as file:
        file.write('ID ' + str(ID_message) + '\n')
        file.write('    ' + str(message) + '\n')


def log_action(message):
    with open(settings.ADDR + '/' + settings.PROCESS_LOGS_NAME, 'a+', encoding="utf-8") as file:
        file.write(message + '\n')


def db_log_action(message):
    with open(settings.ADDR + '/' + settings.DB_LOGS_NAME, 'a+', encoding='utf-8') as file:
        file.write(message + '\n')


def startlogging():
    if not os.path.isdir(settings.ADDR):
        os.makedirs(settings.ADDR)
    with open(settings.ADDR + '/' + settings.PROCESS_LOGS_NAME, 'w', encoding="utf-8") as file:
        file.write('Bot started...' + '\n')
    with open(settings.ADDR + '/' + settings.MESSAGE_LOGS_NAME, 'w', encoding="utf-8") as file:
        file.write('')


def dbstartlogging():
    with open(settings.ADDR + '/' + settings.DB_LOGS_NAME, 'w', encoding='utf-8') as file:
        file.write('')


def finishlogging():
    with open(settings.ADDR + '/' + settings.PROCESS_LOGS_NAME, 'a+', encoding="utf-8") as file:
        file.writelines("Bot died...")


class BotLogReplicas:
    def __init__(self, message: types.Message):
        global last_message_ID
        self.ID = last_message_ID
        self.new_appeal_detected = "--New appeal detected. ID= " + str(self.ID) + ' '

        self.got_random_message = "--I got random message. ID= " + str(self.ID) + ' '

        self.new_set_style_command_detected = "--New set_style command detected. ID= " + str(self.ID) + ' '

        self.new_set_prob_command_detected = "--New set_prob command detected. ID= " + str(self.ID) + ' '

        self.success_finish = "--Appeal successful processed. ID= " + str(self.ID) + ' '
        self.error_message = "--Appeal was crashed. ID= " + str(self.ID) + ' '
        self.wrong_request_message = "--User is stupid. ID= " + str(self.ID) + ' '

        self.error_tab = '   '
        self.filter_reply_crashed_message = "--Reply checking was crashed. ID= " + str(self.ID) + ' '
        self.filter_command_crashed_message = "--Command checking was crashed. ID= " + str(self.ID) + ' '

        self.message = message
        last_message_ID += 1

    def start_appeal_processing(self):
        log_action(self.new_appeal_detected)
        add_new_message_content(self.message, self.ID)

    def start_random_message_processing(self):
        log_action(self.got_random_message)
        add_new_message_content(self.message, self.ID)

    def start_set_style_processing(self):
        log_action(self.new_set_style_command_detected)
        add_new_message_content(self.message, self.ID)

    def start_set_prob_processing(self):
        log_action(self.new_set_prob_command_detected)
        add_new_message_content(self.message, self.ID)

    def success_finish_processing(self):
        log_action(self.success_finish)

    def error_processing(self, e: Exception):
        log_action(self.error_message)
        log_action(self.error_tab + str(e))

    def wrong_request_from_user(self):
        log_action(self.wrong_request_message)

    def filter_reply_crashed(self, e: Exception):
        log_action(self.filter_reply_crashed_message)
        log_action(self.error_tab + str(e))

    def filter_command_crashed(self, e: Exception):
        log_action(self.filter_command_crashed_message)
        log_action(self.error_tab + str(e))

    @staticmethod
    def style_preprocessing_crashed(e: Exception):
        log_action("--Style loading crashed...")
        log_action('    ' + str(e))


class DatabaseLog:
    def __init__(self):
        self.create_new_entry = "Create_new_entry. Chat id = {}"
        self.set_prob_command_detected = "--New set_prob command detected. Chat id = {}, new value = {}"
        self.set_style_command_detected = "--New set_style command detected. Chat id = {}, new value = {}"
        self.get_style = "--New get_style request detected. Chat id = {}"

    def start_create_new_entry(self, chat_id):
        db_log_action(self.create_new_entry.format(chat_id))

    def start_set_style_processing(self, chat_id, new_style):
        db_log_action(self.set_style_command_detected.format(chat_id, new_style))

    def start_get_style_processing(self, chat_id):
        db_log_action(self.get_style.format(chat_id))

    def start_set_prob_processing(self, chat_id, new_prob):
        db_log_action(self.set_prob_command_detected.format(chat_id, new_prob))
