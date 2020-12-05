# https://adventofcode.com/2020/day/2

# part 1
with open("input_day2.txt", encoding="utf-8") as input:
    pwd_lines = input.readlines()
valid = 0
for line in pwd_lines:
    min_max, letter, pwd = line.strip().split(" ")
    min, max = map(int,min_max.split("-"))
    letter_count = pwd.count(letter[0])
    if letter_count >= min and letter_count <= max:
        valid += 1
print(f"{valid} passwords are valid according to their policies.")

#part 2
valid = 0
for line in pwd_lines:
    pos_pos, letter, pwd = line.strip().split(" ")
    pos1, pos2 = map(int,pos_pos.split("-"))
    el1 = pwd[pos1-1] == letter[0]
    el2 = pwd[pos2-1] == letter[0]
    if  el1 != el2:
        valid += 1
print(f"{valid} passwords are valid according to the new interpretation of the policies.")
