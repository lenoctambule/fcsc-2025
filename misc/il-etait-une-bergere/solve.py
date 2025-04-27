from pwn import *
from src.assembly import assembly

context.log_level = "debug"
HOST = "chall.fcsc.fr"
PORT = 2051

r = remote(HOST, PORT)
code = assembly(open("./sqrt.asm", "r").readlines())
r.sendlineafter(b">>> ", code)
r.recvall()
