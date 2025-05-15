import json
import requests

def fetch_data(user_animal_input):
    API_KEY = 'UN4D5vRBaN8ybUMEfq5x3g==OQ4jGHiWAkmE0Zxf'
    SEARCH = user_animal_input
    url = f'https://api.api-ninjas.com/v1/animals?name={SEARCH}'
    res = requests.get(url, headers={'X-Api-Key': API_KEY})
    return json.loads(res.text)