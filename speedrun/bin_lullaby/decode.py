ct = [0] * 19
with open("pt.txt", "r") as f:
    lines = f.readlines()
    for l in lines[:-1]:
        b = l.split()[0]
        p1 = [int(b[:8], 2)]
        p2 = [int(b[8:], 2)]
        j = int(l.split()[1])
        ct[j] = bytes(p1) + bytes(p2)
print(b''.join(ct).decode())