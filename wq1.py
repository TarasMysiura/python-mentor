from tkinter import *

root = Tk()
root.title("Calculator")


def tastare_1():
    linie_date.insert(END, "1")


def tastare_2():
    linie_date.insert(END, "2")


def tastare_3():
    linie_date.insert(END, "3")


def tastare_4():
    linie_date.insert(END, "4")


def tastare_5():
    linie_date.insert(END, "5")


def tastare_6():
    linie_date.insert(END, "6")


def tastare_7():
    linie_date.insert(END, "7")


def tastare_8():
    linie_date.insert(END, "8")


def tastare_9():
    linie_date.insert(END, "9")


def tastare_0():
    linie_date.insert(END, "0")


def tastare_plus():
    linie_date.insert(END, "+")


def tastare_minus():
    linie_date.insert(END, "-")


def tastare_imult():
    linie_date.insert(END, "*")


def tastare_impart():
    linie_date.insert(END, "/")


def tastare_putere():
    linie_date.insert(END, "^")


def tastare_rest():
    linie_date.insert(END, "%")


def stergere():
    linie_date.delete(0, END)


def calculare(semn):
    list_arg = linie_date.get().split(semn)
    arg1 = int(list_arg[0])
    arg2 = int(list_arg[1])

    if semn == "+":
        rezult = arg1 + arg2
        date = f"{arg1}+{arg2} = {rezult}"
        linie_date.delete(0, END)
        linie_date.insert(0, date)

    if semn == "-":
        rezult = arg1 - arg2
        date = f"{arg1}-{arg2} = {rezult}"
        linie_date.delete(0, END)
        linie_date.insert(0, date)

    if semn == "*":
        rezult = arg1 * arg2
        date = f"{arg1}*{arg2} = {rezult}"
        linie_date.delete(0, END)
        linie_date.insert(0, date)

    if semn == "/":
        if arg2 != 0:
            rezult = arg1 / arg2
            date = f"{arg1}/{arg2} = {rezult}"
        else:
            date = "Eroare: Impărțirea la 0"
            linie_date.delete(0, END)
            linie_date.insert(0, date)

    if semn == "%":
        if arg2 != 0:
            rezult = arg1 % arg2
            date = f"{arg1}%{arg2} = {rezult}"
        else:
            date = "Eroare: Impărțirea la 0"
        linie_date.delete(0, END)
        linie_date.insert(0, date)

    if semn == "^":
        rezult = arg1**arg2
        date = f"{arg1} ^ {arg2} = {rezult}"
        linie_date.delete(0, END)
        linie_date.insert(0, date)

    with open("Istorie.txt" "a") as f:
        f.write(date + "\n")


def afisarea_rezultat():
    operatie = linie_date.get()

    try:
        if "+" in operatie:
            calculare("+")

        elif "-" in operatie:
            calculare("-")

        elif "*" in operatie:
            calculare("*")

        elif "/" in operatie:
            calculare("/")

        elif "%" in operatie:
            calculare("%")

        else:
            linie_date.delete(0, END)
            linie_date.insert(0, "Eroare: expresia  greșită")

    except:
        linie_date.delete(0, END)
        linie_date.insert(0, "Eroare: expresia  greșită")


antet = Label(root, text="Calculator matematic")
antet.grid(row=0, column=0, columnspan=4, sticky="nsew", pady=3, padx=3)

linie_date = Entry(root)
linie_date.grid(row=1, column=0, columnspan=4, sticky="nsew", pady=3, padx=3)

buton_1 = Button(root, text="1", width=7, height=2, command=tastare_1)
buton_1.grid(row=2, column=0, pady=3, padx=3)

buton_2 = Button(root, text="2", width=7, height=2, command=tastare_2)
buton_2.grid(row=2, column=1, pady=3, padx=3)

buton_3 = Button(root, text="3", width=7, height=2, command=tastare_3)
buton_3.grid(row=2, column=2, pady=3, padx=3)

buton_4 = Button(root, text="4", width=7, height=2, command=tastare_4)
buton_4.grid(row=3, column=0, pady=3, padx=3)

buton_5 = Button(root, text="5", width=7, height=2, command=tastare_5)
buton_5.grid(row=3, column=1, pady=3, padx=3)

buton_6 = Button(root, text="6", width=7, height=2, command=tastare_6)
buton_6.grid(row=3, column=2, pady=3, padx=3)

buton_7 = Button(root, text="7", width=7, height=2, command=tastare_7)
buton_7.grid(row=4, column=0, pady=3, padx=3)

buton_8 = Button(root, text="8", width=7, height=2, command=tastare_8)
buton_8.grid(row=4, column=1, pady=3, padx=3)

buton_9 = Button(root, text="9", width=7, height=2, command=tastare_9)
buton_9.grid(row=4, column=2, pady=3, padx=3)

buton_0 = Button(root, text="0", width=7, height=2, command=tastare_0)
buton_0.grid(row=5, column=0, pady=3, padx=3)

buton_plus = Button(root, text="+", width=7, height=2, command=tastare_plus)
buton_plus.grid(row=3, column=3, pady=3, padx=3)

buton_minus = Button(root, text="-", width=7, height=2, command=tastare_minus)
buton_minus.grid(row=4, column=3, pady=3, padx=3)

buton_imult = Button(root, text="*", width=7, height=2, command=tastare_imult)
buton_imult.grid(row=5, column=3, pady=3, padx=3)

buton_impart = Button(root, text="/", width=7, height=2, command=tastare_impart)
buton_impart.grid(row=5, column=2, pady=3, padx=3)

buton_putere = Button(root, text="^", width=7, height=2, command=tastare_putere)
buton_putere.grid(row=6, column=3, pady=3, padx=3)

buton_sterge = Button(root, text="C", width=7, height=2, command=stergere)
buton_sterge.grid(row=2, column=3, pady=3, padx=3)

buton_rest = Button(root, text="%", width=7, height=2, command=tastare_rest)
buton_rest.grid(row=5, column=1, pady=3, padx=3)

buton_egal = Button(root, text="=", height=2, command=afisarea_rezultat)
buton_egal.grid(row=6, column=0, columnspan=3, pady=3, padx=3, sticky="nsew")


root.mainloop()
