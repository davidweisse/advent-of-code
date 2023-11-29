with open("day5_input.txt") as input:
    l = input.read().split()

seats = []
for i in l:
    row_start = 0
    row_end = 127
    for j in range(7):
        if i[j] == "F":
            row_end -= 2**(7-j-1)
        else:
            row_start += 2**(7-j-1)
        #print(row_start, row_end)
    col_start = 0
    col_end = 7
    for j in range(7, 10):
        if i[j] == "L":
            col_end -= 2**(10-j-1)
        else:
            col_start += 2**(10-j-1)
        #print(col_start, col_end)
    seats.append(row_start*8+col_start)

seats.sort()

for i in range(80, 927):
    if i not in seats:
        print(i)