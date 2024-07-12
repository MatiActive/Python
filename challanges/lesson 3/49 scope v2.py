accountBalance = 0 

def addFunds():
    global accountBalance
    add = int(input("podaj wartosc dodania do konta "))
    accountBalance = accountBalance + add
    print("wprowadzono srodki w kwocie", add, "zl")
def withDrawFunds():
    global accountBalance
    less = int(input("podaj kwote do wplaty z konta "))
    if less <= accountBalance:
        accountBalance = accountBalance - less
        print("wyplacono srodki w kwocie", less, "zl")
    else:
        print("stan konta nie pozwala na wyplate takiej kwoty ")
def displayBalance():
    print("stan konta : ",accountBalance, "zl")
while True:
    action = input("wybierz 'wplata' 'wyplata' 'stan konta' lub 'exit' ").lower()
    if action == "exit": break
    elif action == "wplata":
        addFunds()
    elif action == "wyplata":
        withDrawFunds()
    elif action == "stan":
        displayBalance()
    else:
        print("nieznana wartosc polecenia")