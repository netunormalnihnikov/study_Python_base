distance_Day = int(input("Введите дистанцию, которую пробежал спортсмен в первый день: "))
distance_For_Answers = int(input("Введите дистанцию, для вычисления дня, её достижения: "))
day = 1

while distance_For_Answers > distance_Day:
    day += 1
    distance_Day = distance_Day + distance_Day * 0.1

print(f"На {day}-й день спортсмен достиг результата — не менее {distance_For_Answers} км")