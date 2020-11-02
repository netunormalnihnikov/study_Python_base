class Date:
    def __init__(self, date_str):
        self.date_str = date_str

    def __str__(self):
        try:
            return f"{self.chek_date(self.convert_to_int(self.date_str))}"
        except (ValueError, IndexError):
            return "Введены некорректные данные"

    @classmethod
    def convert_to_int(cls, date_str):
        return list(map(int, date_str.split("-")))

    @staticmethod
    def chek_date(date_list):
        if date_list[2] <= 0 or date_list[2] > 2500:
            return "Введен некорректный год"
        date_dict = {1: 31,
                     2: 28,
                     3: 31,
                     4: 30,
                     5: 31,
                     6: 30,
                     7: 31,
                     8: 31,
                     9: 30,
                     10: 31,
                     11: 30,
                     12: 31}
        if date_list[2] % 4 == 0:
            date_dict[2] = 29
        try:
            if date_list[0] > date_dict[date_list[1]] or 0 >= date_list[0]:
                return "Введен некорректный день"
        except KeyError:
            return "Введен некорректный месяц"
        return f"Данные введены корректно: {date_list[0]}.{date_list[1]}.{date_list[2]}"


usr_date = Date("01-02-2020")
print(usr_date)
