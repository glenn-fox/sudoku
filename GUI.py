import pygame
import sys
from pygame.locals import *
from main import *

# Number of frames per second
FPS = 10
WINDOWMULTIPLIER = 6 # this changes the size of the grid
WINDOWSIZE = 81
SQUARESIZE = int((WINDOWSIZE * WINDOWMULTIPLIER) / 3)
CELLSIZE = int(SQUARESIZE / 3)
NUMBERSIZE = int(CELLSIZE /3)

WINDOWWIDTH = WINDOWSIZE * WINDOWMULTIPLIER
WINDOWHEIGHT = WINDOWSIZE * WINDOWMULTIPLIER
BLACK = (0,  0,  0)
WHITE = (255,255,255)
LIGHTGRAY = (200, 200, 200)


def initiateCells():
    currentGrid = {}
    fullCell = [1,2,3,4,5,6,7,8,9]
    for xCoord in range(0,9):
        for yCoord in range(0,9):
            currentGrid[xCoord,yCoord] = list(fullCell) # Copies List
    return currentGrid


def displayCells(currentGrid):
    # Create offset factors to display numbers in right location in cells.
    xFactor = 0
    yFactor = 0
    for item in currentGrid: # item is x,y co-ordinate from 0 - 8
        cellData = currentGrid[item] # isolates the numbers still available for that cell
        for number in cellData: #iterates through each number
            if number != ' ': # ignores those already dismissed
                xFactor = ((number-1)%3) # 1/4/7 = 0 2/5/8 = 1 3/6/9 =2
                if number <= 3:
                    yFactor = 0
                elif number <=6:
                    yFactor = 1
                else:
                    yFactor = 2
                #(item[0] * CELLSIZE) Positions in the right Cell
                #(xFactor*NUMBERSIZE) Offsets to position number
                populateCells(number,(item[0]*CELLSIZE)+(xFactor*NUMBERSIZE),(item[1]*CELLSIZE)+(yFactor*NUMBERSIZE))
    return None


def populateCells(cellData, x, y):
    cellSurf = BASICFONT.render('%s' %(cellData), True, LIGHTGRAY)
    cellRect = cellSurf.get_rect()
    cellRect.topleft = (x, y)
    DISPLAYSURF.blit(cellSurf, cellRect)


def drawGrid():
    ### Draw Minor Lines
    for x in range(0, WINDOWWIDTH, CELLSIZE):  # draw vertical lines
        pygame.draw.line(DISPLAYSURF, LIGHTGRAY, (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT, CELLSIZE):  # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, LIGHTGRAY, (0, y), (WINDOWWIDTH, y))

    ### Draw Major Lines
    for x in range(0, WINDOWWIDTH, SQUARESIZE):  # draw vertical lines
        pygame.draw.line(DISPLAYSURF, BLACK, (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT, SQUARESIZE):  # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, BLACK, (0, y), (WINDOWWIDTH, y))

    return None


def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    mouseClicked = False
    mousex = 0
    mousey = 0
    pygame.display.set_caption('Hello World')

    global BASICFONT, BASICFONTSIZE
    BASICFONTSIZE = 15
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)

    # main game loop
    while True:
        mouseClicked = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # mouse movement commands
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos

            # Mouse click commands
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True

        if mouseClicked == True:
            print(mousex)
            print(mousey)

        # repaints screen
        DISPLAYSURF.fill(WHITE)
        displayCells(currentGrid)
        drawGrid()
        # call function to draw box
        drawBox(mousex, mousey)

        pygame.display.update()
        FPSCLOCK.tick(FPS)


if __name__ == '__main__':
    main()