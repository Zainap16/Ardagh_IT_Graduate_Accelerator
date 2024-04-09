import tkinter as tk
from tkinter import messagebox

def save_credentials():
    user_name = name_entry.get()
    user_password = password_entry.get()
    
    if user_name and user_password:
        try:
            with open('user_credentials.txt', 'a') as file:
                file.write(f"{user_name},{user_password}\n")
            messagebox.showinfo("Success", "Credentials saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showwarning("Warning", "Please enter both name and password.")

# create main window
root = tk.Tk()
root.title("Registration")

#create labels and inputs
name_label = tk.Label(root, text="Enter your username:")
name_label.pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

password_label = tk.Label(root, text="Enter your password:")
password_label.pack(pady=5)
password_entry = tk.Entry(root, show="*")  # Masking password input
password_entry.pack(pady=5)

#create button to save credentials
save_button = tk.Button(root, text="Submit", command=save_credentials)
save_button.pack(pady=5)

root.mainloop()
