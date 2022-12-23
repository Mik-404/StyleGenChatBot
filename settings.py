TOKEN = ''
TTM_TOKEN = ''
BOT_NAME = 'stylechangerNLPnebot'

ADDR = 'flud'
PROCESS_LOGS_NAME = 'process_logs.txt'
MESSAGE_LOGS_NAME = 'message_logs.txt'
DB_LOGS_NAME = 'db_log.txt'
DATABASE_NAME = 'db.json'

REQUESTS_TO_TTM = 15
BASE_SETTING_CHAT_IN_DATABASE = {
    "style": "random",
    "p": '50',
}
STYLES = ['rude', 'yoda', 'scientific', 'cute', 'old_rus', 'random']
MODELS = {
    'rude': '633b6955f7afbca241e611ae313d83ee',
    'cute': 'dfa074d119af6e9e15a5f18717b98941',
    'scientific': '9e68215a87e86320a044f41907e1e8d5',
    'yoda': '2ed91ea1878c4f08ffd57a4ae32bb1b5',
    'old_rus': '77a0b80f1962ccac71d3544c16efca89'
}