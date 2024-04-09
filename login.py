import tkinter as tk
from tkinter import messagebox

def login():
    entered_name = name_entry.get()
    entered_password = password_entry.get()
    
    try:
        with open('user_credentials.txt', 'r') as file:
            for line in file:
                name, password = line.strip().split(',')
                if name == entered_name and password == entered_password:
                    messagebox.showinfo("Information","Login Successful")
                    return
        messagebox.showerror("Error", "Invalid credentials. Please try again.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


root = tk.Tk()
root.title("Login")

#create labels and input
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=5)
password_entry = tk.Entry(root, show="*") 
password_entry.grid(row=1, column=1, padx=10, pady=5)

#create login button
login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=2, columnspan=2, padx=10, pady=5)


root.mainloop()
