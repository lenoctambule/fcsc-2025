from ctypes import c_uint32
import sys

key_1 = b'\x7d\x2c\xb4\xe6\xa6\x53\x5c\x7e\x61\xf4\xd2\xc9\x4c\x6b\x11\xa5\x3f\x91\xad\xb4\xbb\xd8\x1c\x74\x19\xf8\xe3\x99\x81\xe7\x0a\xdd'
key_2 = b'\x14\xbc\x2d\x8a\xa9\x53\x5c\x19\x97\x0d\x4b\xc7\xdc\x92\x77\xa6\x30\x67\xa4\x2e\x22\x4e\x7c\x1e\x76\x0e\x83\x67\xe7\x81\xfa\x45'
not_flag = b'\x46\x43\x53\x43\x7b\x35\x75\x38\x6d\x31\x37\x5f\x37\x68\x31\x35\x2d\x34\x6e\x64\x7e\x31\x30\x30\x35\x33\x3d\x68\x34\x72\x64\x7d'

"""
1. Take hex string, convert to bytes and reverse
2. XOR with key_1
3. Carry flag add and add with key_2
"""
# print(len(key_1))
# print(len(not_flag))

ENDIANESS = 'big'

v19 = []
for i in range(0,32,4):
    n = int.from_bytes(not_flag[i:i+4], ENDIANESS)
    v19.append(n)
v19 = v19[::-1]

for i in range(0,32,4):
    n = int.from_bytes(key_2[i:i+4], ENDIANESS)
    res = v19[i//4] - n
    if res < 0:
        res -= 1
    v19[i//4] = c_uint32(res).value

raw = b""
for i in range(0, 32, 4):
    raw += v19[i // 4].to_bytes(4, ENDIANESS)

pt = b""
for i in range(len(raw)):
    pt += bytes([raw[i] ^ key_1[i]])

flag = ""
for i in range(len(pt)-1,-1,-1):
    flag += pt[i:i+1].hex()[::-1]

print(len(flag), file=sys.stderr)
print(f"FCSC{{{flag}}}")
