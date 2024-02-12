import openai
import configparser
import os 
from pathlib import Path

config_file_path = Path('/var/www/DjangoMaster') / 'APIDjangoMaster.ini'
config = configparser.ConfigParser()
config.read(str(config_file_path))

def get_car_ai_bio(model, brand, year):
    prompt = f'''
    Create a bio in portuguese for a car model {model} from {brand} of the year {year} with 250 words.
    '''
    openai.api_key = config['API']['secret-key']
    
    response = openai.Completion.create(
        model='gpt-3.5-turbo-1106',
        prompt=prompt,
        max_tokens=100,
    )
    return response['choices'][0]['text']
