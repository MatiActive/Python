import tkinter as tk 

def button():
    print("button clicked!!!")
    quit()

window1 = tk.Tk()
window1.title("Button app")
button = tk.Button(window1,
    text="KONIEC",
    bd=10,
    fg="black",
    bg="yellow",
    activeforeground="white",
    activebackground="red",
    font="Time 16 bold",
    height=3,
    width=7,
    padx=50,
    pady=10,
    relief="sunken",
    command= button

)
button.pack()
window1.mainloop()