from pwn import *
from src.assembly import assembly

context.log_level = "debug"
REMOTE = "chall.fcsc.fr"
PORT = 2300

r = remote(REMOTE, PORT)

code = open("program.asm", "r").readlines()
r.sendlineafter(b">>> ", assembly(code))
r.sendlineafter(b">>> ", b"1")
print(r.recvall().decode())

