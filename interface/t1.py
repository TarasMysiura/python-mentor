# =========Task 1=========

# from tkinter import*
# root=Tk()
# root.title('Вікно №1')
# root.geometry('500x500')
# root["bg"]="#31B404"

# b1=Button(text='Перша кнопка',    #текст кнопки
#           background='#006400',   #фоновий колір кнопки
#           foreground='#FF8C00',   #колір тексту
#           padx='20',              #відступ від межі до змісту по горизонталі
#           pady='8',               #відступ від межі до змісту по вертикалі
#           font='18',               #висота шрифту
#           width='10',
#           height='4',
#           )

# b1.pack()
# root.mainloop()

# =========Task 2=========
# from tkinter import*
# root=Tk()
# root.title('Вікно №1')
# root.geometry('500x700')
# root["bg"]="#31B404"

# b1=Button(text='Перша кнопка',    #текст кнопки
#           background='#006400',   #фоновий колір кнопки
#           foreground='#FF8C00',   #колір тексту
#           padx='20',              #відступ від межі до змісту по горизонталі
#           pady='8',               #відступ від межі до змісту по вертикалі
#           font='18',               #висота шрифту
#           width='10',
#           height='4',
#           )
# def change():
#     b1['text'] = "Кнопка змінена"
#     b1['bg'] = '#0e7be8'
#     b1['activebackground'] = '#d6aded'
#     b1['fg'] = '#cc1890'
#     b1['activeforeground'] = '#cc1818'
 
# b1.config(command=change)



# b1.pack()
# root.mainloop()


# =========Task 3=========

from tkinter import*
from tkinter import messagebox
def change(event):
    Window.geometry('400x300')
    Window['bg']='green'
    messagebox.showinfo('Повідомлення','Python')
Window=Tk()
Window.bind('<Double-Button-1>',change)
b1=Button(text='Перша кнопка',    #текст кнопки
          background='#006400',   #фоновий колір кнопки
          foreground='#FF8C00',   #колір тексту
          padx='20',              #відступ від межі до змісту по горизонталі
          pady='8',               #відступ від межі до змісту по вертикалі
          font='18',               #висота шрифту
          width='10',
          height='4',
          )
def change():
    b1['text'] = "Кнопка змінена"
    b1['bg'] = '#0e7be8'
    b1['activebackground'] = '#d6aded'
    b1['fg'] = '#cc1890'
    b1['activeforeground'] = '#cc1818'
 
b1.config(command=change)
b1.pack()
Window.mainloop()