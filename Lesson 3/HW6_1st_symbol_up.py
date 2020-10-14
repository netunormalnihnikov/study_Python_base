def int_func(int_str):
    """Убирает слова с кирилицей и символами. В оставшихся словах, первую букву, переводит вверхний регистр"""
    new_str = ""
    for word in int_str.split():
        new_word = ""
        for letter in word:
            if 96 < ord(letter) < 123:
                new_word += letter
            else:
                new_word = ""
                break
        new_str += new_word + " "
    return " ".join(new_str.title().split())


user_text = input("Введите текст разделенный пробелом: ")
print(int_func(user_text))
