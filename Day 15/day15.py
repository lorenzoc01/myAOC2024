
#puzzle 1

with open("input.txt", "r") as f:
	s = f.read()

ch = False
mov = ""
mat = []
for e in s.splitlines():
    if e == "":
        ch = True
    elif ch:
        mov += e
    else:
        mat.append([m for m in e])
        
rows = len(mat)
cols = len(mat[0])
for r in range(rows):
    for c in range(cols):
        if mat[r][c] == "@":
            plr = r
            plc = c
            break

def move(fr, fc, tr, tc):
    if mat[tr][tc] == ".":
        mat[tr][tc] = mat[fr][fc]
        mat[fr][fc] = "."
        return True
    elif mat[tr][tc] == "#":
        return False
    else:
        if move(tr, tc, tr+tr-fr, tc+tc-fc):
            mat[tr][tc] = mat[fr][fc]
            mat[fr][fc] = "."
            return True
        else:
            return False

for m in mov:
    if m == "^":
        if move(plr, plc, plr-1, plc):
            plr = plr-1
    elif m == "v":
        if move(plr, plc, plr+1, plc):
            plr = plr+1
    elif m == "<":
        if move(plr, plc, plr, plc-1):
            plc = plc-1
    elif m == ">":
        if move(plr, plc, plr, plc+1):
            plc = plc+1
        

acc = 0
for r in range(rows):
    for c in range(cols):
        if mat[r][c] == "O":
            acc += 100*r+c

print("p1:", acc)




#puzzle 2

with open("input.txt", "r") as f:
	s = f.read()

ch = False
mov = ""
mat = []
for e in s.splitlines():
    if e == "":
        ch = True
    elif ch:
        mov += e
    else:
        lst = []
        for m in e:
            if m == "O":
                lst.append("[")
                lst.append("]")
            elif m == "@":
                lst.append("@")
                lst.append(".")
            else:
                lst.append(m)
                lst.append(m)
        mat.append(lst)
        
rows = len(mat)
cols = len(mat[0])
for r in range(rows):
    for c in range(cols):
        if mat[r][c] == "@":
            plr = r
            plc = c
            break

def can_move(fr, fc, tr, tc):
    if mat[tr][tc] == ".":
        return True
    elif mat[tr][tc] == "#":
        return False
    else:
        if mat[tr][tc] == "[":
            return can_move(tr, tc, tr+tr-fr, tc+tc-fc) and can_move(tr, tc+1, tr+tr-fr, tc+tc-fc+1)
        elif mat[tr][tc] == "]":
            return can_move(tr, tc, tr+tr-fr, tc+tc-fc) and can_move(tr, tc-1, tr+tr-fr, tc+tc-fc-1)


def move(fr, fc, tr, tc):
    if mat[tr][tc] == ".":
        mat[tr][tc] = mat[fr][fc]
        mat[fr][fc] = "."
    elif mat[tr][tc] == "#":
        pass
    else:
        if mat[tr][tc] == "[":
            move(tr, tc, tr+tr-fr, tc+tc-fc)
            move(tr, tc+1, tr+tr-fr, tc+tc-fc+1)
            mat[tr][tc] = mat[fr][fc]
            mat[fr][fc] = "."
        elif mat[tr][tc] == "]":
            move(tr, tc, tr+tr-fr, tc+tc-fc)
            move(tr, tc-1, tr+tr-fr, tc+tc-fc-1)
            mat[tr][tc] = mat[fr][fc]
            mat[fr][fc] = "."

def move_normal(fr, fc, tr, tc):
    if mat[tr][tc] == ".":
        mat[tr][tc] = mat[fr][fc]
        mat[fr][fc] = "."
        return True
    elif mat[tr][tc] == "#":
        return False
    else:
        if move_normal(tr, tc, tr+tr-fr, tc+tc-fc):
            mat[tr][tc] = mat[fr][fc]
            mat[fr][fc] = "."
            return True
        else:
            return False

for m in mov:
    if m == "^":
        if can_move(plr, plc, plr-1, plc):
            move(plr, plc, plr-1, plc)
            plr = plr-1
    elif m == "v":
        if can_move(plr, plc, plr+1, plc):
            move(plr, plc, plr+1, plc)
            plr = plr+1
            
    elif m == "<":
        if move_normal(plr, plc, plr, plc-1):
            plc = plc-1
    elif m == ">":
        if move_normal(plr, plc, plr, plc+1):
            plc = plc+1    


acc = 0
for r in range(rows):
    for c in range(cols):
        if mat[r][c] == "[":
            acc += 100*r+c

print("p2:", acc)

















           

       
