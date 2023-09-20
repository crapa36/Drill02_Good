from pico2d import *
import math
open_canvas()

grass = load_image('grass.png')
character=load_image('character.png')

delay(1)

def renderAll(x,y):
    clear_canvas_now()
    grass.draw_now(800/2,30)
    character.draw_now(x, y)
    delay(0.01)

def runCircle():
    cx, cy, r = 400,300,200
    for degree in range(0,360,5):
        x=cx+r*math.cos(math.radians(degree))
        y=cy+r*math.sin(math.radians(degree))
        renderAll(x,y)

def runRectangle():
    for x in range(50, 750+1, 10):
       y=90
       renderAll(x,y)
    for y in range(90, 550+1, +10):
        x=750
        renderAll(x,y)

    for x in range(750, 50-1, -10):
        y=550
        renderAll(x,y)
    for y in range(550, 90-1, -10):
        x=50
        renderAll(x,y)

while True:
    #runCircle()
    runRectangle()
    break

close_canvas()