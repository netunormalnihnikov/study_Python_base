user_seconds = int(input("Введите количество секунд: "))

hours = user_seconds // 3600
minuts = user_seconds % 3600 // 60
seconds = user_seconds % 3600 % 60

print(f"В {user_seconds} секундах {hours:0>2d}ч:{minuts:0>2d}м:{seconds:0>2d}с")
