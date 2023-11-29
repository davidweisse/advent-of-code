with open("day11_input.txt") as input:
    l = input.read().split()
    for i in range(len(l)):
        l[i] = [int(d) for d in l[i]]

flashes = 0
def flash(row, col):
    global flashes
    if row > 0:
        if l[row-1][col] != -1:
            l[row-1][col] += 1
        if col > 0:
            if l[row-1][col-1] != -1:
                l[row-1][col-1] += 1
        if col < len(l[row])-1:
            if l[row-1][col+1] != -1:
                l[row-1][col+1] += 1
    if col > 0:
        if l[row][col-1] != -1:
            l[row][col-1] += 1
    if col < len(l[row])-1:
        if l[row][col+1] != -1:
            l[row][col+1] += 1
    if row < len(l)-1:
        if l[row+1][col] != -1:
            l[row+1][col] += 1
        if col > 0:
            if l[row+1][col-1] != -1:
                l[row+1][col-1] += 1
        if col < len(l[row])-1:
            if l[row+1][col+1] != -1:
                l[row+1][col+1] += 1
    l[row][col] = -1
    flashes += 1
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j] > 9:
                flash(i, j)
    l[row][col] = 0

for i in range(215):
    for row in range(len(l)):
        l[row] = [n+1 for n in l[row]]
    for row in range(len(l)):
        for col in range(len(l[row])):
            if l[row][col] > 9:
                flash(row, col)
for s in l:
    print(s)
print(flashes)