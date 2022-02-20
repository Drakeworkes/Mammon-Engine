import pygame
from src.game.boardGame import boardGame
from src.game.boardGame2.firstBoard import FirstBoard
from src.engine.menus import mainmenu


def launchMapMenu(mainWindow, framerate, scale):
    clock = pygame.time.Clock()
    width, height = pygame.display.get_surface().get_size()

    # menu buttons for now
    mapPrevImg = pygame.image.load("data/assets/sprites/mapPreview.png")
    mapButton1Img = pygame.image.load("data/assets/sprites/mapButton1.png")
    comingSoonButtonImg = pygame.image.load("data/assets/sprites/comingSoonMenuButton.png")
    acceptButtonImg = pygame.image.load("data/assets/sprites/acceptMenuButton.png")
    backButtonImg = pygame.image.load("data/assets/sprites/backMenuButton.png")

    # Scale menu buttons and images
    mapPrevImg = pygame.transform.scale(mapPrevImg,
                                        ((mapPrevImg.get_width()) * scale,
                                         (mapPrevImg.get_height()) * scale))
    mapButton1Img = pygame.transform.scale(mapButton1Img,
                                         ((mapButton1Img.get_width()) * scale,
                                          (mapButton1Img.get_height()) * scale))
    comingSoonButtonImg = pygame.transform.scale(comingSoonButtonImg,
                                         ((comingSoonButtonImg.get_width()) * scale,
                                          (comingSoonButtonImg.get_height()) * scale))
    acceptButtonImg = pygame.transform.scale(acceptButtonImg,
                                         ((acceptButtonImg.get_width()) * scale,
                                          (acceptButtonImg.get_height()) * scale))
    backButtonImg = pygame.transform.scale(backButtonImg,
                                         ((backButtonImg.get_width()) * scale,
                                          (backButtonImg.get_height()) * scale))

    # Paint buttons and images to screen
    mainWindow.fill((55, 55, 55))
    mainWindow.blit(mapPrevImg, (0, 0))
    mainWindow.blit(mapButton1Img, (340 * scale, 16 * scale))
    mainWindow.blit(comingSoonButtonImg,(340 * scale, 64 * scale))
    mainWindow.blit(comingSoonButtonImg,(340 * scale, 112 * scale))
    mainWindow.blit(acceptButtonImg,(380 * scale, 348 * scale))
    mainWindow.blit(backButtonImg,(4 * scale, 412 * scale))

    pygame.display.update()
    isRunning = True
    currentMap = ""

    while (isRunning):
        clock.tick(framerate)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False

            # Handle Clicks
            if event.type == pygame.MOUSEBUTTONUP:
                click = pygame.mouse.get_pos()
              #  print(click[0], click[1])

                if((click[0] > 336 * scale) and (click[0] <= 496 * scale)):     # x
                    if((click[1] > 16 * scale) and (click[1] <= 48 * scale)):   # y
                        print("First Board button pressed")
                        currentMap = "FirstBoard"
                        # check if accept is hit, and if so, pass first board to joel
                    elif((click[1] > 64 * scale) and (click[1] <= 96 * scale)): # y
                        print("It ain't here yet")
                        currentMap = "DNE"
                        # if accept hit, print error
                    elif ((click[1] > 112 * scale) and (click[1] <= 148 * scale)): # y
                        print("Nor is this one")
                        currentMap = "DNE"
                        # if accept hit while this selected, print error
                        # else check if the click was Accept NEED IF HERE OR IT FALLS IN FIRST IF
                if((click[0] > 380 * scale) and (click[0] <= 508 * scale)):     # x
                    if((click[1] > 348 * scale) and (click[1] <= 444 * scale)): # y
                        print("ACCEPT")
                        if(currentMap == "FirstBoard"):
                            print("PLAY FIRST BOARD")
                            newWindow = pygame.display.set_mode((width, height))
                            firstBoard = FirstBoard().testFirstBoard()
                            return boardGame.startGame(mainWindow, scale, framerate, firstBoard)
                        elif(currentMap == "DNE"):
                            print("Invalid Map Selection")

                if ((click[0] > 4 * scale) and (click[0] <= 100 * scale)):  # x
                    if ((click[1] > 412 * scale) and (click[1] <= 444 * scale)):  # y
                        print("BACK")
                        return mainmenu.launch(width, height, framerate, scale)