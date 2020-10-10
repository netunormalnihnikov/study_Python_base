user_Str = input("Введите Ваше предложение: ").split()

for n, word in enumerate(user_Str, 1):
    print(f"{n}. {word[:10].capitalize()}")
