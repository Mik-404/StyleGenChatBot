import settings


def clear_log_():
    with open(settings.LOGS_ADDR, 'w', encoding="utf-8") as file:
        file.write('')


def log_(message):
    with open(settings.LOGS_ADDR, 'a+', encoding="utf-8") as file:
        file.writelines(message + '\n')
