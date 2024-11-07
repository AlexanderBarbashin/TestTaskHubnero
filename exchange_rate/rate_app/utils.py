import json
import os

import requests
from dotenv import load_dotenv
from requests import codes

url = "https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base=USD"

load_dotenv()

api_key = os.environ.get("API_KEY")

headers= {
  "apikey": api_key,
}

def get_rate_from_api() -> float | None:
    """
    Функция для получения текущего курса доллара к рублю.
    :return: курс | None
    """

    try:
        response = requests.request("GET", url, headers=headers, timeout=10)
        if response.status_code == codes.ok:
            response_content = json.loads(response.content.decode())
            rate = response_content.get("rates").get("RUB")
            return rate
    except TimeoutError:
        print("Service unavailable")
