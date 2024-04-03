import tkinter as tk

window = tk.Tk()

password_placeholder = "hdgeGH123"
username_placeholder = "Ziah12"

lbl_home = tk.Label(text="Login form")
lbl_home.pack()

lbl_login_username = tk.Label(text="Enter your username")
txt_login_username = tk.Entry() 

lbl_login_password = tk.Label(text="Enter your password")
txt_login_password = tk.Entry() 

lbl_login_username.pack()
txt_login_username.pack()

lbl_login_password.pack()
txt_login_password.pack()

window.mainloop()