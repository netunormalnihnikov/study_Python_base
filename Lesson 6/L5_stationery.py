class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Запуск отрисовки ручкой")


class Pencil(Stationery):
    def draw(self):
        print("Запуск отрисовки карандашом")


class Handle(Stationery):
    def draw(self):
        print("Запуск отрисовки маркером")


pen = Pen("Ручка")
pencil = Pencil("Карандаш")
handle = Handle("Маркер")

for i in [pen, pencil, handle]:
    i.draw()
