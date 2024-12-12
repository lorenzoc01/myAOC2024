
#puzzle 1

with open("input.txt", "r") as f:
	s = f.read()

mat = []
for e in s.splitlines():
    mat.append([m for m in e])
rows = len(mat)
cols = len(mat[0])

pairs = []
fences = []
for r in range(rows):
    for c in range(cols):
        if c+1 < cols:
            if mat[r][c] == mat[r][c+1]:
                pairs.append(((r,c), (r,c+1)))
            else:
                fences.append(((r,c), (r,c+1)))
                fences.append(((r,c+1), (r,c)))
        if r+1 < rows:
            if mat[r][c] == mat[r+1][c]:
                pairs.append(((r,c), (r+1,c)))
            else:
                fences.append(((r,c), (r+1,c)))
                fences.append(((r+1,c), (r,c)))

groups = {}
for p1, p2 in pairs:
    if p1 in groups:
        groups[p1].add(p2)
    else:
        for k in groups:
            if p1 in groups[k]:
                groups[k].add(p2)
                break
        else:
            groups[p1] = set((p2,))

regs = []
for k in groups:
    groups[k].add(k)
    regs.append(groups[k])

while True:
    merged = False
    for reg in regs:
        for p in reg:
            for reg2 in regs:
                if reg == reg2:
                    continue
                if p in reg2:
                    reg.update(reg2)
                    regs.remove(reg2)
                    merged = True
                    break
            if merged:
                break
        if merged:
            break
    if not merged:
        break                
    

for r in range(rows):
    for c in range(cols):
        for reg in regs:
            if (r,c) in reg:
                break
        else:
            regs.append(set(((r,c),)))


## "caching"
with open("regs.txt", "w") as f:
    f.write(str(regs))

## restore from "cached"
from ast import literal_eval
with open("regs.txt", "r") as f:
    regs = literal_eval(f.read())

acc = 0
for reg in regs:
    fn = 0
    for p in reg:
        for f in fences:
            if f[0] == p:
                fn += 1
        if p[0] == 0:
            fn += 1
        if p[1] == 0:
            fn += 1
        if p[0] == rows-1:
            fn += 1
        if p[1] == cols-1:
            fn += 1
    cost = fn * len(reg)
    acc += cost

print("p1:", acc)


    

#puzzle 2

with open("input.txt", "r") as f:
	s = f.read()

mat = []
for e in s.splitlines():
    mat.append([m for m in e])
rows = len(mat)
cols = len(mat[0])

pairs = []
fences = []
for r in range(rows):
    for c in range(cols):
        if c+1 < cols:
            if mat[r][c] == mat[r][c+1]:
                pairs.append(((r,c), (r,c+1)))
            else:
                fences.append(((r,c), (r,c+1)))
                fences.append(((r,c+1), (r,c)))
        if r+1 < rows:
            if mat[r][c] == mat[r+1][c]:
                pairs.append(((r,c), (r+1,c)))
            else:
                fences.append(((r,c), (r+1,c)))
                fences.append(((r+1,c), (r,c)))

groups = {}
for p1, p2 in pairs:
    if p1 in groups:
        groups[p1].add(p2)
    else:
        for k in groups:
            if p1 in groups[k]:
                groups[k].add(p2)
                break
        else:
            groups[p1] = set((p2,))

regs = []
for k in groups:
    groups[k].add(k)
    regs.append(groups[k])

while True:
    merged = False
    for reg in regs:
        for p in reg:
            for reg2 in regs:
                if reg == reg2:
                    continue
                if p in reg2:
                    reg.update(reg2)
                    regs.remove(reg2)
                    merged = True
                    break
            if merged:
                break
        if merged:
            break
    if not merged:
        break                
    

for r in range(rows):
    for c in range(cols):
        for reg in regs:
            if (r,c) in reg:
                break
        else:
            regs.append(set(((r,c),)))

## "caching"
with open("regs.txt", "w") as f:
    f.write(str(regs))

## restore from "cached"
from ast import literal_eval
with open("regs.txt", "r") as f:
    regs = literal_eval(f.read())

acc = 0
for reg in regs:
    sn = 0
    for r in range(rows):        
        fen = list(sorted([e for e in reg if (e[0] == r and (e[0] == 0 or mat[e[0]-1][e[1]] != mat[e[0]][e[1]]))]))
        sides = []
        if fen:
            side = [fen[0]]
            for e in range(1, len(fen)):
                if fen[e][1] == side[-1][1]+1:
                    side.append(fen[e])
                else:
                    sides.append(side)
                    side = [fen[e]]
            sides.append(side)
            sn += len(sides)

    for c in range(cols):        
        fen = list(sorted([e for e in reg if (e[1] == c and (e[1] == 0 or mat[e[0]][e[1]-1] != mat[e[0]][e[1]]))]))
        sides = []
        if fen:
            side = [fen[0]]
            for e in range(1, len(fen)):
                if fen[e][0] == side[-1][0]+1:
                    side.append(fen[e])
                else:
                    sides.append(side)
                    side = [fen[e]]
            sides.append(side)
            sn += len(sides)

    for r in range(rows-1, -1, -1):        
        fen = list(sorted([e for e in reg if (e[0] == r and (e[0] == rows-1 or mat[e[0]+1][e[1]] != mat[e[0]][e[1]]))]))
        sides = []
        if fen:
            side = [fen[0]]
            for e in range(1, len(fen)):
                if fen[e][1] == side[-1][1]+1:
                    side.append(fen[e])
                else:
                    sides.append(side)
                    side = [fen[e]]
            sides.append(side)
            sn += len(sides)

    for c in range(cols-1, -1, -1):        
        fen = list(sorted([e for e in reg if (e[1] == c and (e[1] == cols-1 or mat[e[0]][e[1]+1] != mat[e[0]][e[1]]))]))
        sides = []
        if fen:
            side = [fen[0]]
            for e in range(1, len(fen)):
                if fen[e][0] == side[-1][0]+1:
                    side.append(fen[e])
                else:
                    sides.append(side)
                    side = [fen[e]]
            sides.append(side)
            sn += len(sides)

    cost = len(reg)*sn
    acc += cost

print("p2:", acc)


    












             
                 
               
