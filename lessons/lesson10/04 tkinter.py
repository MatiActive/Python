 # METODA GRID()  -- UMIESZCZA ELEMENTY W  DWUWYMIAROWEJ TABELI  

import tkinter  as tk 

window = tk.Tk() 

label1 = tk.Label(window, text="Name:")
label1.grid(row= 0, column=0, padx= 2, pady=2)

label2 = tk.Label(window, text="Surname:")
label2.grid(row= 1, column=0, padx= 2, pady=2)

entry1 = tk.Entry(window)
entry1.grid(row=0, column=1,padx=2, pady=2)

entry2 = tk.Entry(window)
entry2.grid(row=1, column=1, padx=2, pady=2)

window.mainloop()

### column --  KOLUMNA, DOMYSLNIE 0, CZULI LEWA KOLUMNA
#   row --  WIERSZ DOMYUSLNIE 0, CZYLI NA GORZE 
#   padx i pady --  DOPELNIENIE W OSI X I Y NA OKOLO WIDGETA
#   ipadx, ipady -- DOPELNIENIE WEWNATRZ 
#   columnspan -- ile kolumn zajmuje widget domyslnie 1 
#    rowspan --  ile wierszy zajmuje widget domyslnie 1 ###