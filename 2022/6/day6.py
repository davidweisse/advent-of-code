with open("input/day6_input.txt") as f:
    l = f.read()

print([i + 4 for i in range(len(l)) if len(set(l[i:i + 4])) == 4][0])

print([i + 14 for i in range(len(l)) if len(set(l[i:i + 14])) == 14][0])

for i in range(len(l)):
    if len(set(l[i:i + 4])) == 4:
        print(i + 4, l[i:i + 4])
        break

