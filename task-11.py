from tkinter import *

my_calc = Tk()
my_calc.title("Калькулятор")

# Получаем ширину и высоту экрана
screen_width = my_calc.winfo_screenwidth()
screen_height = my_calc.winfo_screenheight()
# print(screen_width, screen_height)

# Вычисляем координаты окна приложения
window_width = 500
window_height = 400
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
my_calc.geometry(f"{window_width}x{window_height}+{x}+{y}")
font_btn = ("Times", "30", "bold")
font_entry_text = ("Times", "30", "bold")

width_btn = int(window_width / 125)
height_btn = int(window_height / 250)

#  запомним, какое число записано в поле ввода
# изначально это ноль
number = 0


def add_digit(digit):  # функция для ввода цифры
    global number  # чтобы менять глобальную переменную, пишем global
    number = number * 10 + digit  # допишем нужную цифру справа
    entry_text.set(number)  # запишемо число в поле введення


def button_press_1():
    add_digit(1)


def button_press_2():
    add_digit(2)


def button_press_3():
    add_digit(3)


def button_press_4():
    add_digit(4)


def button_press_5():
    add_digit(5)


def button_press_6():
    add_digit(6)


def button_press_7():
    add_digit(7)


def button_press_8():
    add_digit(8)


def button_press_9():
    add_digit(9)


def button_press_0():
    add_digit(0)


Button(
    my_calc,
    text="1",
    font=font_btn,
    height=height_btn,
    width=width_btn,
    command=button_press_1,
).grid(row=3, column=0)
Button(
    my_calc,
    text="2",
    font=font_btn,
    height=height_btn,
    width=width_btn,
    command=button_press_2,
).grid(row=3, column=1)
Button(
    my_calc,
    text="3",
    font=font_btn,
    height=height_btn,
    width=width_btn,
    command=button_press_3,
).grid(row=3, column=2)
Button(
    my_calc,
    text="4",
    font=font_btn,
    height=height_btn,
    width=width_btn,
    command=button_press_4,
).grid(row=2, column=0)
Button(
    my_calc,
    text="5",
    font=font_btn,
    height=height_btn,
    width=width_btn,
    command=button_press_5,
).grid(row=2, column=1)
Button(
    my_calc,
    text="6",
    font=font_btn,
    height=height_btn,
    width=width_btn,
    command=button_press_6,
).grid(row=2, column=2)
Button(
    my_calc,
    text="7",
    font=font_btn,
    height=height_btn,
    width=width_btn,
    command=button_press_7,
).grid(row=1, column=0)
Button(
    my_calc,
    text="8",
    font=font_btn,
    height=height_btn,
    width=width_btn,
    command=button_press_8,
).grid(row=1, column=1)
Button(
    my_calc,
    text="9",
    font=font_btn,
    height=height_btn,
    width=width_btn,
    command=button_press_9,
).grid(row=1, column=2)
Button(
    my_calc,
    text="0",
    font=font_btn,
    height=height_btn,
    width=width_btn,
    command=button_press_0,
).grid(row=4, column=1)

Button(my_calc, text="=", font=font_btn, height=height_btn, width=width_btn).grid(
    row=4, column=0
)
Button(my_calc, text="AC", font=font_btn, height=height_btn, width=width_btn).grid(
    row=4, column=2
)

Button(my_calc, text="+", font=font_btn, height=height_btn, width=width_btn).grid(
    row=1, column=3
)
Button(my_calc, text="-", font=font_btn, height=height_btn, width=width_btn).grid(
    row=2, column=3
)
Button(my_calc, text="*", font=font_btn, height=height_btn, width=width_btn).grid(
    row=3, column=3
)
Button(my_calc, text="/", font=font_btn, height=height_btn, width=width_btn).grid(
    row=4, column=3
)

Button(my_calc, text="//", font=font_btn, height=height_btn, width=width_btn).grid(
    row=1, column=4
)
Button(my_calc, text="%", font=font_btn, height=height_btn, width=width_btn).grid(
    row=2, column=4
)
Button(my_calc, text="+/-", font=font_btn, height=height_btn, width=width_btn).grid(
    row=3, column=4
)
Button(my_calc, text="Sqrt", font=font_btn, height=height_btn, width=width_btn).grid(
    row=4, column=4
)

entry_text = StringVar()
Entry(my_calc, width=width_btn * 5, textvariable=entry_text, font=font_entry_text).grid(
    row=0, column=0, columnspan=5
)

mainloop()
