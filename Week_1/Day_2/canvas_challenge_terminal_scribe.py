import tkinter as tk

# setup
window = tk.Tk()
window.geometry('600x400')
window.title('Canvas')

# canvas
canvas = tk.Canvas(window, bg = "blue")
canvas.pack()

            # left,top,right,bottom
canvas.create_rectangle((50,20,100,200), fill = 'black')

# run
window.mainloop()
