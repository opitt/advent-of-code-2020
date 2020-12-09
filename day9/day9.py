# https://adventofcode.com/2020/day/9

import os

def is_valid_xmas (numbers_25, num):
    #numbers_25: list 25 of [2,3,45,33,22..] 
    #does any 2 numbers in list add up to num
    for n in numbers_25:
        if num - n in numbers_25:
            return True
    return False


def main():
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, "input_day9.txt"), encoding="utf-8") as input:
        nums = input.readlines()
    nums = [int(n.rstrip()) for n in nums]
    
    #part 1
    #0-24=25
    for i in range(25, len(nums)):
        n = nums[i]
        if not is_valid_xmas(nums[i - 25:i], n):
            result_part1 = n
            break
    print(f"Number {result_part1} is the first number that breaks xmas {nums[result_part1 - 25:result_part1]}.")
    
    #part 2
    #print(f"{result_part2} is the acc after fixing the loop.")
    invalid_num = result_part1

    max_idx = len(nums) - 1
    for start in range(0, len(nums) - 2): # start can only last to nums[-2]
        end = start + 1
        xmas_sum = sum(nums[start:end+1]) # include end index in sum, i.e. +1 
        while end<=max_idx and xmas_sum!=invalid_num and xmas_sum < invalid_num:
            end += 1
            xmas_sum = sum(nums[start:end+1]) 
        if xmas_sum == invalid_num:
            result_part2 = min(nums[start:end+1]) + max(nums[start:end+1]) 
    print(f"{result_part2} is the bug in xmas.")

main()
