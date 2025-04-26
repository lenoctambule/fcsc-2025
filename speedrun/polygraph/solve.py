from z3 import *
from program import PROGRAM
import hashlib
from pwn import *

memory = [BitVec(0, 32) for i in range(10)]
input_bytes = [BitVec(f'input_{i}', 8) for i in range(16)]

solver = Solver()

eip = 1
for eip in range(1, len(PROGRAM), 3):
    INSTR = PROGRAM[eip - 1]
    PTR = PROGRAM[eip]
    PARAM = PROGRAM[eip + 1]

    if INSTR == 0xb:
        memory[PTR] = memory[PTR] + memory[PARAM]
    elif INSTR == 0x16:
        memory[PTR] = memory[PTR] - memory[PARAM]
    elif INSTR == 0x2c:
        memory[PTR] = memory[PTR] << (PARAM & 0x1f)
    elif INSTR == 0x37:
        memory[PTR] = LShR(memory[PTR], (PARAM & 0x1f))
    elif INSTR == 0x42:
        memory[PTR] = memory[PTR] * memory[PARAM]
    elif INSTR == 0x4d:
        memory[PTR] = memory[PTR] | memory[PARAM]
    elif INSTR == 0x58:
        memory[PTR] = ZeroExt(24, input_bytes[PARAM])
    elif INSTR == 0x63:
        memory[PTR] = memory[PTR] + PARAM
    else:
        print(f"BAD INSTRUCTION at {eip-1}: {hex(INSTR)}")
        break

solver.add(memory[0] == 0)

if solver.check() == sat:
    model = solver.model()
    print(model)
    solution = bytes([model[input_bytes[i]].as_long() for i in range(16)])
    print(f"{solution}")
else:
    print("no solution")
    exit()

import hashlib
from pwn import *

context.log_level = "debug"

with process("./src/polygraph.exe") as r :
    r.sendlineafter(">>>", solution)
    r.recvline()
    r.recvline()
h = hashlib.sha512(data).digest()
flag = "FCSC{" + ''.join(f"{b:02x}" for b in h) + "}"
print(flag)