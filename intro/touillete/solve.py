with open("src/output.txt") as f:
    ct = f.read().strip()
    pt = ["a"] * len(ct)
    flag = "".join([b + a for a, b in zip(ct[:32], ct[32:])])
    x = "".join([
        flag[-8::-8],
        flag[-7::-8],
        flag[-6::-8],
        flag[-5::-8],
        flag[-4::-8],
        flag[-3::-8],
        flag[-2::-8],
        flag[-1::-8],
    ])[::-1]
    print(x)