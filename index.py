from piece import Piece
from solver import Solver
from reader import Reader
import sys

# List to store the info of each piece.
pieceCollection = []
puzzle = None

if __name__ == "__main__":
	#Get the input file name.
	try:
		inputFile = sys.argv[1]
	except:
		print "Need to designate an input file."

	reader = Reader()
	#Turn the input file into a giant matrix.
	array = reader.textFileToArray(inputFile)
	#Go through the array and get all the contiguous areas of characters that represent the pieces and gameboards.
	#This uses _________ algorithm (Built it a week ago and forgot to write down what I used, find it later)
	pieceCollection = reader.parseArray(array)

	#Sort the array by number of bricks and get the biggest one, make that the puzzle board.
	pieceCollection.sort(key=lambda x: x.size)
	puzzle = pieceCollection[-1]
	pieceCollection.pop()

	#Give each piece a unique number so that the solver won't pick the same piece placed in a different location
	# as part of the answer (assumption is that a piece can only be placed once.)
	# solver does this by creating a column for each pieces identity.
	for i in range (0, len(pieceCollection)):
		pieceCollection[i].setIdentity(i)


	#Instantiate a solver
	solver = Solver(pieceCollection, puzzle)
	#Build a list of every valid placement of a piece on an empty puzzle board.
	solver.getAllPositions(pieceCollection, puzzle)
		#solver.showPlacementList()
	solver.checkValidPlacements(puzzle)
	solver.buildPuzzleReference()



