import tkinter as tk

def button_click(symbol):
    current = display_var.get()
    if current == "Error":
        clear_display()
    if symbol == "C":
        clear_display()
    elif symbol == "=":
        try:
            result = eval(current)
            display_var.set(str(result))
        except Exception as e:
            display_var.set("Error")
    else:
        display_var.set(current + symbol)

def clear_display():
    display_var.set("")

root = tk.Tk()
root.title("Calculator")
root.configure(bg="#393E46")

# Style for the Entry widget
entry_style = {"font": ("Arial", 24), "bd": 10, "insertwidth": 4, "width": 14, "justify": "right", "bg": "#222831", "fg": "#EEEEEE"}

display_var = tk.StringVar()
display = tk.Entry(root, textvariable=display_var, **entry_style)
display.grid(row=0, column=0, columnspan=4, pady=10)

buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

# Style for the Buttons
button_style = {"font": ("Arial", 14), "padx": 20, "pady": 20, "bg": "#00ADB5", "fg": "#EEEEEE", "bd": 0}

# Create buttons in a grid
for i in range(4):
    for j in range(4):
        symbol = buttons[i][j]
        btn = tk.Button(root, text=symbol, command=lambda symbol=symbol: button_click(symbol), **button_style)
        btn.grid(row=i+1, column=j, padx=5, pady=5, sticky="nsew")  # sticky="nsew" to expand buttons in all directions

# Configure grid to expand with window resizing
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
