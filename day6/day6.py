# https://adventofcode.com/2020/day/6

def part1():
    with open("input_day6.txt", encoding="utf-8") as input:
        content = input.read()
    groups = [group_answers.replace("\n","") for group_answers in content.split("\n\n") if group_answers != ""]
    result_part1 = sum([ len(set(answers)) for answers in groups])
    print(f"The sum of the unique yes answers in all groups is {result_part1}")

def part2():
    with open("input_day6.txt", encoding="utf-8") as input:
        content = input.read()
    groups = [group_answers for group_answers in content.split("\n\n") if group_answers != ""]
    result_part2 = sum([len(set.intersection(*list(set(answer) for answer in answers.split("\n") if answer!=""))) for answers in groups])
    #? ONE LINER EXPANDED FOR BETTER UNDERSTANDING / LEARNING: 
    #? result_part2 = 0
    #? for answers in groups:
    #?     answer_sets = [set(answer) for answer in answers.split("\n") if answer!=""] #single passenger group (one line only)
    #?     common_answers = set.intersection(*answer_sets)
    #?     common = len(common_answers)
    #?     result_part2 += common
    print(f"The sum of the all yes answers of a question in all groups is {result_part2}")

part1()
part2()