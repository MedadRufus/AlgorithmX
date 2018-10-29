class Piece(object):
    def __init__(self, inputBrickList):
        self.brickList = inputBrickList
        self.constructMatrix()
        self.size = len(inputBrickList)
        self.identity = None

    # Goes through passed in list of bricks and creates the matrix
    def constructMatrix(self):
        dimensions = self.getDimensions()
        minWidth = dimensions[0]
        minHeight = dimensions[1]
        self.matrix = [[" " for x in range(0, self.width)] for x in range(0, self.height)]
        for bricks in self.brickList:
            self.matrix[bricks[0][0] - minHeight][bricks[0][1] - minWidth] = bricks[1]

        for i in range(0, len(self.brickList)):
            self.brickList[i][0][0] -= minHeight
            self.brickList[i][0][1] -= minWidth

    # Get the height and width of the piece to use to construct its matrix representation
    def getDimensions(self):
        minHeight = self.brickList[0][0][0]
        maxHeight = self.brickList[0][0][0]
        minWidth = self.brickList[0][0][1]
        maxWidth = self.brickList[0][0][1]

        for bricks in self.brickList:
            if bricks[0][0] < minHeight:
                minHeight = bricks[0][0]
            if bricks[0][0] > maxHeight:
                maxHeight = bricks[0][0]
            if bricks[0][1] < minWidth:
                minWidth = bricks[0][1]
            if bricks[0][1] > maxWidth:
                maxWidth = bricks[0][1]

        # HEIGHT AND WIDTH OF THE MATRIX CONTAINING THE PIECE. VERY VITAL
        # Due to how python represents matrices, the height will always be associated with the i, or first [i][] of the array,
        # width will always be associated with the j, or [][j] second value of the array
        # This is kind of obvious but it leaves things open for stupid mistakes.
        self.width = maxWidth - minWidth + 1
        self.height = maxHeight - minHeight + 1

        # Return the width/height so we know how big the array should be
        # minheight/minwidth so we can translate brick locations from inputArray to locations in their small matrix.
        return [minWidth, minHeight]

    # Rotates the piece by ninety degrees.
    def rotateClockWise(self):
        tempMatrix = [[" " for x in range(0, self.height)] for x in range(0, self.width)]
        self.brickList = []
        for i in range(0, self.height):
            for j in range(0, self.width):
                # Translates the matrix to a representation rotated 90 degrees.
                tempMatrix[j][i] = self.matrix[self.height - i - 1][j]
                # Repopulates the bricklist with the correct locations
                if " " not in tempMatrix[j][i]:
                    self.brickList.append([[j, i], tempMatrix[j][i]])

        self.matrix = tempMatrix
        # Switch height and width since, you know, they're different now.
        self.width, self.height = self.height, self.width

    # Unique identity for use in dancing links/algorithm x
    def setIdentity(self, value):
        self.identity = value

    def getIdentity(self):
        return self.identity

    # When storing bricks as placements before doing dancing links, must know where they'll actually lie on the board.
    def translateBricks(self, y, x):
        for i in range(0, len(self.brickList)):
            self.brickList[i][0][0] = self.brickList[i][0][0] + y
            self.brickList[i][0][0] = self.brickList[i][0][0] + x
