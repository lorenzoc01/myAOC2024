
#puzzle 1

with open("input.txt", "r") as f:
	s = f.read()

rows = 71
cols = 71
mat = [[1 for e in range(cols)] for _ in range(cols)]
for i, e in enumerate(s.splitlines()):
    if i == 1024:
        break
    c,r = map(int, e.split(","))
    mat[r][c] = 0



rows += 2
cols += 2
for e in mat:
    e.insert(0, 0)
    e.append(0)
mat.append([0 for _ in range(cols)])
mat.insert(0, [0 for _ in range(cols)])

global curr_min, curr_sol
curr_min = float("inf")
curr_sol = None

p = (1, 1)
ER, EC = rows-2, cols-2

scores = {}

def go(path, cr, cc, d, sc):
    global curr_min, curr_sol
    
    if cr == ER and cc == EC:
        if sc < curr_min:
            curr_sol = path
            curr_min = sc
        return

    if sc > curr_min:
        return

    if d == 0: #est
        if mat[cr][cc+1]:
            if scores.get((cr, cc+1), float("inf")) > sc:
                scores[(cr, cc+1)] = sc
                go(path+((cr, cc+1),), cr, cc+1, 0, sc+1)
            
        if mat[cr-1][cc]:
            if scores.get((cr-1, cc), float("inf")) > sc:
                scores[(cr-1, cc)] = sc
                go(path+((cr-1, cc),), cr-1, cc, 1, sc+1)
        if mat[cr+1][cc]:
            if scores.get((cr+1, cc), float("inf")) > sc:
                scores[(cr+1, cc)] = sc
                go(path+((cr+1, cc),), cr+1, cc, 3, sc+1)

    elif d == 1: #nord         
        if mat[cr-1][cc]:            
            if scores.get((cr-1, cc), float("inf")) > sc:
                scores[(cr-1, cc)] = sc
                go(path+((cr-1, cc),), cr-1, cc, 1, sc+1)
            
        if mat[cr][cc+1]:            
            if scores.get((cr, cc+1), float("inf")) > sc:
                scores[(cr, cc+1)] = sc
                go(path+((cr, cc+1),), cr, cc+1, 0, sc+1)        
        if mat[cr][cc-1]:
            if scores.get((cr, cc-1), float("inf")) > sc:
                scores[(cr, cc-1)] = sc
                go(path+((cr, cc-1),), cr, cc-1, 2, sc+1)

    elif d == 2: #ovest
        if mat[cr][cc-1]:
            if scores.get((cr, cc-1), float("inf")) > sc:
                scores[(cr, cc-1)] = sc
                go(path+((cr, cc-1),), cr, cc-1, 2, sc+1)

        if mat[cr-1][cc]:
            if scores.get((cr-1, cc), float("inf")) > sc:
                scores[(cr-1, cc)] = sc
                go(path+((cr-1, cc),), cr-1, cc, 1, sc+1)       
        if mat[cr+1][cc]:
            if scores.get((cr+1, cc), float("inf")) > sc:
                scores[(cr+1, cc)] = sc
                go(path+((cr+1, cc),), cr+1, cc, 3, sc+1)

    else: #sud              
        if mat[cr+1][cc]:
            if scores.get((cr+1, cc), float("inf")) > sc:
                scores[(cr+1, cc)] = sc
                go(path+((cr+1, cc),), cr+1, cc, 3, sc+1)

        if mat[cr][cc+1]:
            if scores.get((cr, cc+1), float("inf")) > sc:
                scores[(cr, cc+1)] = sc
                go(path+((cr, cc+1),), cr, cc+1, 0, sc+1)                
        if mat[cr][cc-1]:
            if scores.get((cr, cc-1), float("inf")) > sc:
                scores[(cr, cc-1)] = sc
                go(path+((cr, cc-1),), cr, cc-1, 2, sc+1)


go(tuple(), *p, 0, 0)


ss = ""
for r in range(rows):
    for c in range(cols):
        if (r, c) in curr_sol:
            ss += "O"
        else:        
            ss += "#."[mat[r][c]]
    ss += "\n"

print("p1:", curr_min)







#puzzle 2

with open("input.txt", "r") as f:
	s = f.read()

rows = 71
cols = 71
mat = [[1 for e in range(cols)] for _ in range(cols)]
rows += 2
cols += 2
for e in mat:
    e.insert(0, 0)
    e.append(0)
mat.append([0 for _ in range(cols)])
mat.insert(0, [0 for _ in range(cols)])


p = (1, 1)
ER, EC = rows-2, cols-2


visited = set()
def get_nxt(cr, cc):
    nxt = []
    
    if cr == ER and cc == EC:
        return True

    if mat[cr][cc+1]:
        np = (cr, cc+1)
        if np not in visited:
            visited.add(np)
            nxt.append(np)            
    if mat[cr+1][cc]:
        np = (cr+1, cc)
        if np not in visited:
            visited.add(np)
            nxt.append(np)            
    if mat[cr-1][cc]:
        np = (cr-1, cc)
        if np not in visited:
            visited.add(np)
            nxt.append(np)            
    if mat[cr][cc-1]:
        np = (cr, cc-1)
        if np not in visited:
            visited.add(np)
            nxt.append(np)            
    return nxt

for i, e in enumerate(s.splitlines()):
    c,r = map(int, e.split(","))
    mat[r+1][c+1] = 0
    if i < 1024:
        continue
    visited.clear()
    queue = [p]
    while queue:
        q = queue.pop(0)
        nx = get_nxt(*q)
        if nx == True:
            break
        queue = nx+queue
    else:        
        break

print("p2:", e)

