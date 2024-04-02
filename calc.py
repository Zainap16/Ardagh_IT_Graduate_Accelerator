import tkinter as tk

def button_click(value):
    current = entry_display.get()
    entry_display.delete(0, tk.END)
    entry_display.insert(tk.END, current + value)

def clear():
    entry_display.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry_display.get())
        entry_display.delete(0, tk.END)
        entry_display.insert(tk.END, str(result))
    except Exception as e:
        entry_display.delete(0, tk.END)
        entry_display.insert(tk.END, "Error")

root = tk.Tk()
root.title("Basic Calculator")

entry_display = tk.Entry(root, width=30, font=('Arial', 14))
entry_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14),
                       command=lambda t=text: button_click(t) if t != '=' else calculate() if t != 'C' else clear())
    button.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
