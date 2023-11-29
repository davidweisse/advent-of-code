with open("day9_input.txt") as input:
    l = [int(d) for d in input.read().split()]

inavlid = 0
for i in range(25, len(l)):
    valid = False
    for j in range(i-25, i-1):
        for k in range(i-24, i):
            if l[j]+l[k] == l[i]:
                valid = True
    if not valid:
        invalid = l[i]
        break

print(i, l[i])

found = False
for lower in range(len(l)-1):
    for upper in range(lower+1, len(l)):
        print(lower, upper)
        sum = 0
        toohigh = False
        for i in range(lower, upper+1):
            sum += l[i]
            if sum > invalid:
                toohigh = True
        if toohigh:
            break
        if sum == invalid:
            print("lower: ", lower, "upper: ", upper)
            print("sum: ", sum)
            print(l[lower]+l[upper])
            found = True
    if found:
        break