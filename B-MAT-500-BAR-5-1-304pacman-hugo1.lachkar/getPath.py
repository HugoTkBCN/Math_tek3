#!/usr/bin/env python3

import sys

#-1 --> 1(Wall)
#-2 --> 0(Empty)
#-3 --> 'F'(Ghost)
#-4 --> 'P'(Pacman)
#-5 --> Error

resultTab = []

def isPacamanNext(tmpPosition, x, y, z):
    global resultTab
    if (x < 0 or x >= len(resultTab[y]) or y < 0 or y >= len(resultTab)):
        return (False)
    if (resultTab[y][x] == -2):
        resultTab[y][x] = z + 1
        tmpPosition.append((x, y, z + 1))
    elif (resultTab[y][x] == -4):
        return (True)
    return (False)

def getCharactereToPrint(c1, c2, character):
    return ({-1: c1, -2: c2, -3: 'F', -4: 'P'}.get(character, str(character % 10)))

def printPath(c1, c2):
    global resultTab
    for line in resultTab:
        path = ""
        for character in line:
            path += getCharactereToPrint(c1, c2, character)
        print(path)

def isPathFound(prevPosition):
    tmpPosition = []
    for positionPacman in prevPosition:
        if (isPacamanNext(tmpPosition, positionPacman[0], positionPacman[1] - 1, positionPacman[2]) or 
            isPacamanNext(tmpPosition, positionPacman[0] + 1, positionPacman[1], positionPacman[2]) or 
            isPacamanNext(tmpPosition, positionPacman[0], positionPacman[1] + 1, positionPacman[2]) or 
            isPacamanNext(tmpPosition, positionPacman[0] - 1, positionPacman[1], positionPacman[2])):
            return (True, [])
    return (False, tmpPosition)

def findPath(positionPhantom, positionPacman, c1, c2, prevResultTab):
    global resultTab
    resultTab = prevResultTab
    prevPosition = [positionPhantom]
    pathFound = False
    while (pathFound == False and prevPosition != []):
        pathFound, prevPosition = isPathFound(prevPosition)
    printPath(c1, c2)