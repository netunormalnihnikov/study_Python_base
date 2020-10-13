def division(n_1, n_2):
    """Выполняет деление первого числа на второе и проверяет тип числа в ответе"""
    try:
        return int(n_1 / n_2) if n_1 % n_2 == 0 else n_1 / n_2
    except ZeroDivisionError:
        return "На ноль делить нельзя"


while True:
    try:
        num_1 = float(input("Введите делимое число: "))
        num_2 = float(input("Введите делитель: "))
        break
    except ValueError:
        print("Неверный ввод. Укажите число")

print(f"Результат деления, первого числа на второе равен:\n{division(num_1, num_2)}")
