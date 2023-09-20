from pico2d import *
import math
open_canvas()

grass = load_image('grass.png')
character=load_image('character.png')
def runCircle():
    clear_canvas_now()
    grass.draw_now(800/2,30)
    character.draw_now(400,90)
    delay(1)
    

def runRectangle():
    pass

while(1):
    runCircle
    runRectangle
    break

close_canvas
