my_list = [7, 5, 3, 3, 2]

user_Num = input(f"Укажите число, которое необходимо добавить в список {my_list}: ")
while not user_Num.isdigit():  # проверка ввода
    user_Num = input("Вы ввели некорректное значение.\nВведите целое число большее или равное 0: ")
user_Num = int(user_Num)
pos_Elem = 0  # переменная для вычисления позиции элемента

if user_Num in my_list:  # если число есть в списке
    for n, i in enumerate(my_list):
        if i == user_Num:
            pos_Elem = n + 1
    my_list.insert(pos_Elem, str(user_Num))
else:   # если числа нет в списке
    my_list.insert(0, user_Num) if my_list[0] < user_Num else my_list.append(user_Num)

print(f"Число {user_Num}, было добавлено в список:\n{my_list}")
