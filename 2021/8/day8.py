with open("day8_input.txt") as input:
    l = input.read().split("\n")
    l = [s.split(" | ") for s in l]
    for i in range(len(l)):
        l[i] = [s.split() for s in l[i]]

number = 0
for row0, row1 in l:
    dic = {'a': None, 'b': None, 'c': None, 'd': None, 'e': None, 'f': None, 'g':  None}
    known = {0: None, 1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None}
    for num in row0:
        if len(num) == 2:
            known[1] = num
        if len(num) == 3:
            known[7] = num
        if len(num) == 4:
            known[4] = num
        if len(num) == 7:
            known[8] = num
    for c in known[7]:
        if c not in known[1]:
            dic['a'] = c
    for s in row0:
        if len(s) == 5:
            if known[1][0] in s and known[1][1] in s:
                known[3] = s
    dic['d'] = ""
    for c in known[3]:
        if c not in known[7]:
            dic['d'] += c
    for c in dic['d']:
        if c in known[4]:
            dic['d'] = c
    for s in row0:
        if len(s) == 6:
            if dic['d'] not in s:
                known[0] = s
    for s in row0:
        if len(s) == 6 and s != known[0]:
            count = 0
            for c in s:
                if c in known[1]:
                    count += 1
            if count == 2:
                known[9] = s
            elif count == 1:
                known[6] = s
    for s in row0:
        if len(s) == 5 and s != known[3]:
            count = 0
            for c in known[9]:
                if c not in s:
                    count += 1
            if count == 1:
                known[5] = s
            else:
                known[2] = s
    digits = [0, 0, 0, 0]
    for s in range(4):
        for j in range(10):
            if sorted(row1[s]) == sorted(known[j]):
                digits[s] = j
    value = digits[0]*1000 + digits[1]*100 + digits[2]*10 + digits[3]
    number += value
    print(row1, digits, value)
    print(number)
print(number)

'''
gea agfcbe egcbfd aecb cegbf cafgde fgeba ea gabdf begfdca | bcfeg ea fbdga fbgcdae
 7     9       6    4           0      3   1          8

   g
 aaaa
b    c
b    c
 dddd         <- b
e    f
e    f
 gggg

0 --    6n
1 --    2n
2 -- 5n
3 --    5n
4 --    4n
5 -- 5n
6 --    6n
7 --    3n
8 --    7n
9 --    6n

    a
b
c
    d
e
f
g
'''