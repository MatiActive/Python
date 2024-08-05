import requests

response = requests.get("https://api.frankfurter.app/latest?from=PLN")

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