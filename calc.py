number1 = int(input("Введите число :"))
sign = input("Введите символ :")
number2 = int(input("Введите число :"))
if sign == "+":
    print(number1 + number2)
elif sign == "-":
    if number1 > number2:
        print(number1 - number2)
    else:
        print(number2 - number1)
elif sign == "/" and number2 != 0:
    print(number1 / number2)
elif sign == "*":
    print(number1 * number2)
else:
    print("Я не знаю такого знака")

