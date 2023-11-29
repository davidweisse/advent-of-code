with open("day4_input.txt") as input:
    l = input.read().split('\n\n')
    l = [s.split() for s in l]

words = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]



valid1 = 0
valid = 0
for i in l:
    mandatory = words.copy()
    fields = 0
    for j in i:
        key = j[0:3]
        value = j[4:]
        if key == "byr":
            fields += 1
            if 1920 <= int(value) <= 2002:
                mandatory.remove("byr")
        if key == "iyr":
            fields += 1
            if 2010 <= int(value) <= 2020:
                mandatory.remove("iyr")
        if key == "eyr":
            fields += 1
            if 2020 <= int(value) <= 2030:
                mandatory.remove("eyr")
        if key == "hgt":
            fields += 1
            if value[len(value)-2:] == "cm" and 150 <= int(value[:len(value)-2]) <= 193:
                mandatory.remove("hgt")
            if value[len(value)-2:] == "in" and 59 <= int(value[:len(value)-2]) <= 76:
                mandatory.remove("hgt")
        if key == "hcl":
            fields += 1
            if value[0] == "#":
                if len(value[1:]) == 6:
                    isvalid = True
                    for k in value[1:]:
                        if k not in "0123456789abcdef":
                            isvalid = False
                    if isvalid:
                        mandatory.remove("hcl")
        if key == "ecl":
            fields += 1
            if value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                mandatory.remove("ecl")
        if key == "pid":
            fields += 1
            if len(value) == 9:
                isvalid = True
                for k in value:
                    if k not in "0123456789":
                        isvalid = False
                if isvalid:
                    mandatory.remove("pid")
    if fields == 7:
        valid1 += 1
    if mandatory == []:
        valid += 1

print(valid1)
print(valid)