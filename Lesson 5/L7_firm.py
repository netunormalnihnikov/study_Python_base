from json import dump

with open("text_7.txt", "r", encoding="utf-8") as file:
    result_list = [{}, {}]
    profit_sum = 0
    company_with_profit = 0
    for i in file:
        i = i.split()
        profit_company = int(i[2]) - int(i[3])
        result_list[0][i[0]] = profit_company
        if profit_company > 0:
            profit_sum += profit_company
            company_with_profit += 1
    result_list[1]["average_profit"] = float(f"{profit_sum / company_with_profit:.2f}")
print(result_list)

with open("text_77.json", "w", encoding="utf-8") as file_j:
    dump(result_list, file_j, indent=4, ensure_ascii=False)
