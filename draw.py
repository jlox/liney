from display import *

def draw_line( screen, x0, y0, x1, y1, color ):
    slope = (y1-y0)/((x1-x0)*1.0)
    if (slope > 0):
        if (slope < 1):
            if (x0<x1):
                oct1(screen, x0, y0, x1, y1, color)
            else:
                oct1(screen, x1, y1, x0, y0, color)
        else:
            if (x0<x1):
                oct2(screen, x0, y0, x1, y1, color)
            else:
                oct2(screen, x1, y1, x0, y0, color)
    else:
        if (slope > -1):
            if(x0<x1):
                oct4(screen, x0, y0, x1, y1, color)
            else:
                oct4(screen, x1, y1, x0, y0, color)
        else:
            if(x0<x1):
                oct3(screen, x0, y0, x1, y1, color)
            else:
                oct3(screen, x1, y1, x0, y0, color)

#slope is less than one, greater than 0
def oct1(screen, x0, y0, x1, y1, color):
    x = x0
    y = y0
    A = y1-y0
    B = -(x1-x0)
    d = (2*A) + B
    while (x <= x1):
        plot(screen, color, x, y)
        if (d>0):
            y+=1
            d+=(2*B)
        x+=1
        d+=(2*A)

#slope is greater than one
def oct2(screen, x0, y0, x1, y1, color):
    x = x0
    y = y0
    A = y1-y0
    B = -(x1-x0)
    d = A + (2*B)
    while (y <= y1):
        plot(screen, color, x, y)
        if (d<0):
            x+=1
            d+=(2*A)
        x+=1
        d+=(2*B)

#slope is less than -1
def oct3(screen, x0, y0, x1, y1, color):
    x = x0
    y = y0
    A = y1-y0
    B = -(x1 - x0)
    d = (2*A) - B
    while (x <= x1):
        plot(screen, color, x, y)
        if (d<0):
            y-=1
            d-=(2*B)
        x+=1
        d-=(2*A)


#slope is less than 0, greater than -1
def oct4(screen, x0, y0, x1, y1, color):
    x = x0
    y = y0
    A = y1-y0
    B = -(x1-x0)
    d = A - (2*B)
    while (y>=y1):
        plot(screen, color, x, y)
        if (d<0):
            x+=1
            d-=(2*A)
        x+=1
        d-=(2*B)

def up(screen, x0, y0, x1, y1, color):
    x = x0
    y = y0
    if (y<=y1):
        while (y<=y1):
            plot(screen, color, x, y)
            y+=1
    else:
        while (y1<=y):
            plot(screen, color, x, y)
            y-=1

def right(screen, x0, y0, x1, y1, color):
    x = x0
    y= y0
    if(x<=x1):
        while (x<=x1):
            plot(screen, color, x, y)
            x+=1
    else:
        while(x1<=x):
            plot(screen, color, x, y)
            x-=1
