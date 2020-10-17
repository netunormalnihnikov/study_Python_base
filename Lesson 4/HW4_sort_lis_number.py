from random import randint
gen_list = [randint(0, 10) for _ in range(15)]
print(gen_list)
print([num for num in gen_list if gen_list.count(num) == 1])
