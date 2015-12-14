from piece import Piece
import copy

class Solver:
	def __init__(self, pieces, puzzle):
		self.pieces = pieces
		self.puzzle = puzzle
		self.puzzleReference = {}
		self.placementList = []

	#Builds a dictionary that assigns a coordinate tuple to a number value (for lookups, etc)(might be unnecessary)
	def buildPuzzleReference(self):
		count = 0
		for i in range(0, len(self.puzzle.matrix)):
			for j in range(0, len(self.puzzle.matrix[i])):
				if " " not in self.puzzle.matrix[i][j]:
					self.puzzleReference[(i,j)] = count
					count+=1

		#Add each identity for the pieces to the reference as well, this prevents the same piece from
		#being chosen with different placements in the solution.
		for pieces in self.pieces:
			self.puzzleReference[pieces.getIdentity()] = count
			count += 1



	#Begins the process of building every possible placement of a piece on an empty gameboard.
	def getAllPositions(self, pieceList, puzzle):
		for piece in pieceList:
			#Allows checking of each possible rotation of a piece
			for i in range(0,4):
				self.iteratePiece(piece, puzzle)
				piece.rotateClockWise()

	#Shifts the piece along the gameboard in both the x and y directions
	def iteratePiece(self, piece, puzzle):
		#Iterate through puzzle board
		for i in range(0, puzzle.height-piece.height+1):
			for j in range(0, puzzle.width-piece.width+1):
				self.checkFit(piece, puzzle, i, j)




	#Iterates through each brick of the piece and checks if the position it's placed on is equal to its value (X -> X or red -> red, etc)
	#This might be the last time you need to check whether it's a correct color/letter or not....
	def checkFit(self, piece, puzzle, posY, posX):
		#Check each brick in teh piece
		for i in range(0, piece.height):
			for j in range(0, piece.width):
					if piece.matrix[i][j] == puzzle.matrix[posY+i][posX+j]:
						continue
					elif " " in piece.matrix[i][j]:
						continue
					else:
						return False
		self.addPlacement(piece, posY, posX)


	#Adds the placement (positions the bricks would lay on, their values, etc) to the list of possible placements
	#later used in algorithm X. At this point I believe the matrix is only useful for a visual rep of the piece,
	# the only pertinent info is the coordinate info in the bricklist
	def addPlacement(self, piece, posY, posX):
		temp = copy.deepcopy(piece)
		for bricks in temp.brickList:
			bricks[0][0] = bricks[0][0] + posY
			bricks[0][1] = bricks [0][1] + posX
		self.placementList.append(temp)

	def showPlacementList(self):
		for placement in self.placementList:
			print placement.brickList,
			print " --- ",
			print placement.getIdentity()
		return True

	#A Unit test. Glory Be.
	def checkValidPlacements(self, puzzle):
		for placement in self.placementList:
			for brick in placement.brickList:
				if brick[1] in puzzle.matrix[brick[0][1]][brick[0][0]] or " " in brick[1]:
					continue
				else:
					raise


# ------------------------- Here's where we start building the torroidally linked list --------------------------------







