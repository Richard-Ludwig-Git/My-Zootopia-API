import json
import requests
import os
from dotenv import load_dotenv

load_dotenv("secret.env")

def fetch_data(user_animal_input):
    API_KEY = os.getenv("API_KEY")
    SEARCH = user_animal_input
    url = f'https://api.api-ninjas.com/v1/animals?name={SEARCH}'
    res = requests.get(url, headers={'X-Api-Key': API_KEY})
    return json.loads(res.text)

