import json
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.Padding import unpad
from sympy.ntheory.modular import crt

with open("src/output.txt", "r") as f :
    data = json.loads(f.read())
    for d in data :
        iv, c, p, q, dp, dq = d
        iv = bytes.fromhex(iv)
        c = bytes.fromhex(c)
        a = pow(dp, -1 , p - 1)
        b = pow(dq, -1, q - 1)
        k = crt([p-1, q-1], [a, b])[0]
        k = SHA256.new(str(k).encode()).digest()
        E = AES.new(k, AES.MODE_CBC, iv=iv)
        print(unpad(E.decrypt(c), 16).decode(), end='')


