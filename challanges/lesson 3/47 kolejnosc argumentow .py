def bookTickets(band , ticketsNumber, /, *,ticketType = "standard", section = "general"):
    print("Rezerwacja biletow : ")
    print("Zespol : ", band)
    print(" liczba biletow : ", ticketsNumber)
    print(" Rodzaj biletow : ", ticketType)
    print("sekcja : ", section)


band = input("podaj zespol : ")
ticketsNumber = input("podaj liczbe biletow : ")
ticketType = input("podaj typ biletu : ")
section = input("podaj jaka sekcje chcesz : ")
bookTickets(band, ticketsNumber, ticketType=ticketType, section=section)