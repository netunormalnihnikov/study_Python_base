class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def counting(self):
        print(f"Масса асфальта равна:\n{(self._length * self._width * 25 * 5) / 1000:.2f} т.")


length_road = input("Введите длину дороги: ")
width_road = input("Введите ширину дороги: ")
try:
    a = Road(int(length_road), int(width_road))
    a.counting()
except ValueError:
    print("Введены некоректные значения")
