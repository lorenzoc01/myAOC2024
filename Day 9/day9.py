
#puzzle 1

with open("input.txt", "r") as f:
	s = f.read()

disk = []
for e in s.splitlines():
    for m in e:
        disk.append(int(m))

exp = []
n = 0
for i, e in enumerate(disk):
    if i % 2 == 0:
        exp += [n]*e
        n += 1
    else:
        exp += ["."]*e

for n in range(len(exp)):
    found = False
    for e in range(n, len(exp)):
        d = exp[-1-e]
        if d != ".":
            found = -1-e
            break

    if not found:
        break

    to = exp.index(".")

    if to >= found+len(exp):
        break

    exp[to], exp[found] = exp[found], exp[to]

acc = 0
for i, e in enumerate(exp):
    if e == ".":
        break
    acc += i*e

print("p1", acc)


#puzzle 2

with open("input.txt", "r") as f:
	s = f.read()

disk = []
for e in s.splitlines():
    for m in e:
        disk.append(int(m))

exp = []
n = 0
for i, e in enumerate(disk):
    if i % 2 == 0:
        exp += [n]*e
        n += 1
    else:
        exp += ["."]*e

chr_d = [float("inf")]
e = 0
while True:
    if exp[-1-e] != ".":
        d = exp[-1-e]
        c = 1
        try:
            while exp[-1-e-c] == d:
                c += 1
        except IndexError:
            break

        if d < chr_d[-1]:
            chr_d.append(d)

            try:                
                to = ("".join([(g if g == "." else "_") for g in exp])).index("."*c)
                if to < -1-e+len(exp):
                    
                    for m in range(c):
                        exp[to+m] = d
                        exp[-1-e-m] = "."
                
            except ValueError:
                pass

        e += c
    else:
        e += 1

acc = 0
for i, e in enumerate(exp):
    if e == ".":
        continue
    acc += i*e

print("p2", acc)














