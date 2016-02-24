from display import *

def draw_line( screen, x0, y0, x1, y1, color ):
    pass

#slope is less than one, greater than 0
def oct1(x0, y0, x1, y1):
    x = x0
    y = y0
    A = y1-y0
    B = -(x1-x0)
    d = (2*A) + B
    while (x <= x1):
        plot(screen, 50, x, y)
        if (d>0):
            y+=1
            d+=(2*B)
        x+=1
        d+=(2*A)

#slope is greater than one
def oct2(x0, y0, x1, y1):
    x = x0
    y = y0
    A = y1-y0
    B = -(x1-x0)
    d = A + (2*B)
    while (y <= y1):
        plot (screen, 50, x, y)
        if (d<0):
            x+=1
            d+=(2*A)
        x+=1
        d+=(2*B)

#slope is less than -1
def oct3(x0, y0, x1, y1):
    x = x0
    y = y0
    A = y1-y0
    B = -(x1 - x0)
    d = (2*A) - B
    while (x <= x1):
        plot(screen, 50, x, y)
        if (d<0):
            y-=1
            d-=(2*B)
        x+=1
        d-=(2*A)


#slope is less than 0, greater than -1
def oct4(x0, y0, x1, y1):
    x = x0
    y = y0
    A = y1-y0
    B = -(x1-x0)
    d = A - (2*B)
    while (y>=y1):
        plot(screen, 50, x, y)
        if (d<0):
            x+=1
            d-=(2*A)
        x+=1
        d-=(2*B)
