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
        self.box = dict(zip(input, output))
    def __str__(self):
        res = ''
        for i in self.box:
            res += f'{i.hex} | {self.box[i].hex}\n'
        return res

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
        self.box = sbox.box
        self.table = self.buildTable(0)
    
    def res(self, x, a):
        b = []
        for i in range(len(a.bits)):
            if a.bits[i] == 1:
                b.append(i)
        if (len(b) == 0):
            return 0
        x_res = b[0]
        for i in range(1, len(x.bits)):
            x_res = x_res ^ x.bits[i]
        return x_res

    def NL(self, a, b, box):
        yeses = 0
        a = Number(a)
        b = Number(b)
        for i in box:
            x_res = self.res(i, a)
            y_res = self.res(box[i], b)
            yeses += x_res == y_res

        return yeses

    def buildTable(self, dec):
        table = '     '
        for i in self.box:
            table += f'{i.hex:>5}'
        table += '\n'
        for i in self.box:
            line = f'{i.hex:>5}'
            for j in self.box:
                nl = self.NL(i.val, j.val, self.box) - dec
                line += f'{nl:>5}'
            table += line + '\n'
        self.table = table
        return table

    def __str__(self):
        return self.table

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
table = Table(box)
table.buildTable(4)
print(table)
    
#2

#3


#4

def main():
    return

if __name__ == "__main__":
    main()