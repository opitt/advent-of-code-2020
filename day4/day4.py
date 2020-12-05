# https://adventofcode.com/2020/day/4

# part 1
with open("input_day4.txt", encoding="utf-8") as input:
    line = input.read()
passports = [l.replace("\n", " ") for l in line.split("\n\n")]
#print(passports)
# ["hcl:5d90f0 cid:270 ecl:#66dc9c hgt:62cm byr:1945 pid:63201172 eyr:2026"]

valids = 0
for p in passports:
    valids += "byr:" in p and "iyr:" in p and "eyr:" in p and "hgt:" in p and "hcl:" in p and "ecl:" in p and "pid:" in p

print(f"Valid passports: {valids}")

# part 2
import re

valids = 0
min_max = lambda key,vmin,vmax: int(pel.get(key,vmin-1)) >= vmin and int(pel.get(key,vmax+1))<=vmax
for p in passports:
    valid = True
    #create a passport dictionary with pel (passport element)
    pel = {field.split(":")[0]: field.split(":")[1] for field in p.split(" ") if field != ""}
    valid &= min_max("byr", 1920, 2002)
    valid &= min_max("iyr", 2010, 2020)
    valid &= min_max("eyr", 2020, 2030)
    valid &= pel.get("ecl","") in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
    if valid:
        num, unit = int(pel.get("hgt", "00xx")[:-2]), pel.get("hgt","00xx")[-2:]
        valid &= (unit == "cm" and num >= 150 and num <=193 or 
                           unit == "in" and num >= 59 and num <=76)
    for pattern, key in [(r"^#[\da-f]{6}$","hcl"), (r"^[\d]{9}$","pid") ]:
        match = re.fullmatch(pattern, pel.get(key,""))
        valid &= (match != None)
    
    valids += valid
    
print(f"Validated passports: {valids}")