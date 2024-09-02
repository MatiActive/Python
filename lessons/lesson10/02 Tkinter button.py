import tkinter as tk
#  --------BUTTON----------
window =tk.Tk()
button = tk.Button(
    text="Quit",
    bd=20,  # BORDER IN PIXELS
    bg="green",  # BACKGROUND COLOR
    fg="red",  # TEKST COLOR
    command=quit, # FUNCTION WHEN CLICKED
    activeforeground="White", # UNDER CURSOR
    activebackground="Silver", #  UNDER CURSOR
    font="Helvetica 16 bold italic underline",
    height=4, # TEXT LINES HEIGHT 
    justify=tk.CENTER,
    padx=10, # PADDING LEFT AND RIGHT TO THE TEXT
    pady=10, # PADDING ABOVE AND BLOW THE TEXT 
    relief="groove", # BORDER : sunken, raised, groove, ridge
)
button.pack()
window.mainloop()

#  DODATKOWE OPCJONALNE ARGUMENTY : 
#  state - DISABLED, ACTIVE, NORMAL

#  wraplenght - DODATNIA WARTOŚĆ OKREŚLA,A ŻE TEKST BĘDZIE ZAWIJANY ABY ZMIEŚCIĆ SIE W TEJ SZEROKOŚCI
#  width  - DŁUGOŚĆ PRZYCISKU W ILOŚCI ZNAKÓW JEŚLI TEKST PISKELE JEŚLI OBRAZEK

# Image - OBRAZEK DO WYŚWIETLENIA