import requests
import json
from config import currency


class APIException(Exception):
    pass

class Convertor:
    @staticmethod
    def get_price(quote, base, amount):

        try:
            quote_key = currency[quote.lower()]
        except KeyError:
            raise APIException(f'А ты думаешь "{quote}" существует 🤨?')

        try:
            base_key = currency[base.lower()]
        except KeyError:
            raise APIException(f'Как будто бы нет "{base}" такой валюты 🤪')

        if quote_key == base_key:
            raise APIException(f'Серьезно? Две одинаковых валюты "{quote}"? Это невыполнимо 😤')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не понял, сколько-сколько? Прям "{amount}", да 😧 ?')

        r = requests.get(f"https://www.cbr-xml-daily.ru/latest.js")
        currencies = json.loads(r.content)
        x = [{"RUB", 1}]
        currencies.update(x)
        # vivod = currencies[currency[quote.lower()]] * float(amount)
        vivod= currencies['rates'][currency[quote.lower()]] * amount
        vivod = round(vivod, 3)
        text = f'Цена {amount} {quote} в {base} - {vivod}'
        return text
