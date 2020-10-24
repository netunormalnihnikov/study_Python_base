from random import choice


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Машина {self.name}, цвет {self.color}- поехала")

    def stop(self):
        print(f"Машина {self.name} остановилась")

    def turn(self):
        direction = ["Налево", "Направо"]
        print(f"Машина {self.name} повернула {choice(direction)}")

    def show_speed(self):
        print(f"Текущая скорость автомобиля {self.speed}")


class TownCar(Car):
    def show_speed(self):
        print("Вы превысили!" if self.speed > 60 else f"Текущая скорость автомобиля {self.speed}")


class SportCar(Car):
    def see_car(self):
        print("UAAAAU")


class WorkCar(Car):
    def show_speed(self):
        print("Вы превысили!" if self.speed > 40 else f"Текущая скорость автомобиля {self.speed}")


class PoliceCar(Car):
    def pursuit(self):
        print("VI-U-VI-U")


town_car = TownCar(70, "красный", "Lada", False)
sport_car = SportCar(150, "зеленый", "Lamborgini", False)
work_car = WorkCar(30, "Желтый", "Газель", False)
police_car = PoliceCar(90, "синий", "Skoda", True)

for i in [town_car, sport_car, work_car, police_car]:
    if i == sport_car:
        i.see_car()
    i.go()
    i.turn()
    i.show_speed()
    if i == police_car:
        i.pursuit()
    i.stop()
    print("".join("-" for _ in range(40)))
