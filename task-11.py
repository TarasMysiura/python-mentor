from tkinter import *
from decimal import *


my_calc = Tk()
my_calc.title("Калькулятор")
my_calc.iconbitmap(default="favicon_calc.ico")
my_calc.config(bg="red")
my_calc.config(cursor="star")


# Отримуємо ширину и висоту екрану
screen_width = my_calc.winfo_screenwidth()
screen_height = my_calc.winfo_screenheight()
# print(screen_width, screen_height)

# Визначаємо координати вікна додатку
window_width = 510
window_height = 400
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
my_calc.geometry(f"{window_width}x{window_height}+{x}+{y}")

font_btn = ("Times", "30", "bold")
font_entry_text = ("Times", "25", "bold")

width_btn = int(window_width / 150)
height_btn = int(window_height / 250)
width_entry_text = width_btn * 6 + 5

# запа, какое число записано в поле введення
# початково це нуль
number = Decimal(0)
# а це попереднє число в памяті - и також спочатку нуль
previous_number = 0


# параметр - вибрана дія
# def make_action(chosen_action):
#     global number
#     global previous_number
#     global action
#     # запамятовуємо вибрану дію
#     action = chosen_action
#     # запамятовуємо поточне число
#     previous_number = number
#     # і задаємо нуль, або пустий рядок в поточне - користувачу потрібно його ввести
#     number = 0
#     # показуємо поточне значення на екрані
#     entry_text.set(str(number))


# функція для додавання
def button_press_add():
    # вибранна дія - це додавання
    # make_action("+")
    global number
    global previous_number
    global action
    # запамятовуємо вибрану дію
    action = "+"
    # запамятовуємо поточне число
    previous_number = number
    # і задаємо нуль, або пустий рядок в поточне - користувачу потрібно його ввести
    number = 0
    # показуємо поточне значення на екрані
    entry_text.set("")


# def button_press_add():
#     # вибранна дія - це додавання
#     make_action("+")
#     # global number
#     # global previous_number
#     # global action
#     # # запамятовуємо вибрану дію
#     # action = "+"
#     # # запамятовуємо поточне число
#     # previous_number = number
#     # # і задаємо нуль, або пустий рядок в поточне - користувачу потрібно його ввести
#     # number = 0
#     # # показуємо поточне значення на екрані
#     # entry_text.set("")


# функція для віднімання
def button_press_substract():
    # вибранна дія - це віднімання
    # make_action("-")
    global number
    global previous_number
    global action
    # запамятовуємо вибрану дію
    action = "-"
    # запамятовуємо поточне число
    previous_number = number
    # і задаємо нуль, або пустий рядок в поточне - користувачу потрібно його ввести
    number = 0
    # показуємо поточне значення на екрані
    entry_text.set("")


# функція для множення
def button_press_multiply():
    # вибранна дія - це множення
    # make_action("*")
    global number
    global previous_number
    global action
    # запамятовуємо вибрану дію
    action = "*"
    # запамятовуємо поточне число
    previous_number = number
    # і задаємо нуль, або пустий рядок в поточне - користувачу потрібно його ввести
    number = 0
    # показуємо поточне значення на екрані
    entry_text.set("")


# функція для ділення
def button_press_divide():
    # вибранна дія - це ділення
    # make_action("/")
    global number
    global previous_number
    global action
    # запамятовуємо вибрану дію
    action = "/"
    # запамятовуємо поточне число
    previous_number = number
    # і задаємо нуль, або пустий рядок в поточне - користувачу потрібно його ввести
    number = 0
    # показуємо поточне значення на екрані
    entry_text.set("")


def button_press_divide_by_whole():
    global number
    global previous_number
    global action
    action = "//"
    # запамятовуємо поточне число
    previous_number = number
    # і задаємо нуль, або пустий рядок в поточне - користувачу потрібно його ввести
    number = 0
    # показуємо поточне значення на екрані
    entry_text.set("")


def button_press_fraction_from_divide_by_whole():
    global number
    global previous_number
    global action
    action = "%"
    # запамятовуємо поточне число
    previous_number = number
    # і задаємо нуль, або пустий рядок в поточне - користувачу потрібно його ввести
    number = 0
    # показуємо поточне значення на екрані
    entry_text.set("")


def button_press_sqrt():
    global number
    global previous_number
    global action
    action = "√"
    # запамятовуємо поточне число
    # previous_number = number
    number = number**0.5
    # і задаємо нуль, або пустий рядок в поточне - користувачу потрібно його ввести
    # number = 0
    # показуємо поточне значення на екрані
    entry_text.set(number)


# # функция для вычитания
# def button_press_substract():
#     # выбранное действие - это сложение
#     make_action('-')

# # функция для умножения
# def button_press_multiply():
#     make_action('*')

# # функция для деления
# def button_press_divide():
#     make_action('/')


# функция для очистки (AC)
def button_press_clear():
    global number
    global previous_number
    number = 0
    previous_number = 0
    entry_text.set(number)


def button_press_delete_last_symbol():
    global number
    if number >= 0:
        number = number // 10
    else:
        number = -number // 10
        number = -number

    entry_text.set(number)


def button_press_plus_minus():
    global number
    number = number * (-1)
    entry_text.set(number)


# функція для розрахунку результата (=)
def button_press_result():
    global number
    global previous_number
    global action
    # в залежності від action - виконуємо арифметичні операції!
    if action == "+":
        number = previous_number + number
    elif action == "-":
        number = previous_number - number
    elif action == "*":
        number = previous_number * number
    elif action == "/":
        number = previous_number / number
    elif action == "//":
        number = previous_number // number
    elif action == "%":
        number = previous_number % number
    # записуємо відповідь у поле введення
    entry_text.set(number)

def add_digit(digit):
     global activeStr
     global Stack
 
     if text == 'CE':
          Stack.clear()
          activeStr = ' '
          label.configure(text = '0')
 
     elif '0' <= text <= '9':
          activeStr += text
          label.configure(text = activeStr)
 
     elif text == '.':
          if activeStr.find('.') == -1:
               activeStr += text
               label.configure(text = activeStr)
 
     else:
          if len(Stack) >= 2:
               Stack.append(label['text'])
               Calculate()
               Stack.clear()
               Stack.append(label['text'])
               activeStr = ' '
               if text != '=':
                    Stack.append(text)
          else:
               if text != '=':
                    Stack.append(label['text'])
                    Stack.append(text)
                    activeStr = ' '
                    label.configure(text = '0')
 



# def add_digit(digit):
#     global number
#     # global string_number
#     if digit == ".":
#         number = float(number)

#         entry_text.set(number)
#         return number
#     n = len(str(number).split(".")[1])

#     # if type(number) != float:
#     #     if number >= 0:
#     #         number = number * 10 + digit
#     #     else:
#     #         number = number * 10 - digit
#     # else:
#     #     # n = len(str(number).split(".")[1]) + 1
#     #     string_number = str(number)
#     #     # print(n)
#     #     print(string_number)

#     # if number >= 0:
#     #     number = number + digit / (10 ** (n))
#     # else:
#     #     number = number - digit / (10 ** (n))
#     number = number + digit / (10 ** (n))
#     string_number = str(number )
    
#     if string_number.find(".") == -1:
#         number = int(string_number)
#     else:
#         number = float(string_number)
#     entry_text.set(string_number)


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


def button_press_point():
    add_digit(".")


Button(
    my_calc,
    text="1",
    font=font_btn,
    height=height_btn,
    width=width_btn,
    command=button_press_1,
    # cursor=True,
    # padx=1,
    # pady=1,
    # bd=7,
    # activebackground="light gray",
    # activeforeground="gray",
    # bg="green",
    # fg="white",
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

Button(
    my_calc,
    text="=",
    font=font_btn,
    height=height_btn,
    width=width_btn,
    command=button_press_result,
).grid(row=4, column=0)
Button(
    my_calc,
    text=".",
    font=font_btn,
    height=height_btn,
    width=width_btn,
    command=button_press_point,
).grid(row=4, column=2)
Button(
    my_calc,
    text="AC",
    font=font_btn,
    height=height_btn,
    width=width_btn,
    command=button_press_clear,
).grid(row=1, column=5)
Button(
    my_calc,
    text="+",
    font=font_btn,
    height=height_btn,
    width=width_btn,
    command=button_press_add,
).grid(row=1, column=3)
Button(
    my_calc,
    text="-",
    font=font_btn,
    height=height_btn,
    width=width_btn,
    command=button_press_substract,
).grid(row=2, column=3)
Button(
    my_calc,
    text="*",
    font=font_btn,
    height=height_btn,
    width=width_btn,
    command=button_press_multiply,
).grid(row=3, column=3)
Button(
    my_calc,
    text="/",
    font=font_btn,
    height=height_btn,
    width=width_btn,
    command=button_press_divide,
).grid(row=4, column=3)
Button(
    my_calc,
    text="⬅",
    font=font_btn,
    height=height_btn,
    width=width_btn,
    command=button_press_delete_last_symbol,
).grid(row=4, column=5)
Button(
    my_calc,
    text="◀",
    font=font_btn,
    height=height_btn,
    width=width_btn,
    # command=button_press_return,
).grid(row=3, column=5)
Button(
    my_calc,
    text="▶",
    font=font_btn,
    height=height_btn,
    width=width_btn,
    # command=button_press_return,
).grid(row=2, column=5)
# Button(
#     my_calc,
#     text="",
#     font=font_btn,
#     height=height_btn,
#     width=width_btn,
#     # command=button_press_return,
# ).grid(row=1, column=5)


Button(
    my_calc,
    text="//",
    font=font_btn,
    height=height_btn,
    width=width_btn,
    command=button_press_divide_by_whole,
).grid(row=1, column=4)
Button(
    my_calc,
    text="%",
    font=font_btn,
    height=height_btn,
    width=width_btn,
    command=button_press_fraction_from_divide_by_whole,
).grid(row=2, column=4)
Button(
    my_calc,
    text="√",
    font=font_btn,
    height=height_btn,
    width=width_btn,
    command=button_press_sqrt,
).grid(row=4, column=4)
Button(
    my_calc,
    text="+/-",
    font=font_btn,
    height=height_btn,
    width=width_btn,
    command=button_press_plus_minus,
).grid(row=3, column=4)

entry_text = StringVar()
Entry(
    my_calc, width=width_entry_text, textvariable=entry_text, font=font_entry_text
).grid(row=0, column=0, columnspan=6)

mainloop()
