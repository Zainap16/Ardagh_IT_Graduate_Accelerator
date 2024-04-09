import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
password_placeholder = "123"
username_placeholder = "Z"

def show_error():
    messagebox.showerror("Error","Incorrect/Invalid username and or password")

def submit_info():
        if username_placeholder == txt_login_username.get() and     txt_login_password.get() == password_placeholder:
            
            messagebox.showinfo("Information", "Login Successful")
        else:
            show_error()



lbl_home = tk.Label(text="Login form")
lbl_home.pack()

lbl_login_username = tk.Label(text="Enter your username")
txt_login_username = tk.Entry() 

lbl_login_password = tk.Label(text="Enter your password")
txt_login_password = tk.Entry() 

btn_submit = tk.Button(text="Submit", command=submit_info)

lbl_login_username.pack()
txt_login_username.pack()

lbl_login_password.pack()
txt_login_password.pack()

btn_submit.pack()
    
    
    

window.mainloop()