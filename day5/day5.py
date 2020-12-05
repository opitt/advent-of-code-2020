
# https://adventofcode.com/2020/day/5

#part 1

with open("./input_day5.txt", encoding="utf-8") as input:
    seat_codes = input.readlines()

def half(direction, low, high, lower_half):
    if high-low == 1:
        return low if direction[0] == lower_half else high
    if direction[0] == lower_half:
        high = low + (high-low)//2
    else:
        low = low + (high-low)//2 +1
    return half(direction[1:],low, high, lower_half)

seats=[]
for code in seat_codes:
    code = code.strip() # remove newline
    row, col = half(code[:7],0,127,"F"), half(code[7:],0,7,"L")
    seats.append(row*8+col)
print(f"Highest seat: {max(seats)}")

#part 2
seats = sorted(seats)
#zipped seats: (513,514) (514,516) << my_seat is the gap: 514+1
my_seat = [seat[0]+1 for seat in zip(seats[:-1], seats[1:]) if seat[0]+1 != seat[1]][0]
print(f"My seat is {my_seat}")

#print([seat[0]+1 for seat in zip(seats[:-1], seats[1:]) if seat[0]+1 != seat[1]])
