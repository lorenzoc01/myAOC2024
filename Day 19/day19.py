
#puzzle 1

with open("input.txt", "r") as f:
	s = f.read()


towels = []
patterns = []
for i, e in enumerate(s.splitlines()):
    if i == 0:
        towels = e.split(", ")
    elif i > 1:
        patterns.append(e)

towels.sort(key=lambda x: -len(x))


def is_doable(p):
    for e in towels:
        if p.startswith(e):
            ns = p[len(e):]
            if ns:
                if is_doable(ns):
                    return True
            else:
                return True
    return False

acc = 0
for pa in patterns:
    if is_doable(pa):
        acc += 1
        
print("p1:", acc)




#puzzle 2

with open("input.txt", "r") as f:
	s = f.read()

towels = []
patterns = []
for i, e in enumerate(s.splitlines()):
    if i == 0:
        towels = e.split(", ")
    elif i > 1:
        patterns.append(e)

towels.sort(key=lambda x: -len(x))

comb_d = {}
def is_doable(p):
    comb = 0
    for e in towels:
        if p.startswith(e):
            ns = p[len(e):]
            if ns:
                if ns in comb_d:
                    comb += comb_d[ns]
                else:
                    comb_d[ns] = is_doable(ns)
                    comb += comb_d[ns]
            else:
                comb += 1
    return comb

acc = 0
for pa in patterns:
    com = is_doable(pa)
    acc += com
        
print("p2:", acc)


