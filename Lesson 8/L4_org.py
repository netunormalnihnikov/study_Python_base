class Store:
    def __init__(self, store_dict=None):
        if store_dict is None:
            store_dict = {}
        self.store_dict = store_dict
        self.dep_list = ["IT", "HR", "Accounting", "Склад"]
        self.unit_list = ["Принтер", "Сканер", "Ксерокс"]

    def __str__(self):
        output_str = ""
        for dep, item_1 in self.store_dict.items():
            output_str += f"{dep}:\n"
            for unity_name, item_2 in item_1.items():
                output_str += f"\t{unity_name}:\n"
                for n, i in enumerate(item_2, 1):
                    output_str += f"\t\t{n}. {i}\n"
        return output_str

    def add_unit(self):
        dep = self.output_print(self.dep_list, "Выберите департамент: ")
        unit_type = self.output_print(self.unit_list, "Выберите тип устройства: ")
        self.chk_dict(dep, unit_type)
        self.store_dict[dep][unit_type].append(self.init_method(unit_type))

    def del_unit(self):
        dep = self.output_print(list(self.store_dict.keys()), "Выберите департамент: ")
        unit_type = self.output_print(list(self.store_dict[dep].keys()), "Выберите тип устройства: ")
        unit_pos = self.output_print(self.store_dict[dep][unit_type], "Выберите устройство: ", 1)
        if len(self.store_dict[dep][unit_type]) == 1:
            self.store_dict[dep].pop(unit_type)
        else:
            self.store_dict[dep][unit_type].pop(unit_pos)
        if len(self.store_dict[dep]) == 0:
            self.store_dict.pop(dep)

    def change_dep(self):
        dep_for_del = self.output_print(list(self.store_dict.keys()), "Выберите департамент, откуда переносим: ")
        unit_type = self.output_print(list(self.store_dict[dep_for_del].keys()), "Выберите тип устройства: ")
        unit_pos = self.output_print(self.store_dict[dep_for_del][unit_type], "Выберите устройство, для переноса: ", 1)
        if len(self.store_dict[dep_for_del][unit_type]) == 1:
            el = self.store_dict[dep_for_del][unit_type].pop(unit_pos)
            self.store_dict[dep_for_del].pop(unit_type)
        else:
            el = self.store_dict[dep_for_del][unit_type].pop(unit_pos)
        if len(self.store_dict[dep_for_del]) == 0:
            self.store_dict.pop(dep_for_del)
        dep = self.output_print(self.dep_list, "Выберите департамент, куда перенесем: ")
        self.chk_dict(dep, unit_type)
        self.store_dict[dep][unit_type].append(el)

    def chk_dict(self, dep, unit_type):
        if self.store_dict.get(dep) is None:
            self.store_dict.update({dep: {}})
        if self.store_dict[dep].get(unit_type) is None:
            self.store_dict[dep].update({unit_type: []})

    @staticmethod
    def init_method(unit_type):
        if unit_type == "Принтер":
            return Print().dict
        elif unit_type == "Сканер":
            return Scan().dict
        elif unit_type == "Ксерокс":
            return Copy().dict

    @staticmethod
    def output_print(iter_list, txt, ret_pos=None):
        while True:
            try:
                for n, el in enumerate(iter_list, 1):
                    print(f"{n}. {el}")
                usr_input = int(input(txt))
                if ret_pos:
                    return usr_input - 1
                return iter_list[usr_input - 1]
            except (IndexError, ValueError):
                print("Некорректный ввод. Попробуйте снова")


class OfficeEquipment:
    def __init__(self):
        self.company = input("Укажите производителя устройства: ")
        self.color = input("Укажите цвет устройства: ")
        self.connect = input("Укажите тип подключения устройства: ")
        self.dict = {"Компания": self.company,
                     "Цвет устройства": self.color,
                     "Способ подключения": self.connect}


class Print(OfficeEquipment):
    def __init__(self):
        super().__init__()
        self.print_type = input("Укажите тип принтера: ")
        self.color_type = input("Принтер цветной?: ")
        self.dict.update({"Тип принтера": self.print_type,
                          "Цветная печать": self.color_type})


class Scan(OfficeEquipment):
    def __init__(self):
        super().__init__()
        self.speed_scan = input("Укажите скорость сканирования в секундах: ")
        self.dict.update({"Скорость сканирования": self.speed_scan})


class Copy(OfficeEquipment):
    def __init__(self):
        super().__init__()
        self.speed_copy = input("Укажите скорость копирования в секундах: ")
        self.dict.update({"Скорость копирования": self.speed_copy})


a = {"IT": {"Принтер": [{"Компания": "Samsung", "Цвет устройства": "white", "Способ подключения": "USB",
                         "Тип принтера": "Laser", "Цветная печать": "yes"},
                        {"Компания": "Sony", "Цвет устройства": "black", "Способ подключения": "Lan",
                         "Тип принтера": "Струный", "Цветная печать": "yes"}],
            "Сканер": [{"Компания": "HP", "Цвет устройства": "white", "Способ подключения": "USB",
                        "Скорость сканирования": 99},
                       {"Компания": "Xerox", "Цвет устройства": "black", "Способ подключения": "Lan",
                        "Скорость сканирования": 11}],
            "Ксерокс": [{"Компания": "HP", "Цвет устройства": "white", "Способ подключения": "USB",
                         "Скорость копирования": 9},
                        {"Компания": "Xerox", "Цвет устройства": "white", "Способ подключения": "USB",
                         "Скорость копирования": 10}]},
     "HR": {"Принтер": [{"Компания": "Samsung", "Цвет устройства": "white", "Способ подключения": "USB",
                         "Тип принтера": "Laser", "Цветная печать": "yes"},
                        {"Компания": "Sony", "Цвет устройства": "black", "Способ подключения": "Lan",
                         "Тип принтера": "Laser", "Цветная печать": "yes"}],
            "Сканер": [{"Компания": "HP", "Цвет устройства": "white", "Способ подключения": "USB",
                        "Скорость сканирования": 99},
                       {"Компания": "Xerox", "Цвет устройства": "black", "Способ подключения": "Lan",
                        "Скорость сканирования": 11}],
            "Ксерокс": [{"Компания": "HP", "Цвет устройства": "white", "Способ подключения": "USB",
                         "Скорость копирования": 9},
                        {"Компания": "Xerox", "Цвет устройства": "white", "Способ подключения": "USB",
                         "Скорость копирования": 10}]},
     "Accounting": {"Принтер": [{"Компания": "Samsung", "Цвет устройства": "white", "Способ подключения": "USB",
                                 "Тип принтера": "Laser", "Цветная печать": "yes"},
                                {"Компания": "Sony", "Цвет устройства": "black", "Способ подключения": "Lan",
                                 "Тип принтера": "Laser", "Цветная печать": "yes"}],
                    "Сканер": [{"Компания": "HP", "Цвет устройства": "white", "Способ подключения": "USB",
                                "Скорость сканирования": 99},
                               {"Компания": "Xerox", "Цвет устройства": "black", "Способ подключения": "Lan",
                                "Скорость сканирования": 11}],
                    "Ксерокс": [{"Компания": "HP", "Цвет устройства": "white", "Способ подключения": "USB",
                                 "Скорость копирования": 9},
                                {"Компания": "Xerox", "Цвет устройства": "white", "Способ подключения": "USB",
                                 "Скорость копирования": 10}]},
     "Склад": {"Принтер": [{"Компания": "Samsung", "Цвет устройства": "white", "Способ подключения": "USB",
                            "Тип принтера": "Laser", "Цветная печать": "yes"},
                           {"Компания": "Sony", "Цвет устройства": "black", "Способ подключения": "Lan",
                            "Тип принтера": "Laser", "Цветная печать": "yes"}],
               "Сканер": [{"Компания": "HP", "Цвет устройства": "white", "Способ подключения": "USB",
                           "Скорость сканирования": 99},
                          {"Компания": "Xerox", "Цвет устройства": "black", "Способ подключения": "Lan",
                           "Скорость сканирования": 11}],
               "Ксерокс": [{"Компания": "HP", "Цвет устройства": "white", "Способ подключения": "USB",
                            "Скорость копирования": 9},
                           {"Компания": "Xerox", "Цвет устройства": "white", "Способ подключения": "USB",
                            "Скорость копирования": 10}]}
     }


def chk_empty(dictionary):
    return len(dictionary) == 0


store = Store(a)

while True:
    task_str = {"Добавить позицию на склад": "store.add_unit()", "Выйти": "exit()"}\
        if chk_empty(store.store_dict) else\
        {"Показать склад": "print(store)", "Добавить позицию на склад": "store.add_unit()",
         "Удалить позицию со склада": "store.del_unit()", "Переместить позицию": "store.change_dep()",
         "Очистить склад": "store.store_dict.clear()", "Выйти": "exit()"}
    if chk_empty(store.store_dict):
        print("Склад пустой")
    exec(task_str[store.output_print(list(task_str.keys()), "Укажите желаемую команду: ")])
