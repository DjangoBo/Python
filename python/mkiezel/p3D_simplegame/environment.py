import random
import pygame


tree1 = pygame.image.load('images/tree1.png')
tree2 = pygame.image.load('images/tree2.png')
tre = [tree1, tree2, tree1, tree2, tree1, tree2]

h1 = random.randint(-30, 160)
h2 = random.randint(-30, 160)
h3 = random.randint(-30, 160)
h4 = random.randint(-30, 160)

def losujdrzewo(x):
    if random.randint(0, 1) == 0:
        tre[x] = tree1
    else:
        tre[x] = tree2

def printennv(win):

    pass