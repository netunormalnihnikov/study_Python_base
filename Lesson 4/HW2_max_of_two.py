from random import randint, random
gen_list = [randint(0, 100) for _ in range(20)]
print(gen_list)
print([num for n, num in enumerate(gen_list) if n != 0 and num > gen_list[n-1]])
