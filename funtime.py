from display import *
from draw import *
from random import randint

screen = new_screen()
color = [0, 0, 0]

for x in range(XRES):
    color[GREEN] = (x*randint(0, 63))%16
    color[RED] = randint(50, MAX_COLOR)
    color[BLUE]= randint(0, MAX_COLOR/2)
    draw_line(screen, XRES/3, YRES/2, x/3, YRES/2, color)

for n in range(XRES):
    color[RED] = 200
    color[GREEN] = randint(0,MAX_COLOR/2)
    color[BLUE] = randint(MAX_COLOR/2,MAX_COLOR)
    draw_line(screen, XRES/2 , YRES/3 , n/2 , YRES/3, color)

for y in range(YRES):
    color[RED] = randint(MAX_COLOR-10,MAX_COLOR)
    color[BLUE] = (x**randint(0,16))% 21
    color[GREEN] = randint(MAX_COLOR/3,MAX_COLOR)
    draw_line(screen, XRES/5 - 63 , YRES/7 , XRES/6 + 37, y**2 , color)
    
for y in range(YRES):
    color[RED] = randint(MAX_COLOR/2,MAX_COLOR)
    color[BLUE] = y % MAX_COLOR/2
    color[GREEN] = randint(0,MAX_COLOR/3)
    draw_line(screen, XRES/5 + 63 , YRES/7 , XRES/6 - 37 , y**2 , color)
save_ppm(screen,"oof.ppm")
