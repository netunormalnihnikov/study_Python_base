user_Length_List = input("Введите требуемую длину списка: ")
while not user_Length_List.isdigit():  # проверка ввода
    user_Length_List = input("Вы ввели некорректное значение.\nВведите целое, положительное число: ")
result_List = []  # для вывода обработанного списка
user_List = []  # для вывода вбитого списка
i = 0  # счетчик

while i != int(user_Length_List):
    user_elem = input(f"Введите {i + 1}-й элемент: ")
    user_List.append(user_elem)
    result_List.append(user_elem)
    if (i + 1) % 2 == 0:
        result_List[i - 1], result_List[i] = result_List[i], result_List[i - 1]
    i += 1
print(f"{user_List} - Введенный Вами список. После изменения позиций элементов, список стал:\n{result_List}")
