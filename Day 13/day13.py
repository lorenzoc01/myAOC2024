
#puzzle 1

with open("input.txt", "r") as f:
	s = f.read()

ss = ""
for e in s.splitlines():
    if e == "":
        continue
    ss += e
    if e.startswith("Prize"):
        ss += "|"
    else:
        ss += "&"

acc = 0
for m in ss.split("|"):
    if not m:
        continue
    a, b, p = m.split("&")
    a = a[a.find(": ")+2:].replace("X+", "").replace("Y+", "")
    ax, ay = [int(e) for e in a.split(", ")]
    b = b[b.find(": ")+2:].replace("X+", "").replace("Y+", "")
    bx, by = [int(e) for e in b.split(", ")]
    p = p[p.find(": ")+2:].replace("X=", "").replace("Y=", "")
    px, py = [int(e) for e in p.split(", ")]

    sols = []
    for a in range(100):
        for b in range(100):
            if a*ax+b*bx == px and a*ay+b*by == py:
                sols.append((a, b))

    if sols:
        sol = min(sols, key=lambda x: 3*x[0]+x[1])
        
        cost = sol[0]*3+sol[1]
        acc += cost

print("p1:", acc)


#puzzle 2

with open("input.txt", "r") as f:
	s = f.read()

ss = ""
for e in s.splitlines():
    if e == "":
        continue
    ss += e
    if e.startswith("Prize"):
        ss += "|"
    else:
        ss += "&"


acc = 0
for m in ss.split("|"):
    if not m:
        continue
    a, b, p = m.split("&")
    a = a[a.find(": ")+2:].replace("X+", "").replace("Y+", "")
    ax, ay = [int(e) for e in a.split(", ")]
    b = b[b.find(": ")+2:].replace("X+", "").replace("Y+", "")
    bx, by = [int(e) for e in b.split(", ")]
    p = p[p.find(": ")+2:].replace("X=", "").replace("Y=", "")
    px, py = [int(e) for e in p.split(", ")]
    px += 10000000000000
    py += 10000000000000

    sols = []
    
    b = (py-px*ay/ax)/(by-bx*ay/ax)
    a = (px-b*bx)/ax
    b = round(b)
    a = round(a)

    if a*ax+b*bx == px and a*ay+b*by == py:
        sols.append((a,b))
        
    a = (py-px*by/bx)/(ay-ax*by/bx)
    b = (px-a*ax)/bx
    b = round(b)
    a = round(a)

    if a*ax+b*bx == px and a*ay+b*by == py:
        sols.append((a,b))        
        
    b = (px-py*ax/ay)/(bx-by*ax/ay)
    a = (py-b*by)/ay
    b = round(b)
    a = round(a)

    if a*ax+b*bx == px and a*ay+b*by == py:
        sols.append((a,b))
        
    a = (px-py*bx/by)/(ax-ay*bx/by)
    b = (py-a*ay)/by
    b = round(b)
    a = round(a)

    if a*ax+b*bx == px and a*ay+b*by == py:
        sols.append((a,b))

    if sols:
        sol = min(sols, key=lambda x: 3*x[0]+x[1])
        
        cost = sol[0]*3+sol[1]
        acc += cost


print("p2:", acc)
    
    
    
        
