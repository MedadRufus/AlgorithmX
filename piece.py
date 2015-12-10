class Piece(object):

	def __init__(self, inputBrickList):
		self.brickList = inputBrickList
		self.constructMatrix()
		self.size = len(inputBrickList)

	#Goes through passed in list of bricks and creates the matrix
	def constructMatrix(self):
			dimensions = self.getDimensions()
			minWidth = dimensions[0]
			minHeight = dimensions[1]
			self.matrix = [[" " for x in range(0, self.width)] for x in range(0, self.height)]
			for bricks in self.brickList:
				self.matrix[bricks[0][0]-minHeight][bricks[0][1]-minWidth] = bricks[1]
				
			for i in range(0, len(self.brickList)):
				self.brickList[i][0][0] -=  minHeight
				self.brickList[i][0][1] -= minWidth


	#Get the height and width of the piece to use to construct its matrix representation
	def getDimensions(self):
		minHeight = self.brickList[0][0][0]
		maxHeight = self.brickList[0][0][0]
		minWidth = self.brickList[0][0][1]
		maxWidth = self.brickList[0][0][1]

		for bricks in self.brickList:
			if  bricks[0][0] < minHeight:
				minHeight = bricks[0][0]
			if  bricks[0][0] > maxHeight:
				maxHeight = bricks[0][0]
			if  bricks[0][1] < minWidth:
				minWidth = bricks[0][1]
			if  bricks[0][1] > maxWidth:
				maxWidth = bricks[0][1]

		self.width = maxWidth - minWidth + 1
		self.height = maxHeight - minHeight + 1

		#Return the width/height so we know how big the array should be
		#minheight/minwidth so we can translate brick locations from inputArray to locations in their small matrix.
		return [minWidth, minHeight]

	#Rotates the piece by ninety degrees.
	def rotateClockWise(self):
		tempMatrix = [[" " for x in  range(0, self.height)] for x in range(0, self.width)]
		self.brickList = []
		for i in range (0, self.height):
			for j in range (0, self.width):
				#Translates the matrix to a representation rotated 90 degrees.
				tempMatrix[j][i] = self.matrix[self.height-i-1][j]
				#Repopulates the bricklist with the correct locations
				self.brickList.append([[j,i], tempMatrix[j][i]])

		self.matrix = tempMatrix
		#Switch height and width since, you know, they're different now.
		self.width, self.height = self.height, self.width





