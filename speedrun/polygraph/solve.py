from z3 import *

with open("src/polygraph.exe", "rb") as f :
    key = f.read()
    start = key.find(b'\x16\x00\x00\x16\x01\x01\x16\x02\x02\x16\x03\x03\x16')
    key = key[start:start + 774 * 3]

i = 773
eip = 1

memory = [BitVec(f'mem_{i}', 32) for i in range(5)]  # 32-bit symbolic variables
input = [BitVec(f'input_{i}', 8) for i in range(17)]

solver = Solver()

while True:
    INSTR = key[eip - 1]
    PTR = key[eip]
    PARAM = key[eip + 1]

    if INSTR == 0xb :
        R1 = memory[PARAM]
        memory[PTR] += R1
        print(f"MEM[{PTR}] += R1 ({R1})")
    elif INSTR == 0x16 :
        memory[PTR] -= memory[PARAM]
        print(f"MEM[{PTR}] -= MEM[{PARAM}]")
    elif INSTR == 0x2c :
        memory[PTR] = LShR(memory[PTR], (PARAM & 0b11111))
        print(f"MEM[{PTR}] = MEM[{PTR}] << {PARAM & 0b11111}")
    elif INSTR == 0x37 :
        memory[PTR] = memory[PTR] >> (PARAM & 0b11111)
        print(f"MEM[{PTR}] = MEM[{PTR}] >> {PARAM & 0b11111}")
    elif INSTR == 0x42 :
        memory[PTR] *=  memory[PARAM]
        print(f"MEM[{PTR}] *= MEM[{PARAM}]")
    elif INSTR == 0x4d :
        memory[PTR] = memory[PTR] | memory[PARAM]
        print(f"MEM[{PTR}] |= MEM[{PARAM}]")
    elif INSTR == 0x58 :
        memory[PTR] = ZeroExt(24, input[PARAM])
        print(f"MEM[{PTR}] = INPUT[{PARAM}]")
    elif INSTR == 0x63 :
        R1 = PARAM
        memory[PTR] += R1
        print(f"MEM[{PTR}] += {PARAM}")
    else :
        print("BAD INSTRUCTION")
        break

    print(memory)
    i -= 1
    eip += 3
    if i == 0 :
        break

if solver.check() == sat:
    model = solver.model()
    solution = bytes([model[byte].as_long() for byte in input])
    print(f"Found valid input: {solution}")
else:
    print("No solution found.")