# Metoda pack() -   UMOŻLIWIA ROZMIESZCZENIE ELEMENTOW W BLOKACH WEWNĄTRZ OKNA.

import tkinter as tk 
window = tk.Tk()
label1 = tk.Label(window, text="Information text #1")
label1.pack(side = tk.TOP, expand=True)

label2 = tk.Label(window, text="Next information text #2")
label2.pack(side = tk.TOP, expand=True)

label3 = tk.Label(window, text="Bottom information text #3")
label3.pack(side="bottom", expand=True)

button1 = tk.Button(window, text="Opt 1", fg="red")
button1.pack(side = tk.LEFT)

button2 = tk.Button(window, text="Opt 2", fg="green")
button2.pack(side=tk.RIGHT)

window.mainloop()

### OPCJE:
# expand - JEŚLI TRUE WIDGET ROZSZERZA SIE NA DOSTEPNA PRZESTRZEN
# fill - CZY WIDGET WYPEŁNI DODATKOWA PRZESTRZEN ALBO AJMIE MINIMALNA PRZESTRZEN - NONE - DOMYSLNIE 
# X - WYPELNI SIE HORYZONTALNIE
# Y - WERTYKALNIE, BOTH - OBIE
# side -  STRONA: TOP, BOTTOM, LEFT, RIGHT   ###

# METODA PACK() - FILL POZWALA NA WYPEŁNIENIE DODATKOWEJ PRZESTRZENI, KTÓRA NP POJAWI SIE PRZY POWIEKSZENIU OKNA. 

window2 = tk.Tk()

label4 = tk.Label(window2, background="red",
                  text="Information text #1")
label4.pack(fill= tk.BOTH, side= tk.TOP, expand=True)

label5 = tk.Label(window2,background="yellow",
                  text="Next information text #2")
label5.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

label6 = tk.Label(window2,background="green",text="bottom information text #3")
label6.pack(fill= tk.BOTH, side= tk.BOTTOM, expand=True)

button3 = tk.Button(window2, background="red",text="Opt 1", fg="black")
button3.pack(fill= tk.BOTH,side=tk.LEFT)

button4 = tk.Button(window2, background="green", text="Opt 2", fg="blue")
button4.pack(fill=tk.BOTH, side=tk.RIGHT)

window2.mainloop()
