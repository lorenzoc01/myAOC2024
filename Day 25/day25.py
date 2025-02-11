
#puzzle 1

with open("input.txt", "r") as f:
    s = f.read()


everything = []
lst = []
for e in s.splitlines():
    if e == "":
        everything.append(tuple(lst))
        lst = []
    else:
        lst.append(tuple((m for m in e)))
        
everything.append(tuple(lst))
        

keys = []
locks = []
for e in everything:
    if e[0][0] == "#":
        locks.append(e)
    else:
        keys.append(e)

acc = 0
for k in keys:
    kh = []
    for c in range(len(k[0])):
        h = 0
        for r in range(len(k)):
            h += k[r][c] == "#"
        h -= 1
        kh.append(h)
        
    for l in locks:
        lh = []
        for c in range(len(l[0])):
            h = 0
            for r in range(len(l)):
                h += l[r][c] == "#"
            h -= 1
            lh.append(h)
        for a, b in zip(kh, lh):
            if a + b > 5:
                break
        else:
            acc += 1

print("p1:", acc)
