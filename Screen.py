import pygame, sys, mouse, statistics
from random import randint
from time import sleep, perf_counter


size = 1920,1080
black = 0,0,0
white = 255,255,255


count = perf_counter()
screen = pygame.display.set_mode(size)
mousee =  mouse.get_position()
mousex, mousey = mousee
placex, placey = mousee
screen.fill(black)
sleep(3)



times = []
for i in range(0,19):
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    mousee = mouse.get_position()
    mousex, mousey = mousee
    placex, placey = mousee
    while ((((placex-mousex)**2) + ((placey-mousey)**2))<250000):
        placex = randint(100,1630)
        placey = randint(100,930)
    pygame.draw.circle(screen, white,(placex, placey), 30)
    pygame.display.flip()
    st = perf_counter()
    while 1:
        mousee = mouse.get_position()
        mousex, mousey = mousee
        
        if ((((placex-mousex)**2) + ((placey-mousey)**2))<100000):
        	break
        else:
        	pass
        sleep(.1)
    fin = perf_counter()
    tottime = fin-st
    times.append(tottime)
print(*times)
print("AVG = ",statistics.mean(times),"    stdev", statistics.stdev(times))

