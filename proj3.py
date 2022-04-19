### Binary
# Input:    000 | 001 | 010 | 011 | 100 | 101 | 110 | 111
#           ---------------------------------------------
# Output:   110 | 101 | 001 | 000 | 011 | 010 | 111 | 100

### Hexadecimal
# Input:    0 | 1 | 2 | 3 | 4 | 5 | 6 | 7
#           ------------------------------
# Output:   6 | 5 | 1 | 0 | 3 | 2 | 7 | 4


#1
class Sbox:
    def __init__(self, input, output) -> None:
        self.input = input
        self.output = output

class Number:
    def __init__(self, num):
        self.bin = f'{num:03b}'
        self.hex = hex(num)
        self.val = num
        self.bits = self.buildBits()
    def buildBits(self):
        # bits[0] is always 0
        # x1 x2 x3 are in bits[1] bits[2] bits[3]
        bits = [0, None, None, None]
        for i in range(0, len(self.bin)):
            bits[i+1] = int(self.bin[i])
        return bits
    def __str__(self):
        result = ""
        result += f"Value:\t{self.val}\n"
        result += f"Binary:\t{self.bin}\n"
        result += f"Hex:\t{self.hex}\n"
        result += f"Bits:\t{self.bits}"
        return result

class Table:
    def __init__(self, sbox):
        self.sbox = sbox
    def buildTable(self):
        x = []

input = []
for i in range(8):
    input.append(Number(i))
output = [
    Number(0b110),
    Number(0b101),
    Number(0b001),
    Number(0b000),
    Number(0b011),
    Number(0b010),
    Number(0b111),
    Number(0b100),
]

box = Sbox(input, output)
for i in box.input:
    print(i, end="\n\n")
#2

#3


#4

def main():
    return

if __name__ == "__main__":
    main()