import requests
from dotenv import load_dotenv
import os


def SetUp():
    ''''''
    load_dotenv()
    api_key = os.getenv("api_key")
    r = requests.get(f'https://v6.exchangerate-api.com/v6/{api_key}/latest/USD')
    currencies = r.json()

    return currencies


def ConvertCurrency(value1, value2, chosen_currency_1, chosen_currency_2):
    currencies = SetUp()

    USD = 1
    from_currency = currencies['conversion_rates'][f'{chosen_currency_1}']
    to_currency = currencies['conversion_rates'][f'{chosen_currency_2}']

    try:
        if value1:
            converted_amount = (float(USD / from_currency * to_currency)) * float(value1)
            return converted_amount

        else:
            converted_amount = (float(USD / from_currency * to_currency)) * float(value2)
            return converted_amount
    except (ValueError, TypeError):
        pass


def main():
    currencies = SetUp()
    x = ConvertCurrency("EUR", "USD", currencies)
    print(f"{x:.3f}")


if __name__ == '__main__':
    main()

