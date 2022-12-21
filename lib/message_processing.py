from lib.utils import *
from lib import logs
import settings
import tune_the_model as ttm

KEY_FILENAME = 'settings.py'
SAMPLES_SEP = '\n\n'

class ProcessingModel:
    def __init__(self):
        ttm.set_api_key(settings.TTM_TOKEN)
        self.type_list = settings.MODELS
        
        self.fine_tuned_models = dict()
        
        for [name, filename] in self.type_list.items():
            try:
                self.fine_tuned_models[name] = ttm.TuneTheModel.from_id(filename)
                print(f"{name} model is perfectly downloaded")
            except:
                print(f"{name} model had issues with loading ...")
    

    def generate(self, text_type, text):
        if text_type in self.fine_tuned_models:
            answer = self.fine_tuned_models[text_type].generate(text)[0]
            return answer
        a = 6 / 0
    
