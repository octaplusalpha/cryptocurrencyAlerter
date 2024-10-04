from cryptoData import get_coins, Coin


def alert(symbol: str, bottom: float, top: float, coin):
    # for coin in coin_list:
        if coin.symbol == symbol:
            if coin.current_price < bottom or coin.current_price > top:
                print(f"{coin.symbol} is now {coin.current_price}")
            else:
                print(f"{coin.symbol} is still within the range of N{bottom} to N{top}")


if __name__ == '__main__':
    coins: list = get_coins()

    # alert(symbol="btc", bottom=20000, top=24000, coin=coin)
    # alert(symbol="eth", bottom=1800, top=1900, coin_list=coins)
    # alert(symbol="xrp", bottom=.47, top=0.48, coin_list=coins)
