def my_func(x, y):
    answer = 1
    for i in range(abs(y)):
        answer *= x
    try:
        return 1/answer
    except ZeroDivisionError:
        return "0 нельзя возвести в отрицательную степень."


while True:
    try:
        num_1 = float(input("Введите число, возводимое в отрицательную степень: "))
        num_2 = int(input("Введите отрицательную степень: "))
        break
    except ValueError:
        print("Неверный ввод. Укажите число")

print(f"После возведения числа {num_1} в степень {num_2}, получается ответ:\n{my_func(num_1, num_2)}")
