# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame


class player:

    land = 600

    def __init__(self, x, y):
        self.x = x
        self.y = self.land

    def movforward(self):
        self.x = self.x + 10

    def jump(self):
        self.y = self.y - 10

    def gravity(self):
        if self.y != self.land:
            self.y = self.y + 0.1


winWidth = 1200
winHeight = 720

screen = pygame.display.set_mode([winWidth, winHeight])
bg = pygame.image.load("img/background.png")
bg = pygame.transform.scale(bg, (2400, 720))
brick = pygame.image.load("img/ground.png")
brick = pygame.transform.scale(brick, (100, 100))
running = True
clock = pygame.time.Clock()


class Background:
    def __init__(self):
        self.x = 0
        self.y = 0

    def mov(self):
        if self.x > -2400:
            self.x = self.x - 0.5
        else:
            self.x = 2400


class Ground:
    def __init__(self):
        self.x = -25
        self.y = 600


bg1 = Background()
bg2 = Background()
bg2.x = bg1.x + 2400
groundList = []
t = 0
for i in range(27):
    g1 = Ground()
    g1.x = g1.x + t
    groundList.append(g1)
    t = t + 48
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    screen.blit(bg, (bg1.x, bg1.y))
    screen.blit(bg, (bg2.x, bg2.y))
    bg1.mov()
    bg2.mov()
    for ground in groundList:
        ground.x -= 1
        if ground.x < -90:
            ground.x += 48*(27)

    for ground in groundList:
        screen.blit(brick, (ground.x, ground.y))

    pygame.display.flip()
    clock.tick(200)

pygame.quit()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
