from tkinter import *

root = Tk()

mylbl_1= Label(root, text="Hello World 1")
mylbl_2 = Label(root, text="Hello World 2")

mylbl_3= Label(root, text="Hello World 3")
mylbl_4 = Label(root, text="Hello World 4")

mylbl_1.grid(row=0,column=0)
mylbl_2.grid(row=1,column=0)

mylbl_3.grid(row=0,column=1)
mylbl_4.grid(row=1,column=1)

root.mainloop()










