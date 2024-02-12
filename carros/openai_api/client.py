import openai
import configparser
import os 

userprofile = os.environ.get('USERPROFILE') or os.environ.get('HOME')
credentials_path = os.path.join(userprofile, 'Área de Trabalho\\Projetos\\DjangoMaster\\')
config = configparser.ConfigParser()
config.read(credentials_path + 'APIDjangoMaster.ini')

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
