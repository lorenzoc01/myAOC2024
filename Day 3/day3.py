
#puzzle 1

with open("input.txt", "r") as f:
    e = f.read()

acc = 0
while True:
    c = e.find("mul(")
    if c == -1:
        break
    e = e[c+4:]
    a = e.find(",")
    num1 = e[:a]
    try:
        num1 = int(num1)
    except:
        continue
    e = e[a+1:]
    b = e.find(")")
    num2 = e[:b]
    try:
        num2 = int(num2)
    except:
        continue
    acc += num1*num2
print("p1:", acc)


#puzzle 2

with open("input.txt", "r") as f:
    e = f.read()
    
wait_for_do = False
acc = 0
while True:
    if wait_for_do:
        do = e.find("do()")
        if do == -1:
            break
        e = e[do+4:]
        wait_for_do = False
    dont = e.find("don't()")
    c = e.find("mul(")
##    print(dont, c)
    if dont != -1 and c > dont:
        e = e[dont+7:]
        wait_for_do = True
        continue
    if c == -1:
        break
    e = e[c+4:]
    a = e.find(",")
    num1 = e[:a]
    try:
        num1 = int(num1)
    except:
        continue
    e = e[a+1:]
    b = e.find(")")
    num2 = e[:b]
    try:
        num2 = int(num2)
    except:
        continue
    acc += num1*num2
##    print(num1, num2)
print("p2:", acc)
    
        
        
