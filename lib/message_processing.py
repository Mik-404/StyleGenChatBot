from lib.utils import *
from lib import logs
import pandas as pd
import tune_the_model as ttm

KEY_FILENAME = 'settings.py'
SAMPLES_SEP = '\n\n'


class ProcessingModel:
    def __init__(self, type_list):
        
        with open(KEY_FILENAME) as f:
            for param in f.readlines():
                if 'TTM_TOKEN' in param:
                    line = param.split('=')[1].strip()[1:-1]
                    ttm.set_api_key(line)
            
        self.type_list = type_list
        self.few_shot_starter = dict()
        self.few_shot_types = dict()
        
        for [name, filename] in self.type_list.items():
            print(name + ' ' + filename)
            try:
              sample = pd.read_csv(filename, sep=';')
              sample_text = ''
              
              text_type = sample.columns[0]
              converted_text_type = sample.columns[1]
              self.few_shot_types[name] = [text_type, converted_text_type]
              
              for row in sample.iterrows():
                  sample_text += f'{text_type}: {row[1][0]}\n'
                  sample_text += f'{converted_text_type}: {row[1][1]}\n'
                  sample_text += SAMPLES_SEP
              sample_text += f'{text_type}: '

              self.few_shot_starter[name] = sample_text
            except Exception as e:
                logs.botLogReplicas.style_processing_crashed("--Style loading crashed...", e)
              
            
            
    def generate(self, text_type, text):
        if text_type in self.few_shot_starter:
          few_shot_text = self.few_shot_starter[text_type]
          few_shot_text += text + '\n'
          few_shot_text += self.few_shot_types[text_type][1] + ': '
          return list(ttm.generate(few_shot_text)[0].split(SAMPLES_SEP))[0]
        a = 6 / 0
