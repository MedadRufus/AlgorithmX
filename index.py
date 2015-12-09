from collections import deque
from piece import Piece
from solver import Solver
import sys



# List to store the info of each piece.
pieceCollection = []
puzzle = None

def checkRight(array, r, c):
	try:
		if " " not in array[r][c+1]:
			return True
		else:
			return False
	except:
		return False

def checkDown(array, r, c):
	try:
		if " " not in array[r+1][c]:
			return True
		else:
			return False
	except:
		return False

def checkLeft(array, r, c):
	try:
		if " " not in array[r][c-1]:
			return True
		else:
			return False
	except:
		return False

def checkUp(array, r, c):
	try:
		if " " not in array[r-1][c]:
			return True
		else:
			return False
	except:
		return False

#Reads in the text file, adds each character (including spaces) to an array, if it finds a new line it creates a new row.
#Basically lays out the text file as a grid for easier processing.
def textFileToArray(inputFile):
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

#Starts searching through the array, once it finds a brick it starts to find the entire thing using findPiece (read comment for findPiece)
def traverseArray(array):
	for i in range(0, len(array)):
		for j in range (0, len(array[i])):
			if " " not in array[i][j]:
				array = findPiece(array, i, j)
	return array

# When traverse array finds a "brick", it sends the value and location to this function which uses Connected Component Labeling (wiki)
# to explore surrounding bricks to find all those connected using a queue.
# This is basically how breadth first search works
def findPiece(array, r, c):
	brickList = []
	queue = deque([])
	queue.append([[r,c], array[r][c]])
	#If a brick is found, it's removed from the array so that it isn't found again later.
	array[r][c] = " "

	while len(queue) > 0:
		brick = queue.popleft()
		x = brick[0][0]
		y = brick[0][1]
		brickList.append(brick)

		if checkRight(array, x, y):
			queue.append([[x,y+1], array[x][y+1]])
			array[x][y+1] = " "
		if checkDown(array, x, y):
			queue.append([[x+1,y], array[x+1][y]])
			array[x+1][y] = " "
		if checkLeft(array, x, y):
			queue.append([[x,y-1], array[x][y-1]])
			array[x][y-1] = " "
		if checkUp(array, x, y):
			queue.append([[x-1,y], array[x-1][y]])
			array[x-1][y] = " "

	currentPiece = Piece(brickList)
	pieceCollection.append(currentPiece)
	return array

if __name__ == "__main__":
	try:
		inputFile = sys.argv[1]
	except:
		print "Need to designate an input file."

	array = textFileToArray(inputFile)
	array = traverseArray(array)
	# for pieces in pieceCollection:
	# 	print pieces.size
	# 	for rows in pieces.matrix:
	# 		print rows
	# 	print "\n"
	pieceCollection.sort(key=lambda x: x.size)
	puzzle = pieceCollection[-1]
	pieceCollection.pop()
	solver = Solver(pieceCollection, puzzle)
	solver.buildPuzzleReference()



