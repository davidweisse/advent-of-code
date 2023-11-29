import time
import os

with open("input/day10_input.txt") as f:
    input = [x for x in f.read().splitlines()]

i = 0
reg = 1
sum = 0

crt = [["." for i in range(40)] for j in range(6)]

x = y = 0
pos = 1

def printx():
    os.system("cls")
    for row in crt:
        print("".join(row))
    time.sleep(0.01)

printx()
for instr in input:
    if abs(x - pos) <= 1:
        crt[y][x] = "#"
    printx()
    i += 1
    x = (x + 1) % 40
    if x == 0:
        y += 1
    if i in (20, 60, 100, 140, 180, 220): sum += i * reg
    if instr.split()[0] != "noop":
        if abs(x - pos) <= 1:
            crt[y][x] = "#"
        printx()
        i += 1
        x = (x + 1) % 40
        if x == 0:
            y += 1
        if i in (20, 60, 100, 140, 180, 220): sum += i * reg
        reg += int(instr.split()[1])
        pos = reg
    
print("\n\n")
print(sum)