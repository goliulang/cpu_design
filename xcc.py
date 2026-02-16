import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'Rom_op.bin')

"""
add a2, a1, a0
opcode 
0000***0 ***0 ***0
op = 0x000
op = pp | a2<<4 | a1<<4 | a0 << 8
"""

opcode_dict = {
"add" : 0b0000000000000001
}

regester_dict = {
"s0" : 0b000,
"x2" : 0b001,
"a0" : 0b010,
"a1" : 0b011,
"a2" : 0b100,
"a3" : 0b101,
"a4" : 0b110,
"ra" : 0b111,
}


HLT = 0x0000

micro = [HLT for _ in range(5)]

#add a2, a1, a0
#op = op | a2<<4 | a1<<8 | a0 << 12
opcode_tmp = opcode_dict["add"] | regester_dict["a2"]<<4 | regester_dict["a1"]<<8 | regester_dict["a0"]<<12

#binary_number = bin(opcode_tmp)
micro[0] = opcode_tmp
print(type(opcode_tmp), opcode_tmp)

#add a2, a4, a3
#op = op | a2<<4 | a3<<8 | a4 << 12
opcode_tmp = opcode_dict["add"] | regester_dict["a2"]<<4 | regester_dict["a3"]<<8 | regester_dict["a4"]<<12
micro[1] = opcode_tmp

print(type(opcode_tmp), opcode_tmp)


with open(filename, 'wb') as file:
        for value in micro:
            value = value.to_bytes(2, byteorder='little', signed=False)
            print(type(value), value)
            file.write(value)

print('Compile micro instruction finish!!!')
