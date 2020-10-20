def translation(word):
    word = word.lower()
    word_dict = {"one": "Один",
                 "two": "Два",
                 "three": "Три",
                 "four": "Четыре"}
    return word_dict[word]


with open("text_4.txt", "r", encoding="utf-8") as file_source:
    with open("text_4_translate.txt", "w", encoding="utf-8") as file_translate:
        for i in file_source:
            i = i.split()
            file_translate.write(f"{translation(i[0])} {i[1]} {i[2]}\n")
