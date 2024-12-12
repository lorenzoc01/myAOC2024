
#puzzle 1

with open("input.txt", "r") as f:
	s = f.read()


mat = [[m for m in e] for e in s.splitlines()]

an = set()
rows = len(mat)
cols = len(mat[0])
for r in range(rows):
    for c in range(cols):
        if mat[r][c] != ".":
            p = mat[r][c]
            for r2 in range(r, rows):
                for c2 in range(cols):
                    if r2 == r and c2 == c:
                        continue

                    if mat[r2][c2] == p:
                        dr = r2-r
                        dc = c2-c

                        ar = r-dr
                        ac = c-dc
                        br = r2+dr
                        bc = c2+dc

                        if rows > ar >= 0 and cols > ac >= 0:
                            an.add((ar, ac))

                        if rows > br >= 0 and cols > bc >= 0:
                            an.add((br, bc))

print("p1:", len(an))



#puzzle 2

with open("input.txt", "r") as f:
	s = f.read()

mat = [[m for m in e] for e in s.splitlines()]

an = set()
rows = len(mat)
cols = len(mat[0])
for r in range(rows):
    for c in range(cols):
        if mat[r][c] != ".":
            p = mat[r][c]
            for r2 in range(r, rows):
                for c2 in range(cols):
                    if r2 == r and c2 == c:
                        continue

                    if mat[r2][c2] == p:
                        an.add((r, c))
                        an.add((r2, c2))
                        
                        dr = r2-r
                        dc = c2-c

                        ar = r-dr
                        ac = c-dc
                        while rows > ar >= 0 and cols > ac >= 0:
                            an.add((ar, ac))
                            ar -= dr
                            ac -= dc

                        br = r2+dr
                        bc = c2+dc                        
                        while rows > br >= 0 and cols > bc >= 0:
                            an.add((br, bc))
                            br += dr
                            bc += dc


print("p2:", len(an))




