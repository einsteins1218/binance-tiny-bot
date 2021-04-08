
ohlc = {
    "BTC":[100, 200, 300, 400],
    "ETH":[200, 300, 400, 500]
}

def get_open_price(currency):
    return ohlc[currency][0]

def get_close_price(currency):
    return ohlc[currency][3]

