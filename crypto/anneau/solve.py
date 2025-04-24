import json
from math import gcd
from Crypto.Util.number import long_to_bytes

data = json.loads(open("src/output.txt").read())

ct = data["C"][0]["c"]
iv = data["C"][0]["iv"]
pt = data["data"]

a1 = pt[0]["m"] * pt[0]["iv"] - pt[0]["c"]
a2 = pt[1]["m"] * pt[1]["iv"] - pt[1]["c"]

s = gcd(a1, a2)
print(s)

flag = b""
bs = 64 // 8
for b in data["C"]:
    iv = b["iv"]
    c = b["c"]
    m = (c * pow(iv, -1, s)) % s
    flag += long_to_bytes(m)

print(flag)
