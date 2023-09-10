import tkinter as tk


def func():
    if b["state"] == tk.NORMAL:
        b.config(state=tk.DISABLED, bg="red")
    else:
        b.config(state=tk.NORMAL, bg="green")


root = tk.Tk()
button = tk.Button(text='Кнопощка', state=tk.DISABLED, font="Courier 20")
button.pack()
b = tk.Button(text="Активировать", command=func)
b.pack()
root.mainloop()