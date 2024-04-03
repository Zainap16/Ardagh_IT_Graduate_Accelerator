import tkinter as tk
import subprocess

def open_register():
    subprocess.Popen(["python","register.py"])
    window.destroy()

def open_login():
    subprocess.Popen(["python","login.py"])
    window.destroy()
    

window = tk.Tk()

lbl_home = tk.Label(text="Register or Login")
lbl_home.pack()

btn_register = tk.Button(text="Register", command=open_register)
btn_login = tk.Button(text="Login",command=open_login)

btn_login.pack()
btn_register.pack()



window.mainloop()