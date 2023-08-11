a = "Програма перевірки логіна і пароля"
a1 = a.center(100)
print(a1)

def printWelcome(user):
    z = f"Ласкаво просимо, {user}!!!"
    z1 = z.center(100)
    return z1
    

# ===============DateUsers============

user1 = "Taras"
password1 = "TarasPassword"

user2 = "Illia"
password2 = "IlliaPassword"

user3 = "Anton"
password3 = "AntonPassword"

# ===============Input Data============

login = input("Введіть логін: ")
password = input("Введіть пароль: ")

if login == user1 and password == password1:
    print(printWelcome(user1))
elif login == user2 and password == password2:
    printWelcome(user2)
elif login == user3 and password == password3:
    printWelcome(user3)


# if (
#     (login == user1 and password == password1)
#     or (login == user2 and password == password2)
#     or (login == user3 and password == password3)
# ):

else:
    while (
        not (login == user1 and password == password1)
        or (login == user2 and password == password2)
        or (login == user3 and password == password3)
    ):
        print("Неправильний логін чи пароль. Спробуйте ще раз")
        login = input("Введіть логін: ")
        password = input("Введіть пароль: ")
    else:
        if login == user1 and password == password1:
            printWelcome(user1)
        # print(f'{z1}, {login}')
        elif login == user2 and password == password2:
            printWelcome(user2)
        elif login == user3 and password == password3:
            printWelcome(user3)
