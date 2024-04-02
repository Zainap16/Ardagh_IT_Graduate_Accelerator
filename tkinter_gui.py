import tkinter as tk

window = tk.Tk()

# window.geometry("500x500")
# window.title("Basic Calculator")

# textbox = tk.Text(window, height = 3,font=("Arial", 18))
# textbox.pack(padx = 20, pady = 20)
greeting = tk.Label(text="Hello, Tkinter")
greeting.pack() # add to window 

window.mainloop()
