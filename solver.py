from piece import Piece
import copy

class Solver:
	def __init__(self, pieces, puzzle):
		self.pieces = pieces
		self.puzzle = puzzle
		self.puzzleReference = {}
		self.placementList = []
		self.solutionList = []


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
			print " --- "
			for row in placement.matrix:
				print row
			print " --- "
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

	#Sets up the solver		
	def beginSolving(self):
		partial_solution = self.getBlankMatrix()
		number_solution =  self.getBlankMatrix()
		placement_unused = self.placementList
		placement_used = []
		self.solve(partial_solution, number_solution, placement_unused, placement_used, 1)
		self.showSolutions()
		return

	#Recursive function that checks every possible placement of every piece to see if it eventually
	# finds a solution, which will then be caught by the base case and saved to the list of solutions
	def solve(self, partial_solution, number_solution, placement_unused, placement_used, depth):
		if self.checkSolution(partial_solution):
			self.addSolution(partial_solution, number_solution, placement_used)
			return
		elif len(placement_unused) == 0:
			return
		else:
			for placement in placement_unused:
				if self.noOverlap(partial_solution, placement):
					new_partial_solution, new_number_solution = self.addPlacementToSolution(partial_solution, number_solution, placement)
					new_placement_used = copy.deepcopy(placement_used)
					new_placement_used.append(placement)
					new_placement_unused = self.removeAlternatePlacements(placement, placement_unused)
					self.solve(new_partial_solution, new_number_solution, new_placement_unused, new_placement_used, depth+1)
			return

	# Checks if a piece can be placed within the partial solution, it can't if the piece overlaps with another
	# thats already been placed in that spot.
	def noOverlap(self, partial_solution, placement):
		for bricks in placement.brickList:
			if " " not in bricks[1]:
				if " " in partial_solution[bricks[0][0]][bricks[0][1]]:
					continue
				else:
					return False

		return True

	# Adds the piece in its position and rotation onto the partial solution.
	def addPlacementToSolution(self, partial_solution, number_solution, placement):
		tempPartial = copy.deepcopy(partial_solution)
		tempNumber = copy.deepcopy(number_solution)
		for bricks in placement.brickList:
			tempPartial[bricks[0][0]][bricks[0][1]] = str(bricks[1])
			tempNumber[bricks[0][0]][bricks[0][1]] = int(placement.getIdentity())
		return tempPartial, tempNumber


	# When a piece is placed as above ^, this iterates through the list of possible placements and removes any that are
	# of the same piece, since it's already been added to the partial solution.
	def removeAlternatePlacements(self, placement, placement_unused):
		return_placement_unused = []
		for i in range(0, len(placement_unused)):
			if placement.getIdentity() != placement_unused[i].getIdentity():
				return_placement_unused.append(placement_unused[i])
		return return_placement_unused

	#This checks to see if the partial solution is equal to the actual puzzle board, if it is, a solution has been found.
	def checkSolution(self, partial_solution):
		for i in range(0, len(self.puzzle.matrix)):
			for j in range(0, len(self.puzzle.matrix[0])):
				if partial_solution[i][j] == self.puzzle.matrix[i][j]:
					continue
				else:
					return False
		return True

	#This adds a solution to the list of valid solutions that have already been found.
	def addSolution(self, partial_solution, number_solution, placement_used):
		# for row in number_solution:
		# 	print row
		# print " ---- "
		# print len(self.solutionList)
		if self.solutionIsUnique(copy.deepcopy(number_solution)):
			self.solutionList.append([partial_solution, number_solution, placement_used])
			print "Solution found!:"
			for row in number_solution:
				print row
			print "\n"
		return

	#This checks if the solution is unique, preventing isomorphic solutions from being included.
	# It iterates through the list of solutions already found and compares them to the one we're about to add.
	def solutionIsUnique(self, number_solution):
		uniqueSolution = True
		if len(self.solutionList) > 0:
			for solution in self.solutionList:
				if self.areSolutionsEqual(solution[1], number_solution):
					uniqueSolution = False
		return uniqueSolution

	#Helper function for above, simply compares one solution to another.
	def areSolutionsEqual(self, sol1, sol2):
		equal = True
		for i in range(len(sol1)):
			for j in range(len(sol1[0])):
				if sol2[i][j] != sol1[i][j]:
					equal = False
		return equal

	#Outputs the list of solutions after the search has been completed.
	def showSolutions(self):
		count = 1
		for solutions in self.solutionList:
			print "Solution #",
			print count,
			count+=1
			print ":"
			print "   Puzzle Representation: "
			for row in solutions[0]:
				print row
			print "   Piece Representation"
			for row in solutions[1]:
				print row
			print "\n"

	#Gets a new matrix to be used in the above functions that's equal to the size of the puzzle
	#Because Pythons pass by reference and I completely forgot that.
	def getBlankMatrix(self):
		blank_matrix = [[" " for x in range(len(self.puzzle.matrix[0]))] for x in range(len(self.puzzle.matrix))]
		if len(blank_matrix) != len(self.puzzle.matrix) or len(blank_matrix[0]) != len(self.puzzle.matrix[0]):
			raise
		return blank_matrix






