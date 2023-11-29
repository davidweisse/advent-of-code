with open("day5_input.txt") as input:
    l = input.read().split("\n")
    l = [s.split(" -> ") for s in l]
    for i in range(len(l)):
        for j in range(len(l[i])):
            l[i][j] = [int(d) for d in l[i][j].split(",")]

def draw(field):
    for i in field:
        s = ""
        for j in i:
            if j == 0:
                s += "."
            else:
                s += str(j)
        print(s)

highest_x = 0
highest_y = 0
for  i in l:
    for j in i:
        if j[0] > highest_x:
            highest_x = j[0]
        if j[1] > highest_y:
            highest_y = j[1]

highest_x += 1
highest_y += 1
field = [[0]*highest_x for i in range(highest_y)]

for i in l:
    if i[0][0] == i[1][0]:
        if i[1][1] > i[0][1]:
            for j in range(i[0][1], i[1][1]+1):
                field[j][i[0][0]] += 1
        else:
            for j in range(i[1][1], i[0][1]+1):
                field[j][i[0][0]] += 1
    elif i[0][1] == i[1][1]:
        if i[1][0] > i[0][0]:
            for j in range(i[0][0], i[1][0]+1):
                field[i[0][1]][j] += 1
        else:
            for j in range(i[1][0], i[0][0]+1):
                field[i[0][1]][j] += 1
    else:
        if i[1][0] > i[0][0]:
            if i[1][1] > i[0][1]:
                for j, k in zip(range(i[0][0], i[1][0]+1), range(i[0][1], i[1][1]+1)):
                    field[k][j] += 1
            else:
                for j, k in zip(range(i[0][0], i[1][0]+1), range(i[0][1], i[1][1]-1, -1)):
                    field[k][j] += 1
        else:
            if i[1][1] > i[0][1]:
                for j, k in zip(range(i[0][0], i[1][0]-1, -1), range(i[0][1], i[1][1]+1)):
                    field[k][j] += 1
            else:
                for j, k in zip(range(i[0][0], i[1][0]-1, -1), range(i[0][1], i[1][1]-1, -1)):
                    field[k][j] += 1

twoormore = 0
for i in field:
    for j in i:
        if j >= 2:
            twoormore += 1

print(twoormore)