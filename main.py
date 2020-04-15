import pygame
import math
from pygame.locals import *

pygame.init()
screen=pygame.display.set_mode((1280,640))
white=(255,255,255)
black=(0,0,0)

def draw_line(x,y,L):
    pygame.draw.aaline(screen,black,(x,y),(x,y+L))

def ruler_b(y):
    for x in range(1,10):
        draw_line(120+int(500*math.log(x,10)),y,10)
    for x in range(1,5):
        draw_line(120+int(500*math.log(x+0.5,10)),y,8)
    for x in range(7,10):
        draw_line(120+int(500*math.log(x+0.5,10)),y,5)
    for x in range(1,20):
        draw_line(120+int(500*math.log(1+x/20.0,10)),y,5)
    for x in range(1,30):
        draw_line(120+int(500*math.log(2+x/10.0,10)),y,5)
    for x in range(1,10):
        draw_line(120+int(500*math.log(5+x/5.0,10)),y,5)
    for x in range(1,11):
        draw_line(620+int(500*math.log(x,10)),y,10)
    for x in range(1,5):
        draw_line(620+int(500*math.log(x+0.5,10)),y,8)
    for x in range(7,10):
        draw_line(620+int(500*math.log(x+0.5,10)),y,5)
    for x in range(1,20):
        draw_line(620+int(500*math.log(1+x/20.0,10)),y,5)
    for x in range(1,30):
        draw_line(620+int(500*math.log(2+x/10.0,10)),y,5)
    for x in range(1,10):
        draw_line(620+int(500*math.log(5+x/5.0,10)),y,5)
def ruler_t(y):
    for x in range(1,10):
        draw_line(1120+int(1000*math.log(math.tan(math.pi*x/36),10)),y,10)
    for x in range(6,45):
        draw_line(1120+int(1000*math.log(math.tan(math.pi*x/180),10)),y,7)
    for x in range(51,100):
        draw_line(1120+int(1000*math.log(math.tan(math.pi*x/1800),10)),y,4)
    for x in range(51,150):
        draw_line(1120+int(1000*math.log(math.tan(math.pi*x/900),10)),y,5)
    for x in range(61,90):
        draw_line(1120+int(1000*math.log(math.tan(math.pi*x/360),10)),y,4)
def ruler_d(y):
    for x in range(1,11):
        draw_line(120+int(1000*math.log(x,10)),y,10)
    for x in range(1,5):
        draw_line(120+int(1000*math.log(x+0.5,10)),y,8)
    for x in range(36,50):
        draw_line(120+int(1000*math.log(x/5,10)),y,5)
    for x in range(1,50):
        draw_line(120+int(1000*math.log(1+x/50.0,10)),y,4)
    for x in range(1,40):
        draw_line(120+int(1000*math.log(1+x/10.0,10)),y,7)
    for x in range(1,60):
        draw_line(120+int(1000*math.log(2+x/20.0,10)),y,4)
    for x in range(1,20):
        draw_line(120+int(1000*math.log(5+x/10.0,10)),y,5)

def ruler_l(y):
    for x in range(11):
        draw_line(120+100*x,y,10)
    for x in range(0,10):
        draw_line(170+100*x,y,9)
    for x in range(101):
        draw_line(120+10*x,y,7)
    for x in range(100):
        draw_line(125+10*x,y,5)
    
def ruler_s(y):
    for x in range(1,10):
        draw_line(1120+int(1000*math.log(math.sin(math.pi*x/18),10)),y,10)
    for x in range(8):
        draw_line(1120+int(1000*math.log(math.sin(math.pi*(x+0.5)/18),10)),y,8)
    for x in range(6,40):
        draw_line(1120+int(1000*math.log(math.sin(math.pi*x/180),10)),y,6)
    for x in range(51,100):
        draw_line(1120+int(1000*math.log(math.sin(math.pi*x/1800),10)),y,4)
    for x in range(51,100):
        draw_line(1120+int(1000*math.log(math.sin(math.pi*x/900),10)),y,4)
    for x in range(41,80):
        draw_line(1120+int(1000*math.log(math.sin(math.pi*x/360),10)),y,4)
    for x in range(41,60):
        draw_line(1120+int(1000*math.log(math.sin(math.pi*x/180),10)),y,5)

def ruler_ll1(y):
    for x in range(1,12):
        draw_line(2120+int(1000*math.log10(math.log(1+x/100))),y,10)
    for x in range(1,5):
        draw_line(2120+int(1000*math.log10(math.log(1+(x+0.5)/100))),y,8)
    for x in range(36,55):
        draw_line(2120+int(1000*math.log10(math.log(1+x/500))),y,5)
    for x in range(1,50):
        draw_line(2120+int(1000*math.log10(math.log(1.01+x/5000))),y,4)
    for x in range(1,10):
        draw_line(2120+int(1000*math.log10(math.log(1.01+x/1000))),y,6)
    for x in range(1,60):
        draw_line(2120+int(1000*math.log10(math.log(1.02+x/2000))),y,5)
    for x in range(1,20):
        draw_line(2120+int(1000*math.log10(math.log(1.05+x/1000))),y,5)


def ruler_ll2(y):
    for x in range(1,19):
        draw_line(1120+int(1000*math.log10(math.log(1+x/10))),y,10)
    for x in range(91,140):
        draw_line(1120+int(1000*math.log10(math.log(x/50))),y,5)
    for x in range(110,180):
        draw_line(1120+int(1000*math.log10(math.log(x/100))),y,6)
    for x in range(50,100):
        draw_line(1120+int(1000*math.log10(math.log(1+x/500))),y,4)
    for x in range(40,100):
        draw_line(1120+int(1000*math.log10(math.log(1+x/200))),y,4)
    
    
def run():
    screen.fill(white)
    '''
    ruler_l(20)
    ruler_b(60)
    ruler_d(80)
    ruler_t(110)
    ruler_s(150)
    '''
    ruler_ll1(190)
    ruler_d(210)
    ruler_ll2(170)
    pygame.display.update()



if __name__=='__main__':
    run()
