import tkinter as tk 


window = tk.Tk()
button= tk.Button(
    window,
    text="QUIT",
    bd=15,
    fg="blue",
    bg="yellow",
    justify=tk.LEFT,
    activeforeground="black",
    activebackground="Silver",
    command=quit,
    font="Time 16 bold italic",
    width=5,
    height=3,
    padx=20,
    pady=7,
    relief="groove"
)
button.pack()
window.mainloop()