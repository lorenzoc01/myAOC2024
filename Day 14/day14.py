
#puzzle 1

with open("input.txt", "r") as f:
	s = f.read()

class Robot:
    def __init__(self, px, py, vx, vy, sizex, sizey):
        self.px = px
        self.py = py
        self.vx = vx
        self.vy = vy
        self.sizex = sizex
        self.sizey = sizey

    def update(self, times=1):
        self.px += self.vx*times
        self.py += self.vy*times
        while self.px >= self.sizex:
            self.px -= self.sizex
        while self.py >= self.sizey:
            self.py -= self.sizey
        while self.px < 0:
            self.px += self.sizex
        while self.py < 0:
            self.py += self.sizey



sizex = 101
sizey = 103
bots = []
for e in s.splitlines():
    p, v = e.split(" ")
    p = p.replace("p=", "").split(",")
    p = tuple((int(e) for e in p))
    v = v.replace("v=", "").split(",")
    v = tuple((int(e) for e in v))
    robot = Robot(*p, *v, sizex, sizey)
    bots.append(robot)


for b in bots:
    b.update(100)

mat = [[0 for e in range(sizex)] for _ in range(sizey)]


limr = sizey//2
limc = sizex//2
q1, q2, q3, q4 = [], [], [], []
for r in range(sizey):
    if r < limr:
        q1.append([e for e in mat[r][:limc]])
        q2.append([e for e in mat[r][limc+1:]])
    elif r > limr:
        q3.append([e for e in mat[r][:limc]])
        q4.append([e for e in mat[r][limc+1:]])

s1 = 0
for r in q1:
    s1 += sum(r)
s2 = 0
for r in q2:
    s2 += sum(r)
s3 = 0
for r in q3:
    s3 += sum(r)
s4 = 0
for r in q4:
    s4 += sum(r)
acc = s1*s2*s3*s4

print("p1:", acc)




#puzzle 2

with open("input.txt", "r") as f:
	s = f.read()


class Robot:
    def __init__(self, px, py, vx, vy, sizex, sizey):
        self.px = px
        self.py = py
        self.vx = vx
        self.vy = vy
        self.sizex = sizex
        self.sizey = sizey

    def update(self, times=1):
        self.px += self.vx*times
        self.py += self.vy*times
        while self.px >= self.sizex:
            self.px -= self.sizex
        while self.py >= self.sizey:
            self.py -= self.sizey
        while self.px < 0:
            self.px += self.sizex
        while self.py < 0:
            self.py += self.sizey


sizex = 101
sizey = 103
bots = []
for e in s.splitlines():
    p, v = e.split(" ")
    p = p.replace("p=", "").split(",")
    p = tuple((int(e) for e in p))
    v = v.replace("v=", "").split(",")
    v = tuple((int(e) for e in v))
    robot = Robot(*p, *v, sizex, sizey)
    bots.append(robot)

import pygame
pygame.font.init()

imgx, imgy = 1920//sizex, 1080//sizey
win = pygame.display.set_mode((sizex*imgx, sizey*imgy))
FONT = pygame.font.SysFont("Segoe UI", 30)

x, y = 0, 0
for e in range(10403):    
    surf = pygame.Surface((sizex, sizey))
    surf.fill((0,0,0))
    
    for b in bots:
        b.update()
        surf.set_at((b.px, b.py), (255, 255, 255))

    surf.blit(FONT.render(str(e), True, (0, 255, 0) if e == 7343 else (255, 0, 0)), (0, 0))
    
    win.blit(surf, (x*sizex, y*sizey))
    x += 1
    if x == imgx:
        x = 0
        y += 1
    if y == imgy:
        x, y = 0, 0
        pygame.display.update()
        if e > 7343:
            break
        
    pygame.event.clear()

print("p2:", 7343)


        
        
    




        
