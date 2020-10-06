profit = int(input("Введите выручку фирмы: "))
expenditure = int(input("Ведите сумму издержек фирмы: "))

if profit > expenditure:
    print(f"Фирма работает в плюс."
          f"\nЧистый доход составляет: {profit - expenditure}."
          f"\nРентабельность фирмы равна: {profit / expenditure:.2f}")
    employee = int(input("Введите количество сотрудников в фирме: "))
    print(f"На одного сотрудника приходится {(profit - expenditure) / employee:.2f} чистой прибыли")
elif profit < expenditure:
    print("Фирма работает в минус. Убытки составляют:", expenditure - profit)
else:
    print("Фирма работает в '0'")
