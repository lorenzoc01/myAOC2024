
#puzzle 1

with open("input.txt", "r") as f:
	s = f.read()


def get_next(e):
    e = (e ^ (e * 64)) % 16777216
    
    e = (e ^ (e // 32)) % 16777216    

    e = (e ^ (e * 2048)) % 16777216
    return e


acc = 0
for sec in s.splitlines():
    sec = int(sec)
    osec = sec
    for i in range(2000):
        sec = get_next(sec)
    acc += sec

print("p1:", acc)
    

#puzzle 2

with open("input.txt", "r") as f:
	s = f.read()
	

def get_next(e):
    e = (e ^ (e * 64)) % 16777216
    
    e = (e ^ (e // 32)) % 16777216    

    e = (e ^ (e * 2048)) % 16777216
    return e

seq = []
diff = []
for sec in s.splitlines():
    sec = int(sec)
    slst = [sec % 10]
    for _ in range(2000):
        sec = get_next(sec)
        slst.append(sec % 10)

    do = ["+"+str(slst[e+1]-slst[e]) if slst[e+1]-slst[e] > 0 else str(slst[e+1]-slst[e]) for e in range(len(slst)-1)]
    seq.append(slst)
    diff.append("".join(do))

def d_rep(pool, ss=""):
    if len(ss.replace("-", "").replace("+", "")) == 4:
        return {ss}
    else:
        res = set()
        for e in pool:
            res.update(d_rep(pool, ss+e))
        return res

results = {}

for s in d_rep(list(["+"+str(e) if e > 0 else str(e) for e in range(-9, 10)])):
    tot = 0
    for se, d in zip(seq, diff):        
        find = d.find(s)
        if find != -1:
            string = d[:find].replace("-", "").replace("+", "")            
            tot += se[len(string) + 4]            
    results[s] = tot
    
print("p2:", max(results.values()))

























    
    
    
