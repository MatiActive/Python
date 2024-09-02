# Metoda place() - umieszcza elementy dokladnie w wskazanym miejscu 

import tkinter as tk 

window = tk.Tk()

l1= tk.Label(window, text="Text 1", bg= "white")
l1.place(x=10, y=10)

l2 = tk.Label(window, text="Text 2", bg = "red")
l2.place(x=100, y=10, height=50, width=80)

entry = tk.Entry(window)
entry.place(x=70, y=100)

window.mainloop()