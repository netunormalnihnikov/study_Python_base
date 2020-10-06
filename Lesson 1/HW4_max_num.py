user_num = int(input("Введите целое, положительное число: "))
answer = 0
temp_num = 0

while user_num != 0:
    temp_num = user_num % 10
    user_num = user_num // 10
    if answer < temp_num:
        answer = temp_num

print("Самая большая цифра из Вашего числа:", answer)
