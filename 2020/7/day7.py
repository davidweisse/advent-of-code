with open("day7_input.txt") as input:
    raw = input.read().split("\n")
    l = []
    for i in range(len(raw)):
        line = raw[i].split()
        l.append([line[0] + " " + line[1]])
        for j in range(len(line)):
            try:
                if int(line[j]):
                    l[i].append(int(line[j]))
                    l[i].append(line[j+1] + " " + line[j+2])
            except ValueError:
                pass

cache = []
def count_bags(color):
    bags = []
    count = 0
    for i in range(len(l)):
        for j in range(2, len(l[i])):
            if l[i][j] == color:
                if l[i][0] not in bags and l[i][0] not in cache:
                    bags.append(l[i][0])
                    cache.append(l[i][0])
    count = len(bags)
    for b in bags:
        count += count_bags(b)
    if bags == []:
        return 0
    else:
        print(bags)
        return count

def inside_bags(color):
    bags = []
    count = 1
    for i in range(len(l)):
        if l[i][0] == color:
            #print(l[i])
            if len(l[i]) > 1:
                for j in range(1, len(l[i]), 2):
                    bags.append(l[i][j+1])
                    count += l[i][j] * inside_bags(l[i][j+1])
            else:
                return 1
    #print(color, bags)
    return count

print(inside_bags("shiny gold")-1)