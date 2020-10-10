my_List = [1, 2.33, "str", (2, 3), True, [4, 5]]

print(f"Список '{my_List}' содержит следующие типы элементов: ")
for i in my_List:
    print(f"Элемент {i} имеет тип: {type(i)}")
