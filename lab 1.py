try:
    num1 = int(input("Введите певрое число: "))
    num2 = int(input("Введите втрое число: "))
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
except ValueError:
    print("Ввели не число")