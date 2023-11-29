with open("day2_input.txt") as input:
    l = input.read().split()

horizontal = 0
depth = 0
aim = 0
for i in range(0, len(l), 2):
    if l[i] == "forward":
        horizontal += int(l[i+1])
        depth += aim * int(l[i+1])
    elif l[i] == "down":
        aim += int(l[i+1])
    elif l[i] == "up":
        aim -= int(l[i+1])

print(horizontal*depth)