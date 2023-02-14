# Import pygame
import time
import pygame
from pygame import mixer
import sys
import random


# VARIABLES
shopop = 1
shopopen = 0
collide = 0
wading = False
x = 0
y=0
tog = 0
D = 0
U = 0
L = 0
R = 0
cpos2 = 256
K = " "
Grid = []
itemsx = []
itemsy = []
currentitemx = []
currentitemy = []
Hotbar = (256,600)
itemid = []
itemnum = [0,0,0,0,0,0]
hotbaractive = 0
HY = 623
start = 281
times = 32
slot1 = (start+times*0,HY)
slot2 = (start+times*1,HY)
slot3 = (start+times*2,HY)
slot4 = (start+times*3,HY)
slot5 = (start+times*4,HY)
slot6 = (start+times*5,HY)
slots = [slot1, slot2, slot3, slot4, slot5, slot6]
HY = 657
start = 295
times = 29
anumbr1 = (start+times*0,HY)
bnumbr1 = (start+times*0+5,HY)
anumbr2 = (start+times*1,HY)
bnumbr2 = (start+times*1+5,HY)
anumbr3 = (start+times*2,HY)
bnumbr3 = (start+times*2+5,HY)
anumbr4 = (start+times*3,HY)
bnumbr4 = (start+times*3+5,HY)
anumbr5 = (start+times*4,HY)
bnumbr5 = (start+times*4+5,HY)
anumbr6 = (start+times*5,HY)
bnumbr6 = (start+times*5+5,HY)
anumbrs = [anumbr1, anumbr2, anumbr3, anumbr4, anumbr5, anumbr6]
bnumbrs = [bnumbr1, bnumbr2, bnumbr3, bnumbr4, bnumbr5, bnumbr6]
hotbarid = [" "," "," "," "," "," "]
hotbarslot = [0,0,0,0,0,0]
ebar = []
Electricity = 0
e1 = 0

for i in range(42):
    ebar.append("Electric" + str(i+1))


def Blit_EBAR(num):
    if not num < 42:
        e1 = pygame.image.load(str((str(ebar[41])+".png"))).convert_alpha()
    else:
        e1 = pygame.image.load(str((str(ebar[num])+".png"))).convert_alpha()
    e1 = pygame.transform.scale(e1, (128, 256))
    screen.blit(e1,(600,480))







# Init Pygame
pygame.init()

# Set window size
size = width,height = 700, 700
screen = pygame.display.set_mode(size)

# Clock
clock = pygame.time.Clock()

# Load image
image = pygame.image.load('GRASSFINAL.png').convert_alpha()
image2 = pygame.image.load('RESIZED.png').convert_alpha()
image3 = pygame.image.load('TreeTop.png').convert_alpha()
image6 = pygame.image.load('Stump.png').convert_alpha()
image5 = pygame.image.load('rocks.png').convert_alpha()
image7 = pygame.image.load('Stone.png').convert_alpha()
Wind1 = pygame.image.load('Wind-1.png').convert_alpha()
Wind2 = pygame.image.load('Wind-2.png').convert_alpha()
Wind3 = pygame.image.load('Wind-3.png').convert_alpha()
Wind4 = pygame.image.load('Wind-4.png').convert_alpha()
Wind5 = pygame.image.load('Wind-5.png').convert_alpha()
Wind6 = pygame.image.load('Wind-6.png').convert_alpha()
Wind7 = pygame.image.load('Wind-7.png').convert_alpha()
FRONT = pygame.image.load('FRONT.png').convert_alpha()
BACK = pygame.image.load('BACK.png').convert_alpha()
RIGHT = pygame.image.load('RIGHT.png').convert_alpha()
LEFT = pygame.image.load('LEFT.png').convert_alpha()
WFRONT = pygame.image.load('Wading-FRONT.png').convert_alpha()
WBACK = pygame.image.load('Wading-BACK.png').convert_alpha()
WRIGHT = pygame.image.load('Wading-RIGHT.png').convert_alpha()
WLEFT = pygame.image.load('Wading-LEFT.png').convert_alpha()
wooditem = pygame.image.load('Wood.png').convert_alpha()
HOTBAR = pygame.image.load('HOTBAR-1.png').convert_alpha()
n1 = pygame.image.load('Number-1.png').convert_alpha()
n2 = pygame.image.load('Number-2.png').convert_alpha()
n3 = pygame.image.load('Number-3.png').convert_alpha()
n4 = pygame.image.load('Number-4.png').convert_alpha()
n5 = pygame.image.load('Number-5.png').convert_alpha()
n6 = pygame.image.load('Number-6.png').convert_alpha()
n7 = pygame.image.load('Number-7.png').convert_alpha()
n8 = pygame.image.load('Number-8.png').convert_alpha()
n9 = pygame.image.load('Number-9.png').convert_alpha()
n0 = pygame.image.load('Number-0.png').convert_alpha()
MM = pygame.image.load('MM.png').convert_alpha()
RIVER = pygame.image.load('RIVER.png').convert_alpha()
numbers = [n0, n1, n2, n3, n4, n5, n6, n7, n8, n9]
shop1 = pygame.image.load("Shop1.png").convert_alpha()
shop2 = pygame.image.load("Shop2.png").convert_alpha()

# Set the size for the image
DEFAULT_IMAGE_SIZE = (3000,3000)
siziofor = (200,200)
TS = (250,250)
SS = (120,120)
HB = (270,100)
HT = (100,100)

# Scale the image to your needed size
image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)
image2 = pygame.transform.scale(image2, siziofor)
image3 = pygame.transform.scale(image3, TS)
image7 = pygame.transform.scale(image7, SS)
image6 = pygame.transform.scale(image6, TS)
image5 = pygame.transform.scale(image5, DEFAULT_IMAGE_SIZE)
RIVER = pygame.transform.scale(RIVER, (3000,480))
HOTBAR = pygame.transform.scale(HOTBAR, HB)
n1 = pygame.transform.scale(n1, HT)
n2 = pygame.transform.scale(n2, HT)
n3 = pygame.transform.scale(n3, HT)
n4 = pygame.transform.scale(n4, HT)
n5 = pygame.transform.scale(n5, HT)
n6 = pygame.transform.scale(n6, HT)
n7 = pygame.transform.scale(n7, HT)
n8 = pygame.transform.scale(n8, HT)
n9 = pygame.transform.scale(n9, HT)
MM = pygame.transform.scale(MM, (740,500))
shop1 = pygame.transform.scale(shop1,(512,512))
shop2 = pygame.transform.scale(shop2,(512,512))




# Set a default position
DEFAULT_IMAGE_POSITION = (0,0)
center = screen.get_rect().center
cpos = (256,256)
# Prepare loop condition
running = True

#AUDIO
mixer.init()
mixer.music.load('Menu.mp3')
mixer.music.set_volume(0.2)
mixer.music.play()


#Tree Creation
tree_x = []
tree_y = []
stone_x = []
stone_y = []
count = 0
CY = 0
spacing = 80
Repeats = int((3000/spacing)-5)
for i in range(Repeats):
    for x in range(40):
        CX = count*spacing
        if random.randint(1,10) < 3:
            tree_x.append(CX)
            tree_y.append(CY)
        else:
            if random.randint(1,60) == 1:
                stone_x.append(CX-15)
                stone_y.append(CY+20)
        count+=1
    CX = 0
    count = 0
    CY +=spacing
TreeCurrentx = []
TreeCurrenty = []
print(tree_x,tree_y)


#Functions
def Blit_Trees(Type):
    TreeCurrentx.clear()
    TreeCurrenty.clear()
    for i in range(len(tree_x)):
        if Type == 1:
            screen.blit(image3,(tree_x[i]+x,tree_y[i]+y))
        else:
            screen.blit(image6,(tree_x[i]+x,tree_y[i]+y))
        TreeCurrentx.append(tree_x[i]+x)
        TreeCurrenty.append(tree_y[i]+y)
def Blit_Stones():
    for i in range(len(stone_x)):
            screen.blit(image7,(stone_x[i]+x,stone_y[i]+y))

def Blit_Items():
    for i in range(len(itemsx)):
        if itemid[i] == "wood":
            screen.blit(wooditem,(itemsx[i]+x,itemsy[i]+y))
        currentitemx.append(itemsx[i]+x)
        currentitemy.append(itemsy[i]+y)


def spawn_item(tempx,tempy,ID):
    for i in range (random.randint(3,15)):
        itemsx.append(tempx+(random.randint(50,150)))
        itemsy.append(tempy+(random.randint(50,150)))
        if ID == "1":
            itemid.append("wood")

def itempickup():
    global currentitemx
    global currentitemy
    global hotbarslot
    global hotbarid
    global hotbaractive
    for i in range(len(itemsx)):
        if currentitemx[i]-100 < cpos2+50 and currentitemx[i]-50 > cpos2-30:
            if currentitemy[i]-50 < cpos2+45 and currentitemy[i]-50 > cpos2-20:
                itemsx.remove(itemsx[i])
                itemsy.remove(itemsy[i])
                for o in range(6):
                    if itemid[o] == "wood":
                        if hotbarslot[o] == 0 or itemnum[o] < 99:
                            hotbarslot[o] = 1
                            hotbarid[o] = "wood"
                            itemnum[o] = itemnum[o] + 1
                            break
                hotbaractive = 1
                print(itemnum)

                break
    currentitemx = []
    currentitemy = []
    

def TreeCollide():
    counting = 0
    global collide
    for i in range(len(TreeCurrentx)):
        if TreeCurrentx[i] < cpos2+30 and TreeCurrentx[i] > cpos2-30:
            if TreeCurrenty[i]+65 < cpos2+45 and TreeCurrenty[i]+65 > cpos2-20:
                collide = 1
                spawn_item(tree_x[i],tree_y[i],"1")
                tree_x.remove(tree_x[i])
                tree_y.remove(tree_y[i])
    counting +=1



# Event loop
running = False
while running == False:
    screen.fill((3, 156, 35))
    screen.blit(MM, (0,100))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            running = True
            mixer.music.stop()
            mixer.music.load('Breezey.mp3')
            mixer.music.queue("An Autumn Wind.mp3","test",99999)
            mixer.music.play()
    pygame.display.flip()
while running:

    # Close window event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Background Color
    screen.fill((3, 156, 35))

    # Show the image

    screen.blit(image, DEFAULT_IMAGE_POSITION)
    screen.blit(image5, DEFAULT_IMAGE_POSITION)
    Blit_Stones()






    # Part of event loop

    clock.tick(60)
    DEFAULT_IMAGE_POSITION = (0+x, 0+y)

    if y > -1052 and y < -630:
        wading = True
    else:
        wading = False

    if shopopen == False:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if wading == False:
                    x-=4
                else:
                    x-=1.5
                K = "R"
            if event.key == pygame.K_LEFT:
                if wading == False:
                    x+=4
                else:
                    x+=1.5
                K = "L"
            if event.key == pygame.K_UP:
                if wading == False:
                    y+=4
                else:
                    y+=1.5
                K = "U"
            if event.key == pygame.K_DOWN:
                if wading == False:
                    y-=4
                else:
                    y-=1.5
                K = "D"
    else:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                    shopop = 1
            if event.key == pygame.K_DOWN:
                    shopop = 2




    TreeCollide()

    if collide == 1:
        if K == "R":
            x+=8
        if K == "L":
            x-=8
        if K == "U":
            y-=8
        if K == "D":
            y+=8
        collide = 0
    Blit_Items()
    Blit_Trees(0)
    screen.blit(RIVER, (0 + x, 972 + y))



    if K == "R":
        if wading == False:
            screen.blit(RIGHT, cpos)
        else:
            screen.blit(WRIGHT, cpos)
    elif K == "L":
        if wading == False:
            screen.blit(LEFT, cpos)
        else:
            screen.blit(WLEFT, cpos)
    elif K == "U":
        if wading == False:
            screen.blit(BACK, cpos)
        else:
            screen.blit(WBACK, cpos)
    else:
        if wading == False:
            screen.blit(FRONT, cpos)
        else:
            screen.blit(WFRONT, cpos)
    Blit_Trees(1)
    screen.blit(HOTBAR, Hotbar)
    Blit_EBAR(Electricity)
    itempickup()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                shopopen = not shopopen

    if shopopen:
        if shopop == 1:
            screen.blit(shop1, (100, 100))
        else:
            screen.blit(shop2, (100, 100))


    #Blitting Hotbar
    if hotbaractive == 1:
        for i in range(6):
            if hotbarid[i] == "wood":
                screen.blit(wooditem, slots[i])
                sep = [int(x) for x in str(itemnum[i])]
                if itemnum[i] > 1:
                    temp = numbers[sep[0]]
                    screen.blit(temp,anumbrs[i])
                if itemnum[i] > 9:
                    temp = numbers[sep[1]]
                    screen.blit(temp,bnumbrs[i])


    pygame.display.flip()
        

