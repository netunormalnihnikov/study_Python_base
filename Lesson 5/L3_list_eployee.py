with open("text_3.txt", "r", encoding="utf-8") as file:
    print("Список сотрудников с окладом менее 20000:")
    all_money = 0
    emp = 0
    for i in file:
        emp += 1
        i = i.split()
        all_money += float(i[1])
        if float(i[1]) < 20000:
            print(i[0])
    print(f"Средний доход составляет: {all_money / emp:.2f}")
