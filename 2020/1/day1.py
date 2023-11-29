input = open("day1_input.txt")

l = [int(d) for d in input.read().split()]

for x in l:
    for y in l:
        if x + y == 2020:
            print(x * y)

for i in l:
    for j in l:
        for k in l:
            if i + j + k == 2020:
                print(i * j * k)
                exit()

input.close()