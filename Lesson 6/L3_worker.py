class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f"{self.name} {self.surname}")

    def get_total_income(self):
        print(sum(self._income.values()))


a = Position("Александр", "Сотников", "TeamLead", 25000, 15000)
a.get_total_income()
a.get_full_name()
