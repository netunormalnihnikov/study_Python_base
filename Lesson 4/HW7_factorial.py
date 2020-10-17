def fact(n):
    answer = 1
    if n == 0:
        return answer
    else:
        for i in range(1, n + 1):
            answer *= i
            yield answer


for el in fact(5):
    print(el)
