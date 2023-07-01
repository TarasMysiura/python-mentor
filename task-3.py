a = float(input('введіть перше число: '))

action = input('введіть дію (+ - * /): ')

b = float(input('введіть друге число: '))


if (action == "+" or action == " +" or action == "+ " or action == " + "):
    print("Сумма чисел дорівнює ", str(a+b))
elif (action == "-" or action == " -" or action == "- " or action == " - "):
    print("Різниця чисел дорівнює ", str(a-b))
elif (action == "/" or action == " /" or action == "/ " or action == " / "):
    print("Частка чисел дорівнює", str(a/b))
elif (action == "*" or action == " *" or action == "* " or action == " * "):
    print('Добуток чисел дорівнює', str(a*b))
elif (action == "^" or action == " ^" or action == "^ " or action == " ^ "):
    print('Піднесення числа ', a,' до степеня ', b, ' дорівнює', str(a**b))
else:
    print('невірно набрано')
