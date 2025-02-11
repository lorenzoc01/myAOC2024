
#puzzle 1


with open("input.txt", "r") as f:
    s = f.read()

codes = list(s.splitlines())


arr_kp = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], [None, "0", "A"]]
kp_none_pos = (3, 0)

dist_kp = {}
for r in range(4):
    for c in range(3):
        for r1 in range(4):
            for c1 in range(3):
                if (r, c) != kp_none_pos and (r1, c1) != kp_none_pos:
                    dist_kp[(arr_kp[r][c], arr_kp[r1][c1])] = (r1-r, c1-c)


arr_ar = [[None, "^", "A"], ["<", "v", ">"]]
ar_none_pos = (0, 0)
dist_ar = {}
for r in range(2):
    for c in range(3):
        for r1 in range(2):
            for c1 in range(3):
                if (r, c) != ar_none_pos and (r1, c1) != ar_none_pos:
                    dist_ar[(arr_ar[r][c], arr_ar[r1][c1])] = (r1-r, c1-c)


def perm(m, ss=""):
    lst = set()
    if len(m):
        for e in range(len(m)):
            lst.update(perm(m[:e]+m[e+1:], ss+m[e]))
    else:
        return {ss}
    return lst


def dist(ss):
    tot = 0
    for e in range(len(ss)-1):
        d = dist_ar[(ss[e], ss[e+1])]
        tot += abs(d[0])+abs(d[1])
    return tot


acc = 0
for cod in codes:
    prev_num = "A"
    t1s = []
    t1sd = []
    for num in cod:
        dr, dc = dist_kp[(prev_num, num)]
        prev_num = num
        t1 = abs(dr)*("^" if dr < 0 else "v") + abs(dc)*("<" if dc < 0 else ">")
        t1s.append(t1)
        t1sd.append((dr, dc))

    final = []
    cp = (3, 2)
    for i, t1 in enumerate(t1s):
        fin_t1s = []
        for p in perm(t1):

            sp = cp
            not_valid = False
            for ch in p:
                if ch == "<":
                    sp = (sp[0], sp[1]-1)
                elif ch == ">":
                    sp = (sp[0], sp[1]+1)
                elif ch == "^":
                    sp = (sp[0]-1, sp[1])
                elif ch == "v":
                    sp = (sp[0]+1, sp[1])
                if sp == kp_none_pos:
                    not_valid = True
                    break
            if not_valid:
                continue
            
            
            p += "A"
            prev_num = "A"
            t2s = []
            for num in p:
                dr, dc = dist_ar[(prev_num, num)]
                prev_num = num
                t2 = abs(dr)*("^" if dr < 0 else "v") + abs(dc)*("<" if dc < 0 else ">")
                t2s.append(t2)

            fin_t2s = []
            for t2 in t2s:
                fin_t3s = []
                for p in perm(t2):

                    sp = (0, 2)
                    not_valid = False
                    for ch in p:
                        if ch == "<":
                            sp = (sp[0], sp[1]-1)
                        elif ch == ">":
                            sp = (sp[0], sp[1]+1)
                        elif ch == "^":
                            sp = (sp[0]-1, sp[1])
                        elif ch == "v":
                            sp = (sp[0]+1, sp[1])
                        if sp == ar_none_pos:
                            not_valid = True
                            break
                    if not_valid:
                        continue
                    
                    p += "A"
                    prev_num = "A"
                    trad3 = ""
                    for num in p:
                        dr, dc = dist_ar[(prev_num, num)]
                        prev_num = num
                        trad3 += abs(dr)*("^" if dr < 0 else "v") + abs(dc)*("<" if dc < 0 else ">") + "A"

                    fin_t3s.append((p, trad3))

                best = min(fin_t3s, key=lambda x: len(x[1]))
                fin_t2s.append(best)

            sm = "".join([e[0] for e in fin_t2s])
            sn = "".join([e[1] for e in fin_t2s])
                
            fin_t1s.append((sm, sn))

        best = min(fin_t1s, key=lambda x: len(x[1]))

        final.append(best)

        cp = (cp[0]+t1sd[i][0], cp[1]+t1sd[i][1])

    wf = "".join([e[1] for e in final])

    acc += len(wf)*int(cod.replace("A", ""))

print("p1:", acc)





with open("input.txt", "r") as f:
    s = f.read()

codes = list(s.splitlines())


arr_kp = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], [None, "0", "A"]]
kp_none_pos = (3, 0)

dist_kp = {}
for r in range(4):
    for c in range(3):
        for r1 in range(4):
            for c1 in range(3):
                if (r, c) != kp_none_pos and (r1, c1) != kp_none_pos:
                    dist_kp[(arr_kp[r][c], arr_kp[r1][c1])] = (r1-r, c1-c)


arr_ar = [[None, "^", "A"], ["<", "v", ">"]]
ar_none_pos = (0, 0)
dist_ar = {}
for r in range(2):
    for c in range(3):
        for r1 in range(2):
            for c1 in range(3):
                if (r, c) != ar_none_pos and (r1, c1) != ar_none_pos:
                    dist_ar[(arr_ar[r][c], arr_ar[r1][c1])] = (r1-r, c1-c)


def perm(m, ss=""):
    lst = set()
    if len(m):
        for e in range(len(m)):
            lst.update(perm(m[:e]+m[e+1:], ss+m[e]))
    else:
        return {ss}
    return lst


def dist(ss):
    tot = 0
    for e in range(len(ss)-1):
        d = dist_ar[(ss[e], ss[e+1])]
        tot += abs(d[0])+abs(d[1])
    return tot


pretrads = [('935A', '^^^AvvA<^Avv>A'), ('319A', '^A<<A^^>>AvvvA'), ('480A', '^^<<A^>AvvvA>A'), ('789A', '^^^<<A>A>AvvvA'), ('176A', '^<<A^^Av>>AvvA')]

for cod in codes:
    prev_num = "A"
    t1s = []
    t1sd = []
    for num in cod:
        dr, dc = dist_kp[(prev_num, num)]
        prev_num = num
        t1 = abs(dr)*("^" if dr < 0 else "v") + abs(dc)*("<" if dc < 0 else ">")
        t1s.append(t1)
        t1sd.append((dr, dc))

    print(pretrads[0])
    print(t1s)


rec = {('A', 0, 1): '>A',
       ('A', 0, 2): 'A',
       ('A', 1, 0): '>>^A',
       ('A', 1, 1): '^>A',
       ('A', 1, 2): '^A',
       ('^', 0, 1): 'A',
       ('^', 0, 2): '<A',
       ('^', 1, 0): '>^A',
       ('^', 1, 1): 'A',
       ('^', 1, 2): '<^A',
       ('>', 0, 1): 'v>A',
       ('>', 0, 2): 'vA',
       ('>', 1, 0): '>>A',
       ('>', 1, 1): '>A',
       ('>', 1, 2): 'A',
       ('v', 0, 1): 'vA',
       ('v', 0, 2): '<vA',
       ('v', 1, 0): '>A',
       ('v', 1, 1): 'A',
       ('v', 1, 2): '<A',
       ('<', 0, 1): 'v<A',
       ('<', 0, 2): 'v<<A',
       ('<', 1, 0): 'A',
       ('<', 1, 1): '<A',
       ('<', 1, 2): '<<A'}
                  

prpcs = {k: (0, 2) for k in range(26)}

cache = {}

def get_length(s, depth):        
    if (s, depth, prpcs[depth]) in cache:
        par_tot, pr, pc = cache[(s, depth, prpcs[depth])]
        prpcs[depth] = (pr, pc)
        return par_tot
        
    par_tot = 0
    if depth:
        for e in s:
            pr, pc = prpcs[depth]
            moves = rec[(e, pr, pc)]
            for m in moves:
                if m == "<":
                    pc -= 1
                elif m == ">":
                    pc += 1
                elif m == "v":
                    pr += 1
                elif m == "^":
                    pr -= 1
            prpcs[depth] = (pr, pc)
            par_tot += get_length(moves, depth-1)            
        
    else:
        for e in s:
            pr, pc = prpcs[depth]
            moves = rec[(e, pr, pc)]
            for m in moves:
                if m == "<":
                    pc -= 1
                elif m == ">":
                    pc += 1
                elif m == "v":
                    pr += 1
                elif m == "^":
                    pr -= 1
            prpcs[depth] = (pr, pc)
            par_tot += len(moves)

    cache[(s, depth, prpcs[depth])] = (par_tot, pr, pc)

    return par_tot

acc = 0
for cod, trad in pretrads:
    acc += get_length(trad, 24)*int(cod.replace("A", ""))

print("p2:", acc)
    








