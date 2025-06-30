import tkinter as tk


root = tk.Tk()
root.title("Dark Theme Calculator")
root.geometry("320x460")
root.configure(bg="#1e1e1e")
root.resizable(False, False)


entry = tk.Entry(root, font=("Segoe UI", 24), bg="#252526", fg="#ffffff", bd=0, justify="right", insertbackground="white")
entry.grid(row=0, column=0, columnspan=4, padx=20, pady=20, ipadx=8, ipady=15, sticky="nsew")


def click(char):
    if char == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif char == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, char)


btn_style = {
    "font": ("Segoe UI", 16),
    "width": 5,
    "height": 2,
    "bd": 0,
    "bg": "#333333",
    "fg": "#ffffff",
    "activebackground": "#555555",
    "activeforeground": "#ffffff",
}


buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]


for r, row in enumerate(buttons):
    for c, char in enumerate(row):
        button = tk.Button(root, text=char, command=lambda ch=char: click(ch), **btn_style)
        button.grid(row=r+1, column=c, padx=10, pady=10)


for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)


root.mainloop()
