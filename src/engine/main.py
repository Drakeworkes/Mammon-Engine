import pygame
import time

import src.engine.scenecreator.sceneCreator as sceneCreator

def main():
    print("Welcome to the Mammon Engine!")
    pygame.init()
    #For resize use second arg: pygame.RESIZABLE
    mainWindow=pygame.display.set_mode((512,448))
    isRunning = True
    testImg = pygame.image.load("../../data/assets/sprites/testSprite.png")
    grndSprite1 = pygame.image.load("../../data/assets/sprites/groundSprite1.png")
    testImg = pygame.transform.scale(testImg, (64, 64))
    grndSprite1 = pygame.transform.scale(grndSprite1, (64, 64))

    ground=[]
    mainWindow.fill((255, 255, 255))

    mainWindow.blit(testImg, (0, 0))


    w, h = pygame.display.get_surface().get_size()

    #mainWindow.blit(grndSprite1, (224, 224))
    mainWindow=sceneCreator.createPlatform(mainWindow, grndSprite1, ground, 512/64, 64,0,h, True)
    mainWindow = sceneCreator.createPlatform(mainWindow, grndSprite1, ground, 512 / 64, 64, 0, h, False)
    mainWindow = sceneCreator.createPlatform(mainWindow, grndSprite1, ground, 512 / 64, 64, 0, 0, False)
    mainWindow = sceneCreator.createPlatform(mainWindow, grndSprite1, ground, 512 / 64, 64, w, h, True)

    pygame.display.update()
    while(isRunning):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning=False

    print("Goodbye")


if(__name__ == "__main__"):
    main()