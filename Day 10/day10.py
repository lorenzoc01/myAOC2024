
#puzzle 1

with open("input.txt", "r") as f:
	s = f.read()

##s = """89010123
##78121874
##87430965
##96549874
##45678903
##32019012
##01329801
##10456732"""

mat = []
for e in s.splitlines():
    mat.append([int(p) for p in e])

rows = len(mat)
cols = len(mat[0])

dest = []
def search(i, j, n):
    if 0 <= i+1 < rows and 0 <= j < cols and mat[i+1][j] == n:
        if n == 9:
            dest.append((i+1, j))
        else:
            search(i+1, j, n+1)
    if 0 <= i-1 < rows and 0 <= j < cols and mat[i-1][j] == n:
        if n == 9:
            dest.append((i-1, j))
        else:
            search(i-1, j, n+1)
    if 0 <= i < rows and 0 <= j+1 < cols and mat[i][j+1] == n:
        if n == 9:
            dest.append((i, j+1))
        else:
            search(i, j+1, n+1)
    if 0 <= i < rows and 0 <= j-1 < cols and mat[i][j-1] == n:
        if n == 9:
            dest.append((i, j-1))
        else:
            search(i, j-1, n+1)

acc = 0
for r in range(rows):
    for c in range(cols):
        if mat[r][c] == 0:
            search(r, c, 1)
            acc += len(set(dest))
            dest.clear()
print("p1:", acc)
            


#puzzle 2

with open("input.txt", "r") as f:
	s = f.read()

mat = []
for e in s.splitlines():
    mat.append([int(p) for p in e])

rows = len(mat)
cols = len(mat[0])

dest = []
def search(i, j, n):
    if 0 <= i+1 < rows and 0 <= j < cols and mat[i+1][j] == n:
        if n == 9:
            dest.append((i+1, j))
        else:
            search(i+1, j, n+1)
    if 0 <= i-1 < rows and 0 <= j < cols and mat[i-1][j] == n:
        if n == 9:
            dest.append((i-1, j))
        else:
            search(i-1, j, n+1)
    if 0 <= i < rows and 0 <= j+1 < cols and mat[i][j+1] == n:
        if n == 9:
            dest.append((i, j+1))
        else:
            search(i, j+1, n+1)
    if 0 <= i < rows and 0 <= j-1 < cols and mat[i][j-1] == n:
        if n == 9:
            dest.append((i, j-1))
        else:
            search(i, j-1, n+1)

acc = 0
for r in range(rows):
    for c in range(cols):
        if mat[r][c] == 0:
            search(r, c, 1)
            acc += len(dest)
            dest.clear()
print("p2:", acc)
                
                    
            

