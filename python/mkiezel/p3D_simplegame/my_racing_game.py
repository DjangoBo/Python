import pygame, sys
from math import *
from pygame.locals import *
import random
from environment import *

# window
WIDTH, HEIGHT = 800, 700
win = pygame.display.set_mode((WIDTH, HEIGHT))
# player_car=pygame.image.load('player_car.png').convert_alpha()
pygame.font.init()
pygame.display.set_caption('Drive your own FERRARI 2019')
font = pygame.font.Font('freesansbold.ttf', 32)

pygame.draw.polygon(win, (90, 179, 0), [(0, 250), (0, 550), (350, 250)])
pygame.draw.polygon(win, (90, 179, 0), [(800, 250), (800, 550), (450, 250)])

pygame.draw.line(win, (255, 0, 0), (0, 550), (350, 250), 5)
pygame.draw.line(win, (255, 0, 0), (800, 550), (450, 250), 5)

pygame.draw.polygon(win, (50, 50, 255), [(0, 0), (0, 250), (800, 250), (800, 0)])
pygame.draw.circle(win, (255, 255, 42), (690, 100), 30)
# linie
x = 0
y = 375

# win = background.convert()
# other items
trap_1 = pygame.image.load('images/trap1.png')
trap_2 = pygame.image.load('images/trap2.png')
trap_3 = pygame.image.load('images/trap3.png')

typ = [trap_1,trap_2,trap_3]




cloud = pygame.image.load('images/cloud.png')
cy = 0
# loading car
car = pygame.image.load('images/player_car.png').convert_alpha()
car_l = pygame.image.load('images/player_car_l.png')
car_r = pygame.image.load('images/player_car_r.png')

car = pygame.transform.scale(car, (160, 82))
car_l = pygame.transform.scale(car_l, (160, 82))
car_r = pygame.transform.scale(car_r, (160, 82))

car_actual = car
 #################################################################################################################
traps = []

class Trap:
    def __init__(self,droga):
        self.spawn_x = x
        self.typ = typ[random.randint(0,2)]
        self.droga = droga
        self.scale = 0
        print("stworzyłem trapa")

    def updatescale(self):
        self.scale = int(x - self.spawn_x)
        #print(self.scale)

    def showtrap(self):
        if int(x)%500 < 40:
            pass
        else:
            trap = pygame.transform.scale(self.typ, (self.scale // 3, self.scale // 3))
            if self.droga == 0:
                win.blit(trap, (400 - self.scale, 200 + self.scale))
            elif self.droga == 1:
                win.blit(trap, (415 - (self.scale)//2, 200 + self.scale))
            elif self.droga == 2:
                win.blit(trap, (405, 200 + self.scale))
            else:
                win.blit(trap, (415 + (self.scale)//1.6, 200 + self.scale))

def checkcollisions():
    for i in Trap:
        print(1)
        pass



def drawline(x):
    pygame.draw.line(win, (255, 255, 255), (400, 250 + x / 1.1), (400, 255 + x * 1.2), (x // 25) + 1)







def main():
    global x, y, car_actual, cy, h1, h2, h3, h4, tre,a,color, trapy
    clock = pygame.time.Clock()
    clock.tick(50)

    while x >= 0:
        cy += 0.03
        pygame.event.get()
        keys = pygame.key.get_pressed()





        pygame.draw.polygon(win, (132, 132, 132), [(350, 250), (0, 550), (0, 700), (800, 700), (800, 551), (450, 250)])
        drawline(int(x % 500))
        drawline(int((x + 180) % 500))
        drawline(int((x + 360) % 500))

        ######
        #               TRAPS
        ######




  ##############################################################################################################################


        # chmury
        pygame.draw.polygon(win, (90, 179, 0), [(0, 250), (0, 550), (350, 250)])
        pygame.draw.polygon(win, (90, 179, 0), [(800, 250), (800, 550), (450, 250)])

        pygame.draw.polygon(win, (50, 50, 255), [(0, 0), (0, 250), (800, 250), (800, 0)])
        pygame.draw.circle(win, (255, 252, 42), (690, 100), 30)

        if (cy % 1000) - 200 < -190:
            h1 = random.randint(-30, 160)
        if ((cy + 240) % 1000) - 200 < -190:
            h2 = random.randint(-30, 160)
        if ((cy + 600) % 1000) - 200 < -190:
            h3 = random.randint(-30, 160)
        if ((cy + 850) % 1000) - 200 < -190:
            h4 = random.randint(-30, 160)

        win.blit(cloud, ((cy % 1000) - 200, h1))
        win.blit(cloud, (((cy + 240) % 1000) - 200, h2))
        win.blit(cloud, (((cy + 600) % 1000) - 200, h3))
        win.blit(cloud, (((cy + 850) % 1000) - 200, h4))

        # drzewaprawo
        if x % 1000 > 82:
            tre1 = pygame.transform.scale(tre[0], (int((x % 1000) / 4.5), int((x % 1000) / 4.5)))
            win.blit(tre1, (450 + (1.5 * (x % 1000)) / 4.5, 220 + int(0.7 * (x % 1000)) / 4.5))
        elif int(x % 1000) == 1:
            losujdrzewo(0)
        if (x + 333) % 1000 > 82:
            tre2 = pygame.transform.scale(tre[1], (int(((x + 333) % 1000) / 4.5), int(((x + 333) % 1000) / 4.5)))
            win.blit(tre2, (450 + (1.5 * ((x + 333) % 1000)) / 4.5, 220 + int(0.7 * ((x + 333) % 1000)) / 4.5))
        elif int((x + 333) % 1000) == 1:
            losujdrzewo(1)
        if (x + 666) % 1000 > 82:
            tre3 = pygame.transform.scale(tre[2], (int(((x + 666) % 1000) / 4.5), int(((x + 666) % 1000) / 4.5)))
            win.blit(tre3, (450 + (1.5 * ((x + 666) % 1000)) / 4.5, 220 + int(0.7 * ((x + 666) % 1000)) / 4.5))
        elif int((x + 666) % 1000) == 1:
            losujdrzewo(2)

        # drzewalewo
        if (x + 166) % 1000 > 82:
            tre4 = pygame.transform.scale(tre[3], (int(((x + 166) % 1000) / 4.5), int(((x + 166) % 1000) / 4.5)))
            win.blit(tre4, (320 - (2.5 * ((x + 166) % 1000)) / 4.5, 220 + int(0.7 * ((x + 166) % 1000)) / 4.5))
        elif int((x + 166) % 1000) == 1:
            losujdrzewo(3)
        if (x + 500) % 1000 > 82:
            tre5 = pygame.transform.scale(tre[4], (int(((x + 501) % 1000) / 4.5), int(((x + 500) % 1000) / 4.5)))
            win.blit(tre5, (320 - (2.5 * ((x + 500) % 1000)) / 4.5, 220 + int(0.7 * ((x + 500) % 1000)) / 4.5))
        elif int((x + 500) % 1000) == 1:
            losujdrzewo(4)
        if (x + 833) % 1000 > 82:
            tre6 = pygame.transform.scale(tre[5], (int(((x + 833) % 1000) / 4.5), int(((x + 833) % 1000) / 4.5)))
            win.blit(tre6, (320 - (2.5 * ((x + 833) % 1000)) / 4.5, 220 + int(0.7 * ((x + 833) % 1000)) / 4.5))
        elif int((x + 833) % 1000) == 1:
            losujdrzewo(5)


        if int(x)%500 < 1:
            trap = Trap(random.randint(0, 3))
            traps.append(trap)
            x += 1
        trap.updatescale()
        trap.showtrap()
#        if 359 < int(x)%500 < 360:
#            trapy = Trap(random.randint(0, 3))
#            traps.append(trapy)
#            x += 1
#        trapy.updatescale()
#        trapy.showtrap()

        x += 0.5

        # Movement controls

        if keys[K_LEFT]:
            if y > 35:
                y -= 1
            car_actual = car_l
        if keys[K_RIGHT]:
            if y < 606:
                y += 1
            car_actual = car_r
        if keys[K_DOWN]:
            x -= 0.2
        if keys[K_UP]:
            x += 0.2

        # showing score
        text = font.render('Score: ' + str(int(x)), True, (255, 0, 0))
        win.blit(text, pygame.Rect(10, 220, 10, 10))

        win.blit(car_actual, (y, 500))
        pygame.display.update()
        car_actual = car
        print((clock.get_fps()))


main()
