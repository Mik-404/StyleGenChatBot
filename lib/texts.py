import settings

so_har_msg = 'Такое сложное сообщение, а у меня лапки( 😿😿😿'

wrong_appeal_to_bot = 'Вы не привильно задали параметры. ' \
                      'Необходимый формат <Ник бота> <Стиль сообщения> \n' \
                      '!!Второй параметр можно не указывать. Пример: \n' \
                      '@{} cute'.format(settings.BOT_NAME)
wrong_command_to_bot = 'Вы не привильно задали параметры. \n' \
                      'Необходимый формат <Команда> <Ник бота> <Новое значение> \n' \
                       '!!Ник бота можно не указывать.' \
                      'Пример: \n' \
                      '/set_style @{} cute'.format(settings.BOT_NAME)

set_style_success = 'Ок, мы сменили стиль на {}'
set_prob_success = 'Ок, мы сменили вероятность на {}'
help_massage = 'Привет, я могу изменять стиль твоих сообщений!\n'\
               'Не понимаю английский!! И я не использую случайные сообщения длиноой меньше 3 слов.' \
               ' Всего я знаю 4 стиля: научный, грубый, милый, старославянский.'\
               ' А ещё я могу разговаривать как йода!\n'\
                'Ко мне можно обраться ответом на сообщение, указав при этом мой ник.'\
                ' Я использую текст пересланного сообщения для генерации ответа.\n'\
                'Затем мы можете указать стиль ВАЖНО !!(rude - грубый, yoda - йода, cute - милый, '\
                'old_rus - старославянский, scientific - научный или random - случайный) '\
                'или не указывать ничего, тогда будут использованы значения по умолчанию для вашего чата.\n'\
                'Бот также иногда выбирать некоторые сообщения в чате и изменять их стилистику с определённой '\
                'вероятностью, которую вы можете изменять. !!(Значение от 0 до 100) \n'\
                'Узнать текущие настройки можно командой ' \
                '/status <имя бота>\n' \
                '/set_style <имя бота> <новое значение> изменяет значение по умолчанию вашего стиля\n'\
                '/set_prob <имя бота> <новое значение> изменяет ' \
                'вероятность ответа на случайное сообщение от 0 % до 100%\n' \
                '/help <имя бота> описание бота\n'\
                '/start <имя бота> запуск бота\n'\
                '!!В командах имя бота указывать не обязательно.\n' \
                'Пример команды:\n' \
                '/status @{}'.format(settings.BOT_NAME)

status_info = 'Стиль по умолчанию: {}, Вероятность ответа на случайное сообщение: {} %'
too_many_reauests = 'Извините, сейчас сервер слишком нагружен и не может обрабатывать ваш запрос. 😞'

