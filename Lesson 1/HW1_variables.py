age = int(input("Введите Ваш возраст: "))
answer = input("У Вас был день рождения в этом году? да/нет: ")
year = 0

if answer == "да":
    year = 2020 - age
elif answer == "нет":
    year = 2019 - age
else:
    print("Неверная команда")

print("Вы родились в", year, "году")
