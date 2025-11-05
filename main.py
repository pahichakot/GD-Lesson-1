import pgzrun
from random import randint

WIDTH = 300
HEIGHT = 300
TITLE = "SCREEN"

#Draw function - inbuilt function gets called itself; helps to render animations/shapes/texts
def draw():
    screen.fill("black")
    width = WIDTH
    height = HEIGHT - 200
    r = 255
    g = 0
    b = randint(120,255)

    for i in range(20):
        myrect = Rect((0,0), (width,height))
        myrect.center = 150,150
        screen.draw.rect(myrect,(r,g,b))
        
        width = width - 10
        height = height + 10

        r = r - 10
        g = g + 10
        
pgzrun.go()