import requests
value = input("wprowadz walute z podanych (AUD, BGN, BRL, CAD, CHF, CNY, CZK, DKK, EUR, GBP, HKD, HUF, IDR, ILS, INR, ISK, JPY, KRW, MXN, MYR, NOK, NZD, PHP, RON, SEK, SGD, THB, TRY, USD, ZAR, ) : ")
response = requests.get(f"https://api.frankfurter.app/latest?from={value}")

if response.ok == True:
    data = response.json()
    rates = data["rates"]
    base = data["base"]
    date = data["date"]

    print(f"base {base}")
    print(f"date: {date}")
    #print(rates)
    for key, values in rates.items():
        print(f"{key} : {values}")