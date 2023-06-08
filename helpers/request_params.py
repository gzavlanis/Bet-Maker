import os
from dotenv import load_dotenv
load_dotenv()

url = os.environ.get('API_URL')
key = os.environ.get('API_KEY')

def object(selected_odds):
    return {
        "currency_id": 44,
        "amount": 1,
        "odds": selected_odds
    }

def headers():
    return {
        "x-api-key": key
    }