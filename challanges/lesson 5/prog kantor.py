import requests

currency = "pln"
coinsList = None

def getCoinsList():
    global coinsList
    # [ {'id': '01coin', 'symbol': 'zoc', 'name': '01coin', 'platforms': {}}, ... ]
    response = requests.get("https://api.coingecko.com/api/v3/coins/list?include_platform=true")
    if response.ok == True:
        print("response ok")
        data = response.json()
        print(data[0])
        print("Ilość kryptowalut: " + str(len(data)))
        coinsList = data


def findCoinBySymbol(symbol):
    symbol = symbol.lower().strip()
    for coin in coinsList:
        if coin["symbol"] == symbol:
            return coin
    else:
        return None

def getCoinLastMarketData(coinId):
    # {'bitcoin': {'pln': 196445, 'pln_market_cap': 3673378580174.0874, 'pln_24h_vol': 174245706368.16504, 'pln_24h_change': 5.183517675973496, 'last_updated_at': 1615110843}}
    response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids="+coinId+"&vs_currencies="+currency+"&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true")
    if response.ok:
        data = response.json()
        return data
    else:
        return None

def getCoinPriceInCurrency(coinId, currency):
    currency = currency.lower().strip()
    marketData = getCoinLastMarketData(coinId)
    return marketData[coinId][currency]

getCoinsList()

btcData = findCoinBySymbol("btc")
print(btcData)

marketData = getCoinLastMarketData(btcData["id"])
print("marketData: ", marketData)

coinPrice = getCoinPriceInCurrency(btcData["id"], currency)
print("Coin price in " + currency, coinPrice)


print("\nWitamy w crypto exchange")

while True:
    cryptoSymbolToBuy = input("Wybierz symbol krypto do kupienia np btc lub exit aby zakończyć: ")
    if cryptoSymbolToBuy == "exit": break

    coinData = findCoinBySymbol( cryptoSymbolToBuy )
    if coinPrice == None:
        print("Nie ma takiej kryptowaluty")
        continue

    coinPrice = getCoinPriceInCurrency(coinData["id"], currency)
    print("Cena " + str(coinData["id"]),  coinPrice, currency)

    moneyToBuyCrypto = float( input("Ile chcesz przeznaczyć na zakup: ") )
    boughtCrypto = moneyToBuyCrypto / coinPrice

    print("\nGratulacje kupiłeś " + str(boughtCrypto) + " " + cryptoSymbolToBuy )



