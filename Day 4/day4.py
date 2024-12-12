
#puzzle 1

with open("input.txt", "r") as f:
    s = f.read()

acc = 0
#horiz
for e in s.splitlines():
    acc += e.count("XMAS")
    acc += e.count("SAMX")

#vertic
for m in zip(*s.splitlines()):
    e = "".join(m)
    acc += e.count("XMAS")
    acc += e.count("SAMX")    

#diag l to r
lst = list(s.splitlines())
lines = []
length = len(lst[0])
for off in range(length):
    line = ""
    for e in range(length):
        try:
            line += lst[off+e][e]
        except IndexError:
            pass
    lines.append(line)
for off in range(1, length):
    line = ""
    for e in range(length):
        try:
            line += lst[e][off+e]
        except IndexError:
            pass
    lines.append(line)

for e in lines:
    acc += e.count("XMAS")
    acc += e.count("SAMX")
    
#diag r to l
lst = list(s.splitlines())
lines = []
length = len(lst[0])
for off in range(length):
    line = ""
    for e in range(length):
        try:
            line += lst[off+e][length-1-e]
        except IndexError:
            pass
    lines.append(line)
for off in range(1, length):
    line = ""
    for e in range(length):
        try:
            line += lst[e][length-1-off-e]
        except IndexError:
            pass
    line = line[:-off]
    lines.append(line)

for e in lines:
    acc += e.count("XMAS")
    acc += e.count("SAMX")    
print("p1:", acc)


#puzzle 2

with open("input.txt", "r") as f:
    s = f.read()

mat = list(s.splitlines())
acc = 0
for r in range(len(mat)-2):
    for c in range(len(mat[r])-2):
        word1 = mat[r][c] + mat[r+1][c+1] + mat[r+2][c+2]
        word2 = mat[r][c+2] + mat[r+1][c+1] + mat[r+2][c]
        if (word1 == "MAS" or word1 == "SAM") and (word2 == "MAS" or word2 == "SAM"):
            acc += 1    
print("p2:", acc)

    


