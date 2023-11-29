input = open("day3_input.txt")

l = input.read().split()
oxygen = ""
co2 = ""
l2 = l.copy()
l3 = l.copy()
i = 0
while len(l2) > 1:
    ones = 0
    for x in l2:
        if x[i] == "1":
            ones += 1
    
    if ones >= len(l2)/2:
        oxygen = "1"
    else:
        oxygen = "0"

    l2c = []
    for j in range(len(l2)):
        if l2[j][i] == oxygen:
            l2c.append(l2[j])

    l2 = l2c.copy()
    
    i += 1

i = 0
while len(l3) > 1:
    ones = 0
    for x in l3:
        if x[i] == "1":
            ones += 1
    
    if ones < len(l3)/2:
        co2 = "1"
    else:
        co2 = "0"

    l3c = []
    for j in range(len(l3)):
        if l3[j][i] == co2:
            l3c.append(l3[j])

    l3 = l3c.copy()
    
    i += 1

print(l2, l3)
input.close()