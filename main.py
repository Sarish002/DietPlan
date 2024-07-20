import random
import time

import pygame
frameloop = 0
points = 0
pygame.init()
screen = pygame.display.set_mode((800, 500))
running = True
Clock = pygame.time.Clock()
lives = 5
LeftoverTime = time.time()
timeLim = 60
foodList = ['Burger.png', 'Cake.png', 'FrenchFries.png', 'IceCream.png',
            'MilkShake.png', 'PaniPuri.png', 'Samosa.png']
other = ['Chappathi.png', 'Dal.png', 'Fruits.png', 'FruitJuice.png', 'Milk.png', 'Rice.png', 'Sprouts.png', 'Veggies.png']
Panda = pygame.transform.scale(pygame.image.load('Panda.png'), (200, 200))
PandaRect = Panda.get_rect()
PandaRect.center = (75, 250)
sound = pygame.mixer.music.load('happy-african-village-69 (2).mp3')
pygame.mixer.music.play(-1)
class Burger:
    def __init__(self, file):
        self.image = pygame.transform.scale(pygame.image.load(file), (100, 100))
        self.BurgerRect = self.image.get_rect()
        self.BurgerRect.center = (900, random.randint(50, 350))
        if file in other:
            self.Health = True

        else:
            self.Health = False

Burger1 = Burger(random.choice([foodList[random.randint(0, 6)], other[random.randint(0, 7)]]))
F1 = pygame.font.Font('MotleyForcesRegular-w1rZ3.ttf', 30)
F2 = pygame.font.Font('VarelaRound-Regular.otf', 30)
pygame.display.flip()
while running:
    timevar = timeLim - ( - LeftoverTime + time.time())
    T1 = F1.render(f'Lives: {int(lives)}', False, 'black')
    T2 = F1.render(f'Points: {int(points)}', False, 'black')
    T3 = F2.render(f'Time: {(int(timevar) // 60):02}:{(int(timevar) % 60):02}', False, 'black')
    TRect = T1.get_rect()
    TRect.center = (300, 50)
    T2Rect = T2.get_rect()
    T2Rect.center = (500, 50)
    T3Rect = T3.get_rect()
    T3Rect.center = (400, 90)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill('white')
    screen.blit(T1, TRect)
    screen.blit(T2, T2Rect)
    screen.blit(T3, T3Rect)
    screen.blit(Panda, PandaRect)
    screen.blit(Burger1.image, Burger1.BurgerRect)
    Burger1.BurgerRect.x -= 7.5
    if Burger1.BurgerRect.x < -100:
        if not Burger1.Health:
            points += 2
            pygame.mixer.Sound('mixkit-achievement-bell-600.wav').play()
            Burger1.BurgerRect.x = 900
            Burger1.BurgerRect.y = random.randint(50, 450)
            Burger1 = Burger(random.choice([foodList[random.randint(0, 6)], other[random.randint(0, 7)]]))
        else:
            Burger1.BurgerRect.x = 900
            Burger1.BurgerRect.y = random.randint(50, 450)
            Burger1 = Burger(random.choice([foodList[random.randint(0, 6)], other[random.randint(0, 7)]]))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and PandaRect.y > 1:
        PandaRect.y -= 10
    elif keys[pygame.K_DOWN] and PandaRect.y < 300:
        PandaRect.y += 10

    if (PandaRect.colliderect(Burger1.BurgerRect)):
        if not Burger1.Health:
            lives -= (1 / 30)
            points -= (1 / 15)
            frameloop += 1
            if frameloop == 10:
                sound = pygame.mixer.Sound('eating-chips-81092.mp3')
                sound.play(1)

        else:
            points += (1/15)
            pygame.mixer.Sound('mixkit-achievement-bell-600.wav').play()

    if 1 > lives > 0:
        running = False
    if timevar < 0:
        running = False

    pygame.display.update()
    Clock.tick(60)