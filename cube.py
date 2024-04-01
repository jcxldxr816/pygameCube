#http://www.malinc.se/math/linalg/rotatecubeen.php

import pygame
import numpy as np
import math
import time

pygame.init()

W = 1920
H = 1080
centeredW = W/2
centeredH = H/2

screen = pygame.display.set_mode((W, H))

pygame.draw.rect(screen, (0,0,0), pygame.Rect(0,0, W,H))

def rotateX(mat3d):
    rotateMatX = np.array([[1, 0, 0],[0, math.cos(theta), -math.sin(theta)],[0, math.sin(theta), math.cos(theta)]])
    newMat = np.dot(rotateMatX, mat3d)
    return newMat
def rotateY(mat3d):
    rotateMatY = np.array([[math.cos(theta), 0, math.sin(theta)],[0, 1, 0],[-math.sin(theta), 0, math.cos(theta)]])
    newMat = np.dot(rotateMatY, mat3d)
    return newMat
def rotateZ(mat3d):
    rotateMatZ = np.array([[math.cos(theta), -math.sin(theta), 0],[math.sin(theta), math.cos(theta), 0],[0, 0, 1]])
    newMat = np.dot(rotateMatZ, mat3d)
    return newMat
def rotateAllDir(mat3d):
    newMat = rotateZ(rotateY(rotateX(mat3d)))
    return newMat

#projection array from 3d to 2d
projectionMat = np.array([[1, 0, 0],
                           [0, 1, 0]])
def projection(mat3d):
    mat2d = np.dot(projectionMat, mat3d)
    #parsing
    p = tuple(map(tuple, mat2d))
    float1 = 0.0
    float2 = 0.0
    float1Filled = False
    for tup in p:
        tupS = str(tup)
        tupS = tupS.replace(',', '')
        tupS = tupS.replace('(', '')
        tupS = tupS.replace(')', '')
        fl = float(tupS)
        if float1Filled == False:
            float1 = fl
            float1Filled = True
        if float1Filled == True:
            float2 = fl

        float1 += centeredW/2
        float2 += centeredW/2
    return (float1, float2)
    

#points of the cube
pointList = []
value = 75
a = np.array([[value],[value],[value]])
b = np.array([[value],[-value],[value]])
c = np.array([[-value],[value],[value]])
d = np.array([[-value],[-value],[value]])
e = np.array([[value],[value],[-value]])
f = np.array([[value],[-value],[-value]])
g = np.array([[-value],[value],[-value]])
h = np.array([[-value],[-value],[-value]])

pointList.append(a)
pointList.append(b)
pointList.append(c)
pointList.append(d)
pointList.append(e)
pointList.append(f)
pointList.append(g)
pointList.append(h)

theta = 0
run = True
while run == True:
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(0,0, W, H))

    newPtList = []
    theta += math.pi / 128
    for p in pointList: #projecting each point
        p1, p2 = projection(rotateAllDir(p))
        newPtList.append((p1,p2))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(p1, p2, 1,1))

    #drawing lines
    pygame.draw.line(screen, (255,255,255), newPtList[0], newPtList[1])
    pygame.draw.line(screen, (255,255,255), newPtList[1], newPtList[5])
    pygame.draw.line(screen, (255,255,255), newPtList[0], newPtList[4])
    pygame.draw.line(screen, (255,255,255), newPtList[4], newPtList[5])

    pygame.draw.line(screen, (255,255,255), newPtList[2], newPtList[3])
    pygame.draw.line(screen, (255,255,255), newPtList[6], newPtList[7])
    pygame.draw.line(screen, (255,255,255), newPtList[2], newPtList[6])
    pygame.draw.line(screen, (255,255,255), newPtList[3], newPtList[7])

    pygame.draw.line(screen, (255,255,255), newPtList[0], newPtList[2])
    pygame.draw.line(screen, (255,255,255), newPtList[1], newPtList[3])
    pygame.draw.line(screen, (255,255,255), newPtList[4], newPtList[6])
    pygame.draw.line(screen, (255,255,255), newPtList[5], newPtList[7])


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    time.sleep(.05)

    pygame.display.update()

pygame.quit()