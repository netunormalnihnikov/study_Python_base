with open("user_history.txt", "w", encoding="utf-8") as file:
    """Созданный файл будет отрабатывать во втором задании"""
    n = 1
    text = "1"
    while text != "":
        text = input(f"Введите {n}-ю строку: ")
        if text != "":
            file.write(text + "\n")
            n += 1
