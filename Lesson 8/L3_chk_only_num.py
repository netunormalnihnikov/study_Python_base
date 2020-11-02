class OnlyNum(Exception):
    def __init__(self, text):
        self.text = text


result = []
while True:
    usr_num = input("Введите число. Для выхода наберите 'stop': ")
    if usr_num.lower() == "stop":
        print(result)
        break

    """Проверка на отрицательное число с точкой"""
    if usr_num[0] == "-":
        tmp_list = usr_num[1:].split(".") if len(usr_num.split(".")) == 2 else [""]
    else:
        tmp_list = usr_num.split(".") if len(usr_num.split(".")) == 2 else [""]

    """Проверка на целое, целое отрицательное число. Также проверяется число с точкой"""
    try:
        if usr_num.isdigit() or (usr_num[0] == "-" and usr_num[1:].isdigit()):
            result.append(int(usr_num))
        elif tmp_list[0].isdigit() and tmp_list[1].isdigit():
            result.append(float(usr_num))
        else:
            raise OnlyNum("Некорректный ввод")
    except OnlyNum as error:
        print(error)
