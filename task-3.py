a = float(input('введіть перше число: '))

action = input('введіть дію (+ - * /): ')

b = float(input('введіть друге число: '))


if (action == "+"):
    print("Сумма чисел дорівнює ", str(a+b))
elif (action == "-"):
    print("Різниця чисел дорівнює ", str(a-b))
elif (action == "/"):
    print("Частка чисел дорівнює", str(a/b))
elif (action == "*"):
    print('Добуток чисел дорівнює', str(a*b))
else:
    print('невірно набрано')
