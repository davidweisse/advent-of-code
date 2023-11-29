with open("day8_input.txt") as input:
    l = input.read().split()

for cmd in range(0, len(l), 2):
    if l[cmd] == "nop":
        l[cmd] = "jmp"
    elif l[cmd] == "jmp":
        l[cmd] = "nop"
    else:
        continue
    acc = 0
    cache = []
    i = 0
    while i not in cache and i < len(l)/2:
        cache.append(i)
        print(i, cache[len(cache)-5:])
        if l[i*2] == "acc":
            if l[i*2+1][:1] == '+':
                acc += int(l[i*2+1][1:])
            elif l[i*2+1][:1] == '-':
                acc -= int(l[i*2+1][1:])
            i += 1
        elif l[i*2] == "jmp":
            if l[i*2+1][:1] == '+':
                i += int(l[i*2+1][1:])
            elif l[i*2+1][:1] == '-':
                i -= int(l[i*2+1][1:])
        elif l[i*2] == "nop":
            i += 1
    if i >= len(l)/2:
        print(acc)
        break
    else:
        if l[cmd] == "nop":
            l[cmd] = "jmp"
        elif l[cmd] == "jmp":
            l[cmd] = "nop"