
#puzzle 1

with open("input.txt", "r") as f:
	s = f.read()

s1, s2 = s.split("\n\n")

rules = []
for e in s1.splitlines():
    rule = e
    rules.append(rule)

acc = 0
for e in s2.splitlines():
    seq = e.split(",")
    valid = True
    for n in range(len(seq)-1):
        a = seq[n]
        b = seq[n+1]
        if b+str("|")+a in rules:
            valid = False
            break
    if valid:
        n = len(seq)
        acc += int(seq[n//2])
print("p1:", acc)


#puzzle 2

with open("input.txt", "r") as f:
	s = f.read()

s1, s2 = s.split("\n\n")

rules = []
for e in s1.splitlines():
    rule = e
    rules.append(rule)
acc = 0
for e in s2.splitlines():
    seq = e.split(",")
    valid = True
    for n in range(len(seq)-1):
        a = seq[n]
        b = seq[n+1]
        if b+str("|")+a in rules:
            valid = False
            break
    if not valid:    
        valid = False
        while not valid:
            valid = True
            for n1 in range(len(seq)-1):
                broken = False
                for n2 in range(n1+1, len(seq)):
                    a = seq[n1]
                    b = seq[n2]
                    if b+str("|")+a in rules:
                        seq[n1], seq[n2] = seq[n2], seq[n1]
                        valid = False
                        broken = True
                        break
                if broken:
                    break            
        n = len(seq)
        acc += int(seq[n//2])

print("p2:", acc)
            
        
