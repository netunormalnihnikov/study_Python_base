def sum_num_in_str(user_str):
    """Функия принимает строку.

    Возвращает кортеж sum_str, "q" или "":
    sum_str -- сумма чисел в строке до символа "q"(при его наличии);
    "q" -- возвращается если в строке был данный символ;
    "" -- возвращается если в строке не было символа "q".

    """
    user_str = user_str.split()
    sum_str = 0
    for elem in user_str:
        if elem.lower() == "q":
            return sum_str, elem.lower()
        elif elem.isdigit():
            sum_str += int(elem)
    return sum_str, ""


sum_total = 0
while True:
    """Цикл работает, пока функция не вернет вторым значением кортежа символ- 'q'."""
    user_num = input("Введите строку чисел, разделенных пробелом. "
                     "Подсчет после символа 'q', будет остановлен: ")
    data_tuple = sum_num_in_str(user_num)
    sum_total += data_tuple[0]
    print(f"Сумма введенных чисел равна {data_tuple[0]}. Общая сумма равна {sum_total}")
    if data_tuple[1] == "q":
        break

print("Ввод окончен")
