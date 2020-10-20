def num_in_str(text):
    try:
        return int(text[:text.index("(")])
    except ValueError:
        return 0


with open("text_6.txt", "r", encoding="utf-8") as file:
    lesson_dict = {}
    for i in file:
        i = i.split()
        lesson_dict[i[0][:-1]] = num_in_str(i[1]) + num_in_str(i[2]) + num_in_str(i[3])
    print(lesson_dict)
