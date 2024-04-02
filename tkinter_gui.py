import tkinter as tk

window = tk.Tk()

frm_1 = tk.Frame(window)
lbl_result  = tk.Label(master=frm_1,text= "placeholder",height= 5, width= 10)

frm_2 = tk.Frame(window)
btn_one = tk.Button(frm_2,text="1",width=5)

btn_one.pack()
frm_1.pack()
frm_2.pack()
lbl_result.pack()

window.mainloop()
