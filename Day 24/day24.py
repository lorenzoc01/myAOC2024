
#puzzle 1

with open("input.txt", "r") as f:
    s = f.read()

decl = {}
expr = {}
first =  True
for e in s.splitlines():
    if e == "":
        first = False
        continue

    if first:
        name, value = e.split(": ")
        value = bool(int(value))
        decl[name] = value
    else:
        exp, res = e.split(" -> ")
        exp = tuple(exp.split(" "))
        expr[res] = exp


while expr:
    for res in list(expr.keys()):
        f1, op, f2 = expr[res]
        if f1 in decl and f2 in decl:
            if op == "AND":
                val = decl[f1] and decl[f2]
            elif op == "OR":
                val = decl[f1] or decl[f2]
            elif op == "XOR":
                val = decl[f1] != decl[f2]
            decl[res] = val
            del expr[res]


res = int("".join(list(map(lambda x: str(int(x[1])), sorted({k:v for k,v in decl.items() if k.startswith("z")}.items(), reverse=True)))), 2)
print("p1:", res)



#puzzle 2 [DONE MANUALLY, INPUT BASED]

with open("input.txt", "r") as f:
    s = f.read()

fixes = [("tst", "z05"), ("sps", "z11"), ("z23", "frt"), ("pmd", "cgh")]
swaps = []
for fix in fixes:
    s = s.replace(" -> "+fix[0], "TO CHANGE")
    s = s.replace(" -> "+fix[1], " -> "+fix[0])
    s = s.replace("TO CHANGE", " -> "+fix[1])
    swaps.append(fix[0])
    swaps.append(fix[1])


trad = """wrs rem01
ktr rem02
vmr rem03
bbh rem04
pvb rem05
jkm rem06
pgn rem07
dws rem08
cvd rem09
cds rem10
hkc rem11
sps rem12
bvk rem13
vgk rem14
cqf rem15
vfj rem16
jkk rem17
nfd rem18
qdp rem19
mnv rem20
wbk rem21
gdq rem22
kmg rem23
jkv rem24
ckj rem25
cvh rem26
qcs rem27
mjq rem28
dbp rem29
npt rem30
rhn rem31
vdg rem32
pwv rem33
mdn rem34
hhc rem35
wjp rem36
dpv rem37
gcd rem38
rdj rem39
cnh rem40
qqj rem41
wgw rem42
pwc rem43
gmg rem44
"""

for e in range(1, 45):
    xe = "x"+("0"*(e < 10))+str(e)
    ye = "y"+("0"*(e < 10))+str(e)
    a = s.find(xe+" XOR "+ye)
    sub = None
    if a != -1:
        sub = s[a:].split("\n")[0]
    else:
        a = s.find(ye+" XOR "+xe)
        if a != -1:
            sub = s[a:].split("\n")[0]
    name = sub.split(" -> ")[-1]
    s = s.replace(name, "sum"+("0"*(e < 10))+str(e))


for e in range(1, 45):
    xe = "x"+("0"*(e < 10))+str(e)
    ye = "y"+("0"*(e < 10))+str(e)
    a = s.find(xe+" AND "+ye)
    sub = None
    if a != -1:
        sub = s[a:].split("\n")[0]
    else:
        a = s.find(ye+" AND "+xe)
        if a != -1:
            sub = s[a:].split("\n")[0]
    name = sub.split(" -> ")[-1]
    if not name.startswith("z"):
        s = s.replace(name, "and"+("0"*(e < 10))+str(e))


for e in trad.splitlines():
    if e and not e.startswith("#"):
        pre, new = e.split(" ")
        s = s.replace(pre, new)

odecl = {}
oexpr = {}
first =  True
for e in s.splitlines():
    if e == "":
        first = False
        continue

    if first:
        name, value = e.split(": ")
        value = bool(int(value))
        odecl[name] = value
    else:
        exp, res = e.split(" -> ")
        exp = tuple(exp.split(" "))
        oexpr[res] = exp


def expand(lst):
    for m in range(len(lst)):
        if lst[m] in oexpr and len(lst[m]) == 3:
            lst[m] = {lst[m]: list(oexpr[lst[m]])}
            expand(list(lst[m].values())[0])
    return lst


chain = {}    
for e in range(46):
    chain[e] = {e: list(oexpr["z"+("0"*(2-len(str(e))))+str(e)])}
    expand(list(chain[e].values())[0])

    
repl = {"', '": " ", ", '": " ", "', ": " ", "'": "", "[": "(", "]": ")", "xor": "^"}
for i in range(46):
    s = str(chain[i]).lower()
    for r in repl.items():
        s = s.replace(*r)
    si = "0"*(i < 10)+str(i)
        
    wrong = False
    if i == 0:
        if s != "{0: (y00 ^ x00)}":
            wrong = True
    elif i == 45:
        pass
    elif s not in ("{"+f"{i}: (sum{si} ^ rem{si})"+"}", "{"+f"{i}: (rem{si} ^ sum{si})"+"}"):
        wrong = True

    # helps to view where the problem is
##    if wrong:
##        print(s, "BAD")
##    else:
##        print(s)


# check if it works as expected
decl = {k:v for k, v in odecl.items()}
expr = {k:v for k, v in oexpr.items()}
while expr:
    for res in list(expr.keys()):
        f1, op, f2 = expr[res]
        if f1 in decl and f2 in decl:
            if op == "AND":
                val = decl[f1] and decl[f2]
            elif op == "OR":
                val = decl[f1] or decl[f2]
            elif op == "XOR":
                val = decl[f1] != decl[f2]
            decl[res] = val
            del expr[res]

x = int("".join(list(map(lambda x: str(int(x[1])), sorted({k:v for k,v in decl.items() if k.startswith("x")}.items(), reverse=True)))), 2)
y = int("".join(list(map(lambda x: str(int(x[1])), sorted({k:v for k,v in decl.items() if k.startswith("y")}.items(), reverse=True)))), 2)
z = int("".join(list(map(lambda x: str(int(x[1])), sorted({k:v for k,v in decl.items() if k.startswith("z")}.items(), reverse=True)))), 2)
assert x + y == z

print("p2:", ",".join(sorted(swaps)))









