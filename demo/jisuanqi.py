import tkinter as tk

def on_click(event):
    text = event.widget["text"]

    if text == "=":
        try:
            expression = entry.get()
            result = str(eval(expression))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

def on_key(event):
    key = event.keysym

    if key in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
        entry.insert(tk.END, key)
    elif key == "plus":
        entry.insert(tk.END, "+")
    elif key == "minus":
        entry.insert(tk.END, "-")
    elif key == "asterisk":
        entry.insert(tk.END, "*")
    elif key == "slash":
        entry.insert(tk.END, "/")
    elif key == "Return":  # Change this line to handle the Enter key
        try:
            expression = entry.get()
            result = str(eval(expression))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")




root = tk.Tk()
root.title("简单计算器")

entry = tk.Entry(root, font=("Helvetica", 20))
entry.pack(fill=tk.BOTH, expand=True)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

row, col = 0, 0
for button_text in buttons:
    button = tk.Button(button_frame, text=button_text, font=("Helvetica", 20), width=3, height=2)
    button.grid(row=row, column=col, padx=5, pady=5)
    button.bind("<Button-1>", on_click)

    col += 1
    if col > 3:
        col = 0
        row += 1

root.bind("<Key>", on_key)

root.mainloop()
