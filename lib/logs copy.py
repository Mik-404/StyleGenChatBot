import settings
from lib.utils import *

last_message_ID = 1


def add_new_message_content(message: types.Message, ID_message):
    with open(settings.LOGS_ADDR + '/' + settings.MESSAGE_LOGS_NAME, 'a+', encoding="utf-8") as file:
        file.write('ID ' + str(ID_message) + '\n')
        file.write('    ' + str(message) + '\n')


def log_action(message):
    with open(settings.LOGS_ADDR + '/' + settings.PROCESS_LOGS_NAME, 'a+', encoding="utf-8") as file:
        file.write(message + '\n')


def startlogging():
    if not os.path.isdir(settings.LOGS_ADDR):
        os.makedirs(settings.LOGS_ADDR)
    with open(settings.LOGS_ADDR + '/' + settings.PROCESS_LOGS_NAME, 'w', encoding="utf-8") as file:
        file.write('Bot started...' + '\n')
    with open(settings.LOGS_ADDR + '/' + settings.MESSAGE_LOGS_NAME, 'w', encoding="utf-8") as file:
        file.write('')


def finishlogging():
    with open(settings.LOGS_ADDR + '/' + settings.PROCESS_LOGS_NAME, 'a+', encoding="utf-8") as file:
        file.writelines("Bot died...")


class botLogReplicas():
    def __init__(self, message: types.Message):
        global last_message_ID
        self.ID = last_message_ID
        self.start_message = "--New message detected. ID= " + str(self.ID) + ' '
        self.success_finish_message = "--Message successful processed. ID= " + str(self.ID) + ' '
        self.error_f1_message = "--Message was crashed. ID= " + str(self.ID) + ' '
        self.error_tab = '   '
        self.style_processing_crashed_message = "--Reply checking was crashed. ID= " + str(self.ID) + ' '
        self.filter_crashed_message = "--New Message Generate was crashed. ID= " + str(self.ID) + ' '
        self.wrong_request_message = "--User is stupid. ID= " + str(self.ID) + ' '
        self.message = message
        last_message_ID += 1

    def start_processing(self):
        log_action(self.start_message)
        add_new_message_content(self.message, self.ID)

    def success_finish(self):
        log_action(self.success_finish_message)

    def error(self, e: Exception):
        log_action(self.error_f1_message)
        log_action(self.error_tab + str(e))

    def wrong_request_from_user(self):
        log_action(self.wrong_request_message)

    def style_processing_crashed(self, e: Exception):
        log_action(self.style_processing_crashed_message)
        log_action(self.error_tab + str(e))

    @staticmethod
    def filter_crashed(filter_crashed_message, e: Exception):
        log_action(filter_crashed_message)
        log_action('    ' + str(e))
