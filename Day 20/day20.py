

global curr_min, curr_sol, dest


#puzzle 1

with open("input.txt", "r") as f:
    s = f.read()
	

mat = []
for e in s.splitlines():
    mat.append([m for m in e])

rows = len(mat)
cols = len(mat[0])
for r in range(rows):
    for c in range(cols):
        if mat[r][c] == "E":
            ER, EC = r, c            
        elif mat[r][c] == "S":
            p = (r, c)

        if mat[r][c] == "#":
            mat[r][c] = 0
        else:
            mat[r][c] = 1


curr_min = float("inf")
curr_sol = None

scores = {}

def get_nxt(cr, cc, sc):
    global curr_min
    
    if cr == ER and cc == EC:
        if sc < curr_min:
            curr_min = sc
        return []

    if sc > curr_min:
        return []

    nxt = []
    if mat[cr+1][cc]:
        if scores.get((cr+1, cc), float("inf")) > sc:
            scores[(cr+1, cc)] = sc
            nxt.append((cr+1, cc, sc+1))
    if mat[cr][cc+1]:
        if scores.get((cr, cc+1), float("inf")) > sc:
            scores[(cr, cc+1)] = sc
            nxt.append((cr, cc+1, sc+1))
    if mat[cr-1][cc]:
        if scores.get((cr-1, cc), float("inf")) > sc:
            scores[(cr-1, cc)] = sc
            nxt.append((cr-1, cc, sc+1))
    if mat[cr][cc-1]:
        if scores.get((cr, cc-1), float("inf")) > sc:
            scores[(cr, cc-1)] = sc
            nxt.append((cr, cc-1, sc+1))
    return nxt


queue = get_nxt(*p, 0)
while queue:
    q = queue.pop(0)
    nx = get_nxt(*q)                    
    queue = nx + queue

orig_tm = curr_min

che = {}
for r in range(rows):
    for c in range(cols):
        if mat[r][c] == 0 and 0 < r < rows-1 and 0 < c < cols-1:
            scores = {}
            curr_min = float("inf")
            
            mat[r][c] = 1
            queue = get_nxt(*p, 0)
            while queue:             
                queue = get_nxt(*queue.pop(0)) + queue

            sav = orig_tm-curr_min
            if sav in che:
                che[sav] += 1
            else:
                che[sav] = 1
            
            mat[r][c] = 0

acc = 0
for k in che:
    if k >= 100:
        acc += che[k]

print("p1:", acc)



#puzzle 2

with open("input.txt", "r") as f:
    s = f.read()


def get_nxt(pat, cr, cc, sc):
    global curr_min, curr_sol, dest
    
    if (cr, cc) == dest:
        if sc < curr_min:
            curr_min = sc
            curr_sol = pat
        return []

    if sc > curr_min:
        return []

    nxt = []
    if mat[cr+1][cc]:
        if scores.get((cr+1, cc), float("inf")) > sc:
            scores[(cr+1, cc)] = sc
            nxt.append((cr+1, cc, sc+1))
    if mat[cr][cc+1]:
        if scores.get((cr, cc+1), float("inf")) > sc:
            scores[(cr, cc+1)] = sc
            nxt.append((cr, cc+1, sc+1))
    if mat[cr-1][cc]:
        if scores.get((cr-1, cc), float("inf")) > sc:
            scores[(cr-1, cc)] = sc
            nxt.append((cr-1, cc, sc+1))
    if mat[cr][cc-1]:
        if scores.get((cr, cc-1), float("inf")) > sc:
            scores[(cr, cc-1)] = sc
            nxt.append((cr, cc-1, sc+1))
    return nxt

def get_nxt_np(cr, cc, sc):
    global curr_min, dest
    
    if (cr, cc) == dest:
        if sc < curr_min:
            curr_min = sc
        return []

    if sc > curr_min:
        return []

    nxt = []
    if mat[cr+1][cc]:
        if scores.get((cr+1, cc), float("inf")) > sc:
            scores[(cr+1, cc)] = sc
            nxt.append((cr+1, cc, sc+1))
    if mat[cr][cc+1]:
        if scores.get((cr, cc+1), float("inf")) > sc:
            scores[(cr, cc+1)] = sc
            nxt.append((cr, cc+1, sc+1))
    if mat[cr-1][cc]:
        if scores.get((cr-1, cc), float("inf")) > sc:
            scores[(cr-1, cc)] = sc
            nxt.append((cr-1, cc, sc+1))
    if mat[cr][cc-1]:
        if scores.get((cr, cc-1), float("inf")) > sc:
            scores[(cr, cc-1)] = sc
            nxt.append((cr, cc-1, sc+1))
    return nxt


mat = []
for e in s.splitlines():
    mat.append([m for m in e])

rows = len(mat)
cols = len(mat[0])
for r in range(rows):
    for c in range(cols):
        if mat[r][c] == "E":
            EXIT = (r, c)
        elif mat[r][c] == "S":
            p = (r, c)

        if mat[r][c] == "#":
            mat[r][c] = 0
        else:
            mat[r][c] = 1


curr_min = float("inf")
curr_sol = None


def gen_rose(r, c):
    for dist in range(21):
        for dx in range(dist+1):
            a, b = r-dx, c+dist-dx
            if 0 <= a < rows and 0 <= b < cols:
                yield a, b
            a, b = r-dx, c+dx-dist
            if 0 <= a < rows and 0 <= b < cols:
                yield a, b
            a, b = r+dx, c+dist-dx
            if 0 <= a < rows and 0 <= b < cols:
                yield a, b
            a, b = r+dx, c+dx-dist
            if 0 <= a < rows and 0 <= b < cols:
                yield a, b

scores = {}
dest = EXIT
queue = [(*p, 0)]
while queue:
    queue = get_nxt_np(*queue.pop(0)) + queue
no_ch_sol = curr_min

sols = {}
for r1 in range(rows):
    for c1 in range(cols):
        if mat[r1][c1]:
            dest = EXIT
            curr_min = float("inf")
            curr_sol = None
            scores = {}
            queue = [(r1, c1, 0)]
            while queue:
                queue = get_nxt_np(*queue.pop(0)) + queue
            sols[(r1, c1)] = curr_min           

che = {}
for r in range(1, rows-1):
    for c in range(1, cols-1):
        if mat[r][c]:
            dest = (r, c)
            curr_min = float("inf")
            curr_sol = None
            scores = {}

            queue = [(*p, 0)]
            while queue:
                queue = get_nxt_np(*queue.pop(0)) + queue

            pre_score = curr_min

            for r1, c1 in gen_rose(r, c):
                if mat[r1][c1]:
                    sol_score = sols[(r1, c1)]
                    che[(r, c, r1, c1)] = pre_score + abs(r1-r) + abs(c1-c) + sol_score

cnt = {}
for k in che:
    kkk = no_ch_sol-che[k]
    if kkk in cnt:
        cnt[kkk] += 1
    else:
        cnt[kkk] = 1

acc = 0
for k in cnt:
    if k >= 100:
        acc += cnt[k]

print("p2:", acc)


