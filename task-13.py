from tkinter import *

window = Tk() # Создаём объект класса Tk()

window.title('Первое графическое приложение') # Меняем название приложения
window.iconbitmap('python-for-all.ico') # Меняем логотип приложения
window.geometry('600x400+700+400') # Размеры и начальное расположение приложения
window.resizable(False, False) # Фиксируем размеры приложения
window.config(bg='grey') # Меняем цвет фона приложения

def hello():
	print('Привет!')

def entry_get():
	label_entry_get['text'] = f'Ваше число: {entry_1.get()}'

def clear():
	entry_1.delete(0, END)		

frame_1 = Frame(window)
frame_2 = Frame(window)

# button_1 = Button(window, text = 'Кнопка 1', command = hello, width = 10, height = 2, bd = 10, font = 'Arial 10 bold')
button_1 = Button(frame_1, text = 'Кнопка 1', padx = 5, pady = 5, bd = 10, activebackground = 'yellow', activeforeground = 'orange', bg = 'green', fg = 'white')

button_2 = Button(frame_1)
button_2.config(text = 'Кнопка 2', padx = 5, pady = 5, bd = 10, activebackground = 'yellow', activeforeground = 'orange', bg = 'green', fg = 'white')

button_3 = Button(frame_2)
button_3['text'] = 'Кнопка 3'
button_3['padx'] = 5
button_3['pady'] = 5
button_3['bd'] = 10

button_4 = Button(frame_2)
button_4['text'] = 'Кнопка 4'
button_4['padx'] = 5
button_4['pady'] = 5
button_4['bd'] = 10

label_1 = Label(window, text = 'Это виджет Label!', bg = 'green', fg ='white', font = '"Comic Sans MS" 15 bold')
label_img = PhotoImage(file = 'label-image.png')
label_2 = Label(window, image = label_img)

# Виджет Entry
frame_entry = Frame(window)
label_entry = Label(frame_entry, text = 'Поле ввода:')
entry_1 = Entry(frame_entry, bd = 5)
entry_1.insert(0, 'Введите ваше число: ')
button_entry = Button(frame_entry, text = 'Принять', bd = 5, command = entry_get)
button_clear = Button(frame_entry, text = 'Очистить', bd = 5, command = clear)

label_entry.pack(side = LEFT)
entry_1.pack(side = LEFT, padx = 5)
button_entry.pack(side = LEFT)
button_clear.pack(side = LEFT)

label_entry_get = Label(window, text = 'Ваше число: ', bg = 'green', fg = 'white')

frame_1.pack()
frame_2.pack()
button_1.pack(side = LEFT, padx = 5, pady = 5)
button_2.pack(side = LEFT, padx = 5, pady = 5)
button_3.pack(side = LEFT, padx = 5, pady = 5)
button_4.pack(side = LEFT, padx = 5, pady = 5)
label_1.pack()
label_2.pack()
frame_entry.pack()
label_entry_get.pack()

window.mainloop()