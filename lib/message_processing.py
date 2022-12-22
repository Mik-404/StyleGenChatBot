from lib.utils import *
from lib import logs
import settings


class ProcessingModel:
    def __init__(self):
        ttm.set_api_key(settings.TTM_TOKEN)
        self.type_list = settings.MODELS

        self.fine_tuned_models = dict()
        try:
            for [name, filename] in self.type_list.items():
                self.fine_tuned_models[name] = ttm.TuneTheModel.from_id(filename)
            logs.BotLogReplicas.style_preprocessing_success()
        except Exception as e:
            logs.BotLogReplicas.style_preprocessing_crashed(e)
            exit(0)

    async def generate(self, text_type, text, future):
        answer = self.fine_tuned_models[text_type].generate(text)[0]
        future.set_result(answer)
