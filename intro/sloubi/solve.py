ct = "4B}mCuCNJmeVhvCzQusFHS7{2gCBCrQW"
pt = ""
for i in range(len(ct)):
    pt += ct[(i * 17 + 51) % 32]
print(pt)