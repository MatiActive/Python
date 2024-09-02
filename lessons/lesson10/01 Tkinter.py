# Tkinter - biblioteka Pythona umozliwiajaca tworzenie aplikacji z interfejsem uzytkownika(GUI - Graphical User Interface)

import tkinter as tk 
# window is instance of tkinter class 
window = tk.Tk()
window.title("Application") # app title 

# make label 
label1 = tk.Label(text = "Hello World")

# add label to window 

label1.pack()

label2 = tk.Label(
    text = "Hello Again",
    foreground= "white", # text color
    background="black"
)
label2.pack()
# mainloop is Tkinter event loop 


# Utworzenie okna wymaga powołanie instancji klasy TK czyli Tkinter 
# Okno pozwala na zmiane np. tytuł na belce aplikacji Etykiete tworzy się na podstawie klasy Label 
# mainloop() to nieskonczona pętla czekajac na zdarzenie od uytkownika aby je przeprocesowac tak długo jak okno nie zostało zamkniete

# LABEL - ETYKIETA WYSWIETLA TEKST W OKNIE 

label3 = tk.Label(master = window,
    text = "Hello LoL \n Hello LoL Again!",
    foreground="green",  # TEXT COLOR
    background="purple",  # BACKGROUND COLOR
    width=20,  # WIDTH IN CHARACTER
    height=3,  # HEIGHT IN CHARACTERS 
    cursor="dot",  # ARROW, DOT
    anchor = tk.E,  # EAST - TO THE RIGHT
    font= "Helvetica 16 bold italic underline",
    padx = 20,  # EXTRA SPACE TO THE  LEFT AND RIGHT
    pady = 20,  # EXTRA SPACE TO TOP AND DOWN
)
label3.pack() # ADD TO WINDOW 
window.mainloop()


# WIDGET LABEL WYŚWIETLA TEKST LUB OBRAZEK W OKRESLONYM OKNIE (MASTER) ORAZ AKCEPTUJE WIELE POTENCJALNYCH ARGUMENTOW

# ARGUMENT ANCHOR PRZYJMUJE WARTOŚĆ NW / N / NE / W / CENTER / E / SW / S /SE
# WIDTH I HEIGHT TO ILOŚĆ ZNAKOW 

# dodanie zdjecia  --- logo = tk.PhotoImage(file="nazwapliku.png") 
# wywolanie image = logo // label.pack(side="right/left")
# ETYKIETA MOZE BYC WZBOGACONA O OBRAZEK W TAKIM WYPADKU ARGUMENT WIDTH I HEIGHT WSKAZUJE NA ILOSC PIKSELI 

# ABY POLACZYC OBA ELEMENTY WYMAGANY JEST ARGUMENT compound = tk.CENTER
# ABY ZMIENIC WARTOSC W POZNIEJSZYM ETAMIE NALEZY UZYC np . label1.config(text="zmieniony tekst")