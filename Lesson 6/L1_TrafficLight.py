from time import sleep, time


class TrafficLight:
    __color = {"Красный": [7, "\033[31m {}"],
               "Желтый": [2, "\033[33m {}"],
               "Зеленый": [4, "\033[32m {}"]}

    def running(self):
        start = time()
        while time() - start < 30:
            for key, delay_and_color in self.__color.items():
                print(delay_and_color[1].format(key))
                sleep(delay_and_color[0])


a = TrafficLight()
a.running()
