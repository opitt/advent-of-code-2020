# https://adventofcode.com/2020/day/1

#part 1
with open("input_day1.txt", encoding="utf-8") as input:
    expense_report = input.readlines()
expense_report = list(map(str.strip,expense_report))
expense_report = list(map(int,expense_report))
#expense_report = [1941, 1887, 1851, ...]
e1_2020 = [2020-expense for expense in expense_report]
result = [d for d in e1_2020 if d in expense_report]
print(f"The entries ({result[0]},{result[1]}) sum up to 2020, and multiplied result in {result[0]*result[1]}")

#part 2
e1_2020 = [2020-int(e1) for e1 in expense_report]
for el in e1_2020:
    result = [(el - e2) for e2 in expense_report if (el-e2) in expense_report]
    if len(result) == 2:
        break
result.append(2020 - result[0] - result[1])
print(f"The three elements {result[0]}, {result[1]}, {result[2]} sum up to 2020, and multiplied result in {result[0]*result[1]*result[2]}")