#!/usr/bin/env python3

import sys
from getPath import findPath

#-1 --> 1(Wall)
#-2 --> 0(Empty)
#-3 --> 'F'(Ghost)
#-4 --> 'P'(Pacman)
#-5 --> Error

resultTab = []

def loopInLine(line, positionPacman, positionPhantom, positionCursor):
    global resultTab
    resultTab.append([])
    for i in range(0, len(line)):
        if (line[i] == 'P' and positionPacman == None):
            positionPacman = (i, positionCursor)
        elif (line[i] == 'F' and positionPhantom == None):
            positionPhantom = (i, positionCursor, 0)
        elif (line[i] == 'F' or line[i] == 'P'):
            sys.exit(84)
        charMap = {'1': -1, '0': -2, 'F': -3, 'P': -4}.get(line[i], -5)
        if (charMap == -5):
            sys.exit(84)
        resultTab[positionCursor].append(charMap)
    return (positionPacman, positionPhantom)

def run(contentFile, c1, c2):
    positionPhantom = None
    positionPacman = None
    positionCursor = 0
    for line in contentFile:
        positionPacman, positionPhantom = loopInLine(line.strip('\n').strip('\r').strip('\n'), positionPacman, positionPhantom, positionCursor)
        positionCursor += 1
    if ((positionPhantom == None) or (positionPacman == None)):
        sys.exit(84)
    findPath(positionPhantom, positionPacman, c1, c2, resultTab)