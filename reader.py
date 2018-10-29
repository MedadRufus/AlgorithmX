from collections import deque
from piece import Piece


class Reader(object):
    def __init__(self):
        self.pieceCollection = []

    # Helper functions to check around the current brick to see if they're also, you know, a brick.
    def checkRight(self, array, r, c):
        try:
            if " " not in array[r][c + 1]:
                return True
            else:
                return False
        except:
            return False

    def checkDown(self, array, r, c):
        try:
            if " " not in array[r + 1][c]:
                return True
            else:
                return False
        except:
            return False

    def checkLeft(self, array, r, c):
        try:
            if " " not in array[r][c - 1]:
                return True
            else:
                return False
        except:
            return False

    def checkUp(self, array, r, c):
        try:
            if " " not in array[r - 1][c]:
                return True
            else:
                return False
        except:
            return False

    # Reads in the text file, adds each character (including spaces) to an array, if it finds a new line it creates a new row.
    # Basically lays out the text file as a grid for easier processing.
    def textFileToArray(self, inputFile):
        rowcount = 0
        array = [[]]
        with open(inputFile) as f:
            for line in f:
                for char in line:
                    if "\n" in char:
                        rowcount += 1
                        array.append([])
                        continue
                    array[rowcount].append(char)
        return array

    # Starts searching through the array, once it finds a brick it starts to find the entire thing using findPiece (read comment for findPiece)
    def parseArray(self, array):
        for i in range(0, len(array)):
            for j in range(0, len(array[i])):
                if " " not in array[i][j]:
                    array = self.findPiece(array, i, j)
        return self.pieceCollection

    # When traverse array finds a "brick", it sends the value and location to this function which uses Connected Component Labeling (wiki)
    # to explore surrounding bricks to find all those connected using a queue.
    # This is basically how breadth first search works
    def findPiece(self, array, r, c):
        brickList = []
        queue = deque([])
        queue.append([[r, c], array[r][c]])
        # If a brick is found, it's removed from the array so that it isn't found again later.
        array[r][c] = " "

        while len(queue) > 0:
            brick = queue.popleft()
            x = brick[0][0]
            y = brick[0][1]
            brickList.append(brick)

            if self.checkRight(array, x, y):
                queue.append([[x, y + 1], array[x][y + 1]])
                array[x][y + 1] = " "
            if self.checkDown(array, x, y):
                queue.append([[x + 1, y], array[x + 1][y]])
                array[x + 1][y] = " "
            if self.checkLeft(array, x, y):
                queue.append([[x, y - 1], array[x][y - 1]])
                array[x][y - 1] = " "
            if self.checkUp(array, x, y):
                queue.append([[x - 1, y], array[x - 1][y]])
                array[x - 1][y] = " "

        currentPiece = Piece(brickList)
        self.pieceCollection.append(currentPiece)
        return array
