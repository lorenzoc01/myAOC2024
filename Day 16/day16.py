
#puzzle 1

with open("input.txt", "r") as f:
	s = f.read()
            
mat = []
for e in s.splitlines():
    line = []
    for m in e:
        if m == "#":
            m = 0
        elif m == ".":
            m = 1
        elif m == "E":
            m = 2
        elif m == "S":
            m = 1
        line.append(m)
    mat.append(line)
    

rows = len(mat)
cols = len(mat[0])
p = (rows-2, 1)
ER = 1
EC = cols-2

global curr_min, curr_sol
curr_min = float("inf")
curr_sol = None

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
                go(path+((cr-1, cc),), cr-1, cc, 1, sc+1001)
        if mat[cr+1][cc]:
            if scores.get((cr+1, cc), float("inf")) > sc:
                scores[(cr+1, cc)] = sc
                go(path+((cr+1, cc),), cr+1, cc, 3, sc+1001)

    elif d == 1: #nord         
        if mat[cr-1][cc]:            
            if scores.get((cr-1, cc), float("inf")) > sc:
                scores[(cr-1, cc)] = sc
                go(path+((cr-1, cc),), cr-1, cc, 1, sc+1)
            
        if mat[cr][cc+1]:            
            if scores.get((cr, cc+1), float("inf")) > sc:
                scores[(cr, cc+1)] = sc
                go(path+((cr, cc+1),), cr, cc+1, 0, sc+1001)        
        if mat[cr][cc-1]:
            if scores.get((cr, cc-1), float("inf")) > sc:
                scores[(cr, cc-1)] = sc
                go(path+((cr, cc-1),), cr, cc-1, 2, sc+1001)

    elif d == 2: #ovest
        if mat[cr][cc-1]:
            if scores.get((cr, cc-1), float("inf")) > sc:
                scores[(cr, cc-1)] = sc
                go(path+((cr, cc-1),), cr, cc-1, 2, sc+1)

        if mat[cr-1][cc]:
            if scores.get((cr-1, cc), float("inf")) > sc:
                scores[(cr-1, cc)] = sc
                go(path+((cr-1, cc),), cr-1, cc, 1, sc+1001)       
        if mat[cr+1][cc]:
            if scores.get((cr+1, cc), float("inf")) > sc:
                scores[(cr+1, cc)] = sc
                go(path+((cr+1, cc),), cr+1, cc, 3, sc+1001)

    else: #sud              
        if mat[cr+1][cc]:
            if scores.get((cr+1, cc), float("inf")) > sc:
                scores[(cr+1, cc)] = sc
                go(path+((cr+1, cc),), cr+1, cc, 3, sc+1)

        if mat[cr][cc+1]:
            if scores.get((cr, cc+1), float("inf")) > sc:
                scores[(cr, cc+1)] = sc
                go(path+((cr, cc+1),), cr, cc+1, 0, sc+1001)                
        if mat[cr][cc-1]:
            if scores.get((cr, cc-1), float("inf")) > sc:
                scores[(cr, cc-1)] = sc
                go(path+((cr, cc-1),), cr, cc-1, 2, sc+1001)  


go(tuple(), *p, 0, 0)

print("p1:", curr_min)
    


#puzzle 2

with open("input.txt", "r") as f:
	s = f.read()
            
mat = []
for e in s.splitlines():
    line = []
    for m in e:
        if m == "#":
            m = 0
        elif m == ".":
            m = 1
        elif m == "E":
            m = 2
        elif m == "S":
            m = 1
        line.append(m)
    mat.append(line)
    

rows = len(mat)
cols = len(mat[0])
p = (rows-2, 1)
ex = (1, cols-2)
ER = 1
EC = cols-2

global curr_min2
curr_min2 = float("inf")

scores = {}

sols = {}

def go(path, cr, cc, d, sc):
    global curr_min2
    
    if cr == ER and cc == EC:
        if sc <= curr_min2:
            curr_min2 = sc
            if curr_min2 in sols:
                sols[curr_min2].update(path)
            else:
                sols[curr_min2] = set(path)     
        return

    if sc > curr_min2:
        return

    if d == 0: #est
        if mat[cr][cc+1]:
            if scores.get((cr, cc+1), float("inf")) >= sc-1000:
                scores[(cr, cc+1)] = sc
                go(path+((cr, cc+1),), cr, cc+1, 0, sc+1)
            
        if mat[cr-1][cc]:
            if scores.get((cr-1, cc), float("inf")) >= sc-1000:
                scores[(cr-1, cc)] = sc
                go(path+((cr-1, cc),), cr-1, cc, 1, sc+1001)
        if mat[cr+1][cc]:
            if scores.get((cr+1, cc), float("inf")) >= sc-1000:
                scores[(cr+1, cc)] = sc
                go(path+((cr+1, cc),), cr+1, cc, 3, sc+1001)

    elif d == 1: #nord         
        if mat[cr-1][cc]:            
            if scores.get((cr-1, cc), float("inf")) >= sc-1000:
                scores[(cr-1, cc)] = sc
                go(path+((cr-1, cc),), cr-1, cc, 1, sc+1)
            
        if mat[cr][cc+1]:            
            if scores.get((cr, cc+1), float("inf")) >= sc-1000:
                scores[(cr, cc+1)] = sc
                go(path+((cr, cc+1),), cr, cc+1, 0, sc+1001)        
        if mat[cr][cc-1]:
            if scores.get((cr, cc-1), float("inf")) >= sc-1000:
                scores[(cr, cc-1)] = sc
                go(path+((cr, cc-1),), cr, cc-1, 2, sc+1001)

    elif d == 2: #ovest
        if mat[cr][cc-1]:
            if scores.get((cr, cc-1), float("inf")) >= sc-1000:
                scores[(cr, cc-1)] = sc
                go(path+((cr, cc-1),), cr, cc-1, 2, sc+1)

        if mat[cr-1][cc]:
            if scores.get((cr-1, cc), float("inf")) >= sc-1000:
                scores[(cr-1, cc)] = sc
                go(path+((cr-1, cc),), cr-1, cc, 1, sc+1001)       
        if mat[cr+1][cc]:
            if scores.get((cr+1, cc), float("inf")) >= sc-1000:
                scores[(cr+1, cc)] = sc
                go(path+((cr+1, cc),), cr+1, cc, 3, sc+1001)

    else: #sud              
        if mat[cr+1][cc]:
            if scores.get((cr+1, cc), float("inf")) >= sc-1000:
                scores[(cr+1, cc)] = sc
                go(path+((cr+1, cc),), cr+1, cc, 3, sc+1)

        if mat[cr][cc+1]:
            if scores.get((cr, cc+1), float("inf")) >= sc-1000:
                scores[(cr, cc+1)] = sc
                go(path+((cr, cc+1),), cr, cc+1, 0, sc+1001)                
        if mat[cr][cc-1]:
            if scores.get((cr, cc-1), float("inf")) >= sc-1000:
                scores[(cr, cc-1)] = sc
                go(path+((cr, cc-1),), cr, cc-1, 2, sc+1001)  


go((p,), *p, 0, 0)

sol = sols[curr_min2]
sol.add(ex)

print("p2:", len(sol))
        
    



































