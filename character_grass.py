from pico2d import *
import math
open_canvas()

grass = load_image('grass.png')
character=load_image('character.png')

delay(1)
def runCircle():
    cx, cy, r = 400,300,200
    for degree in range(0,360,5):
        x=cx+r*math.cos(math.radians(degree))
        y=cy+r*math.sin(math.radians(degree))
        clear_canvas_now()
        grass.draw_now(800/2,30)
        character.draw_now(x, y)
        delay(0.05)

def runRectangle():
    for x in range(50, 750, 5):
       y=90
       clear_canvas_now()
       grass.draw_now(800/2,30)
       character.draw_now(x, y)
       delay(0.01)

while True:
    runCircle()
    runRectangle()
    break

close_canvas()