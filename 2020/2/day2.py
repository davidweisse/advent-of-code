input = open("day2_input.txt")

l = input.read().replace('-', ' ').split()

valid = 0
for i in range(0, len(l), 4):
    if int(l[i]) <= l[i + 3].count(l[i + 2][0]) <= int(l[i + 1]):
        valid += 1

print(valid)

valid = 0
for i in range(0, len(l), 4):
    if l[i+3][int(l[i])-1] == l[i+2][0] and not l[i+3][int(l[i+1])-1] == l[i+2][0]:
        valid += 1
    elif l[i+3][int(l[i+1])-1] == l[i+2][0] and not l[i+3][int(l[i])-1] == l[i+2][0]:
        valid += 1

print(valid)
input.close()