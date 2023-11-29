with open("day6_input.txt") as input:
    l = input.read().split("\n\n")
    #l = [s.replace("\n", "") for s in l]
    l = [s.split() for s in l]

sum = 0

count = 0
for i in l:
    answers = []
    for p in i:
        for c in p:
            if c not in answers:
                answers.append(c)
    sum += len(answers)
    cache = []
    for c in answers:
        for p in i:
            if c not in p:
                if c not in cache:
                    cache.append(c)
                break
    for c in cache:
        answers.remove(c)
    count += len(answers)

print(sum)
print(count)