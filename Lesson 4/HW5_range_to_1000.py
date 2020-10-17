from functools import reduce


def multiplication_number_list(num_1, num_2):
    return num_1 * num_2


gen_list = [num for num in range(100, 1001) if num % 2 == 0]
print(reduce(multiplication_number_list, gen_list))
