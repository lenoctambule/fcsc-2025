from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Util.number import long_to_bytes
from sympy.ntheory.modular import crt 

ret = []
mods = []
ct = b""
with open("src/output.txt") as f :
    lines = f.readlines()
    for i in range(5):
        ret.append(int(lines[i].split("=")[1]))
    ct = bytes.fromhex(lines[-1].split("=")[1].strip())
    
with open("src/carrote.py") as f:
    lines = f.readlines()
    for i in range(5,10):
        mods.append(int(lines[i].split("%")[1].strip()[:-1]))

ret = crt(mods, ret) 
key = long_to_bytes(ret[0])
E = AES.new(key, AES.MODE_ECB)
pt = unpad(E.decrypt(ct), 16).decode()
print(pt)
