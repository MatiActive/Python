import tkinter as tk
import os
scriptDir = os.path.dirname(__file__)
os.chdir(scriptDir)
window = tk.Tk()
bg = tk.PhotoImage(file="img.png")
window.title("Test App")

label1 = tk.Label(
    text= "Linyx",
    font = "Helvetica 16 bold italic underline",
    compound=tk.CENTER,
    master= window,
    image= bg,
    width=500,
    height= 500
)


label1.pack()
label1.config(text="Linux")
window.mainloop()
