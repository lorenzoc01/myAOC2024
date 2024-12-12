
#puzzle 1

with open("input.txt", "r") as f:
	s = f.read()


mat = []
g = None
for r, e in enumerate(s.splitlines()):
    mat.append([m for m in e])
    if "^" in e:
        g = (r, e.index("^"))

w = len(mat[0])
h = len(mat)

d = (-1, 0)

while True:
    mat[g[0]][g[1]] = "X"

    prev = tuple(g)
    g = (g[0]+d[0], g[1]+d[1])
    
    if g[0] < 0 or g[0] > h-1 or g[1] < 0 or g[1] > w-1:
        print("exited")
        break

    if mat[g[0]][g[1]] == "#":
        g = prev
        if d == (-1, 0):
            d = (0, 1)
        elif d == (0, 1):
            d = (1, 0)
        elif d == (1, 0):
            d = (0, -1)
        elif d == (0, -1):
            d = (-1, 0)

acc = 0
for r in mat:
    acc += r.count("X")
print("p1:", acc)
            
    

#puzzle 2

w, h = 130, 130

with open("input.txt", "r") as f:
	orig = f.read()

acc = 0
for i in range(h):
    print(i,"/ 130")
    
    for j in range(w):
        
        s = str(orig)

        mat = []
        g = None
        for r, e in enumerate(s.splitlines()):
            mat.append([m for m in e])
            if "^" in e:
                g = (r, e.index("^"))


        ss = mat[i][j]
        if ss != ".":
            continue

        mat[i][j] = "#"        

        d = (-1, 0)

        pa = set()

        while True:
            mat[g[0]][g[1]] = "X"            

            prev = tuple(g)
            g = (g[0]+d[0], g[1]+d[1])
            
            if g[0] < 0 or g[0] > h-1 or g[1] < 0 or g[1] > w-1:
                break

            if mat[g[0]][g[1]] == "#":
                g = prev
                if d == (-1, 0):
                    d = (0, 1)
                elif d == (0, 1):
                    d = (1, 0)
                elif d == (1, 0):
                    d = (0, -1)
                elif d == (0, -1):
                    d = (-1, 0)

            else:
                if (g, d) in pa:
                    acc += 1
                    break
                else:
                    pa.add((g, d))

print("p2:", acc)

