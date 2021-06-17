import numpy as np
import pygame


class Obj(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img).convert()
        # self.image.convert_alpha()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.frame = 0

    def move(self, y):
        self.rect.y = y
        self.frame += 1


def main():
    dimX = 800
    dimY = 600
    pygame.init()
    screen = pygame.display.set_mode((dimX, dimY))
    pygame.display.set_caption("Ley de Lenz")
    fps = 24

    bg = pygame.image.load("background.png")
    screen.blit(bg, (0, 0))
    pygame.display.update()
    clock = pygame.time.Clock()

    obj1 = Obj(207, 20, "iman.png")
    obj2 = Obj(542, 20, "iman.png")
    objList = pygame.sprite.Group()
    objList.add(obj1)
    objList.add(obj2)

    g = 9.81  # gravedad
    mu = 0.9999  # Permeabilidad del metal
    mu0 = 4 * np.pi * 10 ** (-7)  # permeabilidad en el vacío
    sig = 58.108 * 10 ** 6  # conductividad del cobre
    t = 0
    ti = 0
    w = 0.004  # Grosor del tubo: 4mm
    a = 0.02  # 2 cm
    m = 0.02  # 20 g
    k = 45 * mu0 * mu0 * mu * mu * sig * w / (1024 * a ** 4)
    y = 0
    yi = 0
    vi = 0
    done = False
    temp = [False, False]

    T = list()
    Y = list()
    Yi = list()

    while not done:
        screen.blit(bg, (0, 0))
        T.append(T)
        Y.append(y)
        Yi.append(yi)
        if y <= 550:
            y = (0.5 * g * t ** 2) / fps
        if yi < 90 or yi > 470:
            temp[t % 2] = False
            if temp[0] != temp[1]:
                ti = 1
                obj1.image = pygame.image.load("iman.png").convert()
                obj1.image.set_colorkey((0, 0, 0))
                obj1.rect.x += 25
                yi += 25
            vi = vi + (g * ti) / fps
        else:
            if temp[0] != temp[1]:
                ti = 1
                obj1.image = pygame.image.load("imanCampo.png").convert()
                obj1.image.set_colorkey((0, 0, 0))
                obj1.rect.x -= 25
            temp[t % 2] = True
            vi = (m * g / k) * (1 - np.e ** (-k * ti / m))
        yi += vi
        obj1.move(yi)
        obj2.move(y)
        objList.draw(screen)
        t += 1
        ti += 1
        if yi >= 550:
            done = True
        pygame.display.update()
        clock.tick(fps)

    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                done = False
                break




if __name__ == "__main__":
    main()
