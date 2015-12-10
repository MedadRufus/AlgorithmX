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
