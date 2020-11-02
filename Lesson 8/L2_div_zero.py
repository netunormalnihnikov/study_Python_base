class ChkZero(Exception):
    def __init__(self, text):
        self.text = text


try:
    n_1 = int(input("Введите делимое: "))
    n_2 = int(input("Введите делитель: "))
    if n_2 == 0:
        raise ChkZero("Делитель не может быть равен нулю")
    print(f"Результат деления равен: {n_1 / n_2}")
except ValueError:
    print("Введены некорректные значения. Введите числа")
except ChkZero as error:
    print(error)
