import tkinter as tk
import tkinter.colorchooser as cc

root = tk.Tk()
root.geometry("250x200")
root.title("Выбор цвета")

def choose_color():
    color = cc.askcolor()[1]  
    color_label.config(text=f"Вы выбрали цвет {color}")  
    second_label.config(bg=color)  

color_button = tk.Button(root, text="Выбрать цвет", command=choose_color)
color_label = tk.Label(root, text="Нажмите кнопку, чтобы выбрать цвет")
second_label = tk.Label(root, text="\t\t\t\n\t\t\t")
color_button.pack(pady=10)
color_label.pack()
second_label.pack(pady=10)

root.mainloop()