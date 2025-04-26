"""
e = 2
d = ... # What we need to leak
N = ...
M = ...
R2 = 1
while True :
    R4 = R2 * M
    R4 = R4 % N
    R3 = d & 1
    R4 = R3 * R4
    R3 = R3 ^ 1
    R2 = R3 * R2
    R2 = R2 + R4
    M = pow(M, e, N)
    d = d >> 1
    if d == 0 :
        break
"""

# I solved this by going with the vibes :D

d = 0
with open("src/mille-fautes.txt", "r") as f :
    lines = f.readlines()
    j = 0
    for i in range(2, len(lines), 2):
        d |= ("False" in lines[i]) << (j)
        j += 1
        print(lines[i])
    print(d)