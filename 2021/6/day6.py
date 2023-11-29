with open("day6_input.txt") as input:
    l = [int(d) for d in input.read().split(",")]

for i in range(30):
    print(str(len(l)) + ",")
    for j in range(len(l)):
        l[j] -= 1
        if l[j] == -1:
            l[j] = 6
            l.append(8)

print(len(l))