class Solver:
	def __init__(self, pieces, puzzle):
		self.pieces = pieces
		self.puzzle = puzzle
		self.puzzleReference = {}


	def buildPuzzleReference(self):
		count = 0
		for i in range(0, len(self.puzzle.matrix)):
			for j in range(0, len(self.puzzle.matrix[i])):
				if " " not in self.puzzle.matrix[i][j]:
					self.puzzleReference[(i,j)] = count
					count+=1

	# def getPossiblePlacements(piece):
	# 	for i in range()

	def getAllPositions(self, pieceList, puzzle):
		for piece in pieceList:
			for i in range(0,4):
				self.shiftPiece(piece, puzzle)
				piece.rotateClockwise()


	def shiftPiece(self, piece, puzzle):
		for i in range(0, puzzle.height-piece.height+1):
			for j in range(0, puzzle.width-piece.width+1):
				fits = self.checkFit(piece, puzzle, i, j)
				if fits == True:
					for brick in piece.brickList:
						print brick[0][0] + i,
						print " - ",
						print brick[0][1] + j
						print "\n"


	def checkFit(self, piece, puzzle, posY, posX):
		fits = True
		for i in range(0, piece.height):
			for j in range(0, piece.width):
				try:
					if piece.matrix[i][j] in puzzle.matrix[posY+i][posX+j]:
						continue
					else:
						return False
				except:
					return False
		return fits
