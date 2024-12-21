
#puzzle 1

with open("input.txt", "r") as f:
	s = f.read()


for i, e in enumerate(s.splitlines()):
    if i == 0:
        a = int(e.split(" ")[-1])
    elif i == 1:
        b = int(e.split(" ")[-1])
    elif i == 2:
        c = int(e.split(" ")[-1])
    elif i == 4:
        pr = [int(m) for m in e.split(" ")[-1].split(",")]

output = []

i = 0
while True:
    try:
        code, op = pr[i], pr[i+1]
    except IndexError:
        break
    if op in (0, 1, 2, 3):
        cop = op
    elif op == 4:
        cop = a
    elif op == 5:
        cop = b
    elif op == 6:
        cop = c

    if code == 0: #adv
        a = a >> cop
    elif code == 1: #bxl
        b = b ^ op
    elif code == 2: #bst
        b = cop % 8
    elif code == 3: #jnz
        if a != 0:
            i = op
            continue
    elif code == 4: #bxc
        b = b ^ c
    elif code == 5: #out
        output.append(cop % 8)
    elif code == 6: #bdv
        b = a >> cop
    elif code == 7: #cdv
        c = a >> cop

    i += 2
        
print("p1:", ",".join(map(str, output)))


#puzzle 2 [INPUT BASED]

with open("input.txt", "r") as f:
	s = f.read()

for i, e in enumerate(s.splitlines()):
    if i == 0:
        a = int(e.split(" ")[-1])
    elif i == 1:
        b = int(e.split(" ")[-1])
    elif i == 2:
        c = int(e.split(" ")[-1])
    elif i == 4:
        pr = [int(m) for m in e.split(" ")[-1].split(",")]

dic = {}
for e in range(8):
    dic[e] = []
for m in range(8):
    b = (m % 8) ^ 1
    for e in range(2**b):
        st = m + 0b1000*e
        a = st

        b = (a % 8) ^ 1
        sh = b
        d = b ^ 5 ^ (a >> b)
        
        st = str(bin(st))[2:]
        while len(st) < sh+3:
            st = "0"+st

        dic[d].append(st)


exp_out = [e for e in pr]
exp_out.reverse()

candidates = []
def get_candidate(a, idx):
    if idx == len(exp_out):
        candidates.append(int(a, 2))
    else:
        for t in dic[exp_out[idx]]:
            sz = len(t)
            if sz > 3:
                if a.endswith(t[:-3]):
                    at = a+t[-3:]
                    get_candidate(at, idx+1)
            else:
                get_candidate(a+t, idx+1)
        

get_candidate(min(dic[exp_out[0]], key=lambda x: int(x, 2)), 1)

print("p2:", min(candidates))















