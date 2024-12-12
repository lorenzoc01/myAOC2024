
#puzzle 1

with open("input.txt", "r") as f:
    s = f.read()

l1 = []
l2 = []
for e in s.splitlines():
    spl = e.split(" ")
    l1.append(int(spl[0]))
    l2.append(int(spl[-1]))

l1.sort()
l2.sort()

acc = 0
for a, b in zip(l1, l2):
    acc += abs(a-b)

##print("p1:", acc)


#puzzle 2

with open("input.txt", "r") as f:
    s = f.read()

l1 = []
l2 = []
for e in s.splitlines():
    spl = e.split(" ")
    l1.append(int(spl[0]))
    l2.append(int(spl[-1]))

l1.sort()
l2.sort()

acc = 0
for a in l1:
    n = l2.count(a)
    acc += n*a

print(acc)




