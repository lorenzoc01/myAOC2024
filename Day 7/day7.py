
#puzzle 1

with open("input.txt", "r") as f:
	s = f.read()

acc = 0
for e in s.splitlines():
    res, other = e.split(":")
    other = other.strip().split(" ")
    res = int(res)
    other = [int(n) for n in other]
    for c in range(2**(len(other)-1)):
        w = str(bin(c)).split("b")[-1]
        while len(w) != len(other)-1:
            w = "0"+w
        par = other[0]        
        for i in range(len(w)):
            if w[i] == "0":
                par += other[i+1]
            else:
                par *= other[i+1]
        if par == res:
            acc += par
            break
print("p1:", acc)



#puzzle 2

with open("input.txt", "r") as f:
	s = f.read()

def ternary(n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))

acc = 0
ln = 0
tot = len(s.splitlines())
for e in s.splitlines():
    ln += 1
    if ln == 100:
        break
    print(ln, "/", tot)
    
    res, other = e.split(":")
    other = other.strip().split(" ")
    res = int(res)
    other = [int(n) for n in other]
    
    for c in range(3**(len(other)-1)):
        w = str(ternary(c))      
        
        while len(w) != len(other)-1:
            w = "0"+w
            
        par = other[0]        
        for i in range(len(w)):
            if w[i] == "0":
                par += other[i+1]
            elif w[i] == "1":
                par *= other[i+1]
            else:
                par = int(str(par)+str(other[i+1]))
                
        if par == res:
            acc += par
            break
        
print("p2:", acc)
