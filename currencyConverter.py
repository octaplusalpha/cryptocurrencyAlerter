import requests
from cryptoData import get_coins
from alerter import alert


def convert_currency( symbol: str, convert_to: str, convert_from: str, coin_list: list):
        api_key = '7eed2fe0d77bc4c5049c0da7'
        url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{convert_from}'

        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            raise Exception("Error fetching data from the API")

        exchange_rate = data['conversion_rates'][convert_to]
        converted_amount = coin.current_price * exchange_rate

        return converted_amount



if __name__ == '__main__':
    target_symbol: str = input('Enter a type of coin: ')
    coins = get_coins()
    selected_coin = None
    for coin in coins:
        if coin.symbol == target_symbol.lower():
            selected_coin = coin
            break
    if selected_coin:
        currency = convert_currency(selected_coin.symbol, 'NGN', 'EUR', selected_coin)
        print(f'converted amount for {selected_coin.symbol}: N{currency}')
        alert(target_symbol, 50000, 100000, selected_coin)
    else:
        print(f'Coin with symbol {target_symbol} not found')




