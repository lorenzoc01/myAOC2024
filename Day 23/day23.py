
#puzzle 1

with open("input.txt", "r") as f:
	s = f.read()


links = {}
for e in s.splitlines():
    a, b = e.split("-")
    if a in links:
        links[a].append(b)
    else:
        links[a] = [b]
    if b in links:
        links[b].append(a)
    else:
        links[b] = [a]


groups = set()

for e1 in links:
    for e2 in links[e1]:
        for e3 in links[e2]:
            if e1 in links[e3]:
                groups.add(tuple(sorted((e1, e2, e3))))

filt_gr = []
for e in groups:
    for m in e:
        if m.startswith("t"):
            filt_gr.append(e)
            break

print("p1:", len(filt_gr))



#puzzle 2

with open("input.txt", "r") as f:
	s = f.read()


links = {}
for e in s.splitlines():
    a, b = e.split("-")
    if a in links:
        links[a].append(b)
    else:
        links[a] = [b]
    if b in links:
        links[b].append(a)
    else:
        links[b] = [a]

groups = set()
for e in links:
    gr = set((e,))
    for e1 in links[e]:
        for e2 in gr:
            if e2 not in links[e1]:
                break
        else:
            gr.add(e1)
    groups.add(tuple(sorted(gr)))
        
best = max(groups, key=lambda x: len(x))

print("p2:", ",".join(best))








