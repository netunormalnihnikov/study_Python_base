from sys import argv

name, sum_hours, cost_hours, prem = argv

print("Сумма зарплаты равна:", int(sum_hours) * int(cost_hours) + int(prem))
