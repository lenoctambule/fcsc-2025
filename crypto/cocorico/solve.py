from pwn import *
from zlib import crc32 
import json

REMOTE = "chall.fcsc.fr"
PORT = 2150

# r = remote(REMOTE, PORT)
r = process(["python3", "./src/cocorico.py"])

context.log_level = "debug"

start = json.dumps({"name" : "tota", "admin" : False}).encode()
target = json.dumps({"name" : "toto", "admin" : "aaa"}).encode()

start += int.to_bytes(crc32(start), 4)
target += int.to_bytes(crc32(target), 4)

print(len(start), len(target))
print(start)
print(target)

assert(len(start) == len(target))


r.sendlineafter(b">>>", b"1")
r.sendlineafter(b"(y/n)", b"y")
r.sendlineafter(b"Name: ", b"tota")
r.recvline()

token = bytes.fromhex(r.recvline().decode().strip())
key =  bytes([a ^ b for a,b in zip(start, token)])

ct_target = bytes([a ^ b for a,b in zip(key, target)])

r.sendlineafter(b">>>", b"1")
r.sendlineafter(b"(y/n)", b"n")
r.sendlineafter(b"Token: ", ct_target.hex().encode())
r.recvline()
r.recvline()

