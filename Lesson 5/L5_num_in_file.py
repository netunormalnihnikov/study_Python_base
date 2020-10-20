from random import randint

with open("text_5.txt", "w+", encoding="utf-8") as file:
    file.write(" ".join([f"{randint(0, 100)}" for _ in range(10)]))
    file.seek(0)
    print(f"Числа записанные в файл 'text_5.txt': {file.read()}")
    file.seek(0)
    print(f"Сумма чисел в файле равна: {sum([int(i) for i in file.read().split()])}")
