#!/usr/bin/env python3
import sys, pygame, random
pygame.init()


size = width, height = 600, 600
white = 255,255,255
black = 0, 0, 0
screen = pygame.display.set_mode(size)
check = 0
if len(sys.argv) == 2: check = int(sys.argv[1])
def drawPoint(xandy):
    pygame.draw.rect(screen, white, (int(xandy[0] - 0.5), int(xandy[1] - 0.5), 1, 1)) 

points = [[0, 0], [width, 0], [width, height], [0, height]]
numberOfPoints = len(points)
pointNew = [width/2, height/2]
divisor = 2
lastWhichPoint = -1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    for i in range(100):
        # Random point 
        whichPoint = random.randint(0, numberOfPoints - 1)
        while whichPoint == (lastWhichPoint + check) % numberOfPoints:
            whichPoint = random.randint(0, numberOfPoints - 1)
        for index,point in enumerate(points):
            if whichPoint == index:
                # lerp
                pointNew = [pointNew[0] + (point[0] - pointNew[0])/divisor, pointNew[1] + (point[1] - pointNew[1])/divisor]
    
        lastWhichPoint = whichPoint
    
       # Rendering
        drawPoint(points[0])
        drawPoint(points[1])
        drawPoint(points[2])
        drawPoint(pointNew)

    pygame.display.flip()
