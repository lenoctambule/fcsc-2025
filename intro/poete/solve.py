from src.assembly import *
from pwn import *

context.log_level = "debug"
HOST = "chall.fcsc.fr"
PORT = 2304

r = process(["python3", "./src/proof-of-elapsed-time.py"])
# r = remote(HOST, PORT)

code = open("program.asm", "r").read().splitlines()
code = assembly(code)
print(len(code), code)
r.sendlineafter(b">>> ", code)
r.recvall()