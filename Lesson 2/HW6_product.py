user_Count_List = input("Укажите, сколько товаров, вы хотите ввести: ")

while not user_Count_List.isdigit() or user_Count_List == "0":  # проверка ввода
    user_Count_List = input("Вы ввели некорректное значение.\nВведите целое, положительное число: ")

user_Count_List = int(user_Count_List)
product_List = []  # список товаров
word_Dict = {"название": [],  # словарь для создания списка
             "цена": [],
             "количество": [],
             "eд": []}
analyt_Dict = word_Dict.copy()  # словарь для вычисления аналитики

for i in range(1, user_Count_List + 1):
    for n in word_Dict:
        tmp_Str_Or_Int = input(f"{n} {i}-го товара: ")  # переменная для дальнейшей проверки на str или int
        word_Dict[n] = int(tmp_Str_Or_Int) if n == "цена" or n == "количество" else tmp_Str_Or_Int
    product_List += [(i, word_Dict.copy())]

print("Указанный список товаров: ")
for i in product_List:
    print(i)

for i in product_List:
    for n in i[1]:
        analyt_Dict[n].append(i[1].get(n))

print("Аналитика по указанным товарам: ")
for i in analyt_Dict.items():
    print(i)
