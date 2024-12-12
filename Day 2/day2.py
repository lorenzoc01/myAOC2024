
#puzzle 1

with open("input.txt", "r") as f:
    s = f.read()

n = 0
for e in s.splitlines():    
    safe = True
    lst = [int(m) for m in e.split(" ")]
    slst = sorted(lst)
    rslst = sorted(lst, reverse=True)

    equal1 = False
    for i, j in zip(lst, slst):
        if i != j:
            break
    else:
        equal1 = True

    equal2 = False
    for i, j in zip(lst, rslst):
        if i != j:
            break
    else:
        equal2 = True

    if equal1:
        for i in range(len(lst)-1):
            if lst[i+1]-lst[i] > 3 or lst[i+1] == lst[i]:
                safe = False
                break
    elif equal2:
        for i in range(len(lst)-1):
            if lst[i+1]-lst[i] < -3 or lst[i+1] == lst[i]:
                safe = False
                break
    else:
        safe = False

    if safe:
        n += 1
print("p1:", n)


#puzzle 2

with open("input.txt", "r") as f:
    s = f.read()

n = 0
for e in s.splitlines():
    olst = [int(m) for m in e.split(" ")]
    #print(olst)

    for to_pop in range(len(olst)):
        safe = True
        lst = [m for m in olst]
        lst.pop(to_pop)
        
        slst = sorted(lst)
        rslst = sorted(lst, reverse=True)

        equal1 = False
        for i, j in zip(lst, slst):
            if i != j:
                break
        else:
            equal1 = True

        equal2 = False
        for i, j in zip(lst, rslst):
            if i != j:
                break
        else:
            equal2 = True

        if equal1:
            for i in range(len(lst)-1):
                if lst[i+1]-lst[i] > 3 or lst[i+1] == lst[i]:
                    safe = False
                    break
        elif equal2:
            for i in range(len(lst)-1):
                if lst[i+1]-lst[i] < -3 or lst[i+1] == lst[i]:
                    safe = False
                    break
        else:
            safe = False

        if safe:
            #print("Safe removing "+str(olst[to_pop]))
            n += 1
            break

print("p2:", n)
