from itertools import count, cycle

start_num = int(input("Введите число с которого начнется последовательность: "))


gen_for_count = count(start_num)
gen_list = [next(gen_for_count) for _ in range(10)]
print(gen_list)


gen_for_cycle = cycle(gen_list)
gen_cycle_list = [next(gen_for_cycle) for _ in range(20)]
print(gen_cycle_list)
