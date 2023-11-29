with open("day1_input.txt") as input:
    l = [int(d) for d in input.read().split()]

s = 0
for i in range(1, len(l)-2):
    if l[i]+l[i+1]+l[i+2] > l[i-1]+l[i]+l[i+1]:
        s += 1
        
print(s)