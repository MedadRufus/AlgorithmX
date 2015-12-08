

def buildpiece(array, r, c):
	traverse = [[-1,0],[0,-1],[0,1],[1,0]]
	x = 0
	y = 0

	piece = []



def checkRight(array, r, c, piece, x, y):
	if " " not in array[r][c+1]:



def checkLeft(array, r, c):


def checkUp(array, r, c):


def checkDown(array, r, c):


def main():

	rowcount = 0
	with open("test.txt") as f:
		array = []
		array.append([])
		for line in f:
			for char in line:
				if "\n" in char:
					rowcount += 1
					array.append([])
					continue
				array[rowcount].append(char)

	buildpiece(array, 2, 5)
	for row in array:
		print row


if __name__ == "__main__":
	main()