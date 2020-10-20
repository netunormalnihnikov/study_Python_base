with open("user_history.txt", "r", encoding="utf-8") as file:
    line = 0
    for i in file:
        line += 1
        print(f"Слов в {line}-й строке: {len(i.split())}")
