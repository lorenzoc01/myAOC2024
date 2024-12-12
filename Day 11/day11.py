
#puzzle 1

with open("input.txt", "r") as f:
	s = f.read()

lst = [int(e) for e in list(s.splitlines())[0].split(" ")]

dic = {}

for b in range(25):
    new = []

    for e in lst:
        if e in dic:
            new += dic[e]
        elif e == 0:
            new.append(1)
            dic[0] = [1]
        else:
            stre = str(e)
            n = len(stre)
            if n % 2 == 0:
                n1 = int(stre[:n//2])
                n2 = int(stre[n//2:])            
                new.append(n1)
                new.append(n2)
                dic[e] = [n1, n2]
            else:
                n1 = e*2024
                new.append(n1)
                dic[e] = [n1]
    lst = new
print("p1:", len(lst))


#puzzle 2

with open("input.txt", "r") as f:
	s = f.read()

olst = [int(e) for e in list(s.splitlines())[0].split(" ")]

dic = {}

ev = {}

for m in olst:
    lst = [m]
    for b in range(25):
        new = []

        rep = 0
        for e in lst:
            if e in dic:
                rep += 1
                new += dic[e]
            elif e == 0:
                new.append(1)
                dic[0] = [1]
            else:
                stre = str(e)
                n = len(stre)
                if n % 2 == 0:
                    n1 = int(stre[:n//2])
                    n2 = int(stre[n//2:])            
                    new.append(n1)
                    new.append(n2)
                    dic[e] = [n1, n2]
                else:
                    n1 = e*2024
                    new.append(n1)
                    dic[e] = [n1]
        lst = new
    ev[m] = tuple(lst)

olst = []
for k in ev:
    for v in ev[k]:
        if v not in ev:
            olst.append(v)

for m in olst:
    lst = [m]
    for b in range(25):
        new = []

        rep = 0
        for e in lst:
            if e in dic:
                rep += 1
                new += dic[e]
            elif e == 0:
                new.append(1)
                dic[0] = [1]
            else:
                stre = str(e)
                n = len(stre)
                if n % 2 == 0:
                    n1 = int(stre[:n//2])
                    n2 = int(stre[n//2:])            
                    new.append(n1)
                    new.append(n2)
                    dic[e] = [n1, n2]
                else:
                    n1 = e*2024
                    new.append(n1)
                    dic[e] = [n1]
        lst = new
    ev[m] = tuple(lst)

olst = []
for k in ev:
    for v in ev[k]:
        if v not in ev:
            olst.append(v)
            
for m in olst:
    lst = [m]
    for b in range(25):
        new = []

        rep = 0
        for e in lst:
            if e in dic:
                rep += 1
                new += dic[e]
            elif e == 0:
                new.append(1)
                dic[0] = [1]
            else:
                stre = str(e)
                n = len(stre)
                if n % 2 == 0:
                    n1 = int(stre[:n//2])
                    n2 = int(stre[n//2:])            
                    new.append(n1)
                    new.append(n2)
                    dic[e] = [n1, n2]
                else:
                    n1 = e*2024
                    new.append(n1)
                    dic[e] = [n1]
        lst = new
    ev[m] = tuple(lst)

lst = [int(e) for e in list(s.splitlines())[0].split(" ")]
acc = 0
for e in lst:
    part = 0
    for m in ev[e]:
        for n in ev[m]:
            part += len(ev[n])
    acc += part

print("p2:", acc)
