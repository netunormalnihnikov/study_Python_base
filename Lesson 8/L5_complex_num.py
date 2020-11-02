class Complex:
    def __init__(self, n_1, n_2):
        self.n_1 = n_1
        self.n_2 = n_2

    def __str__(self):
        return f"{complex(self.n_1, self.n_2)}"

    def __add__(self, other):
        return complex(self.n_1, self.n_2) + complex(other.n_1, other.n_2)

    def __mul__(self, other):
        return complex(self.n_1, self.n_2) * complex(other.n_1, other.n_2)


num_1 = Complex(3, 1)
num_2 = Complex(2, -3)
print(f"Первое число: {num_1}")
print(f"Второе число: {num_2}")
print(f"Сумма чисел: {num_1 + num_2}")
print(f"Произведение чисел: {num_1 * num_2}")
