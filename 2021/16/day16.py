with open("day16_input.txt") as input:
    message = input.read().strip()

table = {
    ord('0') : '0000',
    ord('1') : '0001',
    ord('2') : '0010',
    ord('3') : '0011',
    ord('4') : '0100',
    ord('5') : '0101',
    ord('6') : '0110',
    ord('7') : '0111',
    ord('8') : '1000',
    ord('9') : '1001',
    ord('A') : '1010',
    ord('B') : '1011',
    ord('C') : '1100',
    ord('D') : '1101',
    ord('E') : '1110',
    ord('F') : '1111'
}

message = message.translate(table)
print(message)

i = 0

def literal():
    global i
    sum = ""
    end = False
    while not end:
        if message[i] == '0':
            end = True
        sum += message[i+1:i+5]
        i += 5
    return int(sum, 2)

#while i < len(message):
version = int(message[i:i+3], 2)
print(version)
i += 3
id = int(message[i:i+3], 2)
print(id)
i += 3
if id == 4:
    print(literal())
else:
    lid = message[i]
    print(lid)
    i += 1
    if lid == '0':
        bitlength = int(message[i:i+15], 2)
        #print(bitlength)
    elif lid == '1':
        npackets = int(message[i:i+11], 2)
        #print(npackets)