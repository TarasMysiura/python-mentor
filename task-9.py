from tkinter import *
import random


def randomHexColor():
    hexaColor = ["#" + "".join([random.choice("ABCDEF0123456789") for i in range(6)])]
    return hexaColor

def change():
    b1['text'] = "Кнопка змінена"
    b1['bg'] = '#0e7be8'
    b1['activebackground'] = '#d6aded'
    b1['fg'] = '#cc1890'
    b1['activeforeground'] = '#cc1818'

My_window = Tk()
My_window.title("Welcome")
My_window.geometry("500x500+510+290")
My_window["bg"] = randomHexColor()

b1=Button(text='Зміни колір',    #текст кнопки
          background='#006400',   #фоновий колір кнопки
          foreground='#FF8C00',   #колір тексту
          padx='20',              #відступ від межі до змісту по горизонталі
          pady='8',               #відступ від межі до змісту по вертикалі
          font='18',              #висота шрифту
          width='10',
          height='4',
          )
# b1.grid(column=4, row=4)
# b1.pack(side=TOP)

# for i in range(10):
#     b1.config(command=randomHexColor())
#     My_window["bg"] = randomHexColor()
    
b1.pack(expand=True)

My_window.mainloop()

# =======================================
# import tkinter as tk
# import time

# def questionQuery():
#     root.update_idletasks()
#     time.sleep(2)
#     btn.configure(text='Done')

# root = tk.Tk()
# btn = tk.Button(root, activebackground='red', text="Press me", command=questionQuery)
# btn.pack()

# root.mainloop()

# ==========================================
# from tkinter import*


# root=Tk()
# root.title("KILL YOURSELF")
# root.geometry('400x500')
# b1=Button(text='KILL YOURSELF',
#     background= '#FF0000',
#     foreground= '#F08080',
#     padx='20',
#     pady='8',
#     font="16",
#     # highlightcolor='#FFA07A'
#     height='5',
#     width='10',
#     # activebackground='#FA8072',
#     # activeforeground='#FF0000'
#     )


# b1.pack()










# root.mainloop()