# AlgorithmX
**Python program which takes as input a text file representing a puzzle board and pieces, extracts the board and pieces to an internal matrix representation, and computes all possible ways to cover the entirety of the puzzle board using the provided pieces. The program also satisfies the constraint that each piece much match the underlying pattern on the puzzle board. To represent a normal pentomino or exact cover problem simply define the puzzle board and pieces using the same character.**

##To-Dos
- Format Output To Be More Human-Readable
- Optimize the discovering of all possible placments of each piece, as the algorithm becomes innefficient for any shapes dissimilar to quadrilaterals. 

##Motivation
The motivation to create a program to solve this problem came about from the realization that my day to day work at my job rarely involved the analysis and implementation of more advanced algorithms, a topic which I enjoyed exploring during my undergrad tenure. I decided to search for a project, and through a friend still studying undergrad was shown this problem that was being solved in a class they were taking. I worked on it for a week or so before becoming distracted by other going-ons in my life, and came back to it a few months later to finish it. Overall it was very satisfying to flex my problem-solving muscles, and was rewarding to learn about Exact Cover Problems, their solutions, and their practicality in the real world.

##Resources
- General Explanation of Exact Cover Problems [https://en.wikipedia.org/wiki/Exact_cover](https://en.wikipedia.org/wiki/Exact_cover)
- Explanation of Donald Knuth's Algorithm X [https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X](https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X)
- Donald Knuth's Dancing Links implementation of Algorithm X [http://lanl.arxiv.org/pdf/cs/0011047.pdf](http://lanl.arxiv.org/pdf/cs/0011047.pdf)
- Further Dancing Links Explanation [http://sudopedia.enjoysudoku.com/Dancing_Links.html](http://sudopedia.enjoysudoku.com/Dancing_Links.html)
- More reading on Exact Cover, Algorithm X, and Dancing Links [http://www.ams.org/samplings/feature-column/fcarc-kanoodle](http://www.ams.org/samplings/feature-column/fcarc-kanoodle)

- Explanation of Connected Component Labeling used to read in puzzle file definitions [https://en.wikipedia.org/wiki/Connected-component_labeling](https://en.wikipedia.org/wiki/Connected-component_labeling)

##Implementation
File breakdown:
- reader.py -- Processes the input text file and extracts the puzzle board and pieces, finally returns the gameboard and a list of all pieces sorted by size in number of bricks.
- solver.py -- Accepts list of puzzle pieces and puzzle, then finds all possible placements of each piece on the puzzle board, builds the representation of the Dancing Links matrix using Python dictionaries and sets, and then runs Algorithm X to find all possible solutions.
- index.py -- Main program file which executes all Reader and Solver functions, and displays pertinent information and eventual results of the program.

Example Input File:

```
         O     OXOXO         OX          
     X   XO        X  XO     XO          XOXOXOXO
     O    XO           X     O     X     OXOXOXOX
     X                       X     O     XOXOXOXO
           X   O     XO         OXOX     OXOXOXOX
    XOXO   O   X     OX                  XOXOXOXO
    O      X   OXO    O    X             OXOXOXOX
    X      O          X    O    OX       XOXOXOXO
           XO         O    X    XO       OXOXOXOX
                          XO     X       
                          O  
```
Note: First row and column should remain empty for no good reason other than I've been too lazy to go fix whatever bug makes it freak out if it isn't.

Process:
- Reader class takes in input file and creates a copy represented in matrix form.
- Reader class iterates through matrix until it finds the first none blank character, which it then calls its findPiece function.
- Reader's findPiece function executes the Connected Component Labeling algorithm by checking all surounding locations to the current brick, and if a surrounding location contains a non-blank character, it adds this brick to its queue to be processed later. This is effectively a breadth first search. It operates until no more bricks have been found in connection with the original brick.
- Reader runs findPiece on every contiguous area of non-blank characters in the input file until it reaches the end of the matrix, and returns a list of all pieces.
- Index sorts the list of pieces based on total number of bricks, chooses the largest piece as the puzzle board, and removes it from the list of pieces.
- Solver accepts the piece list and puzzle board during initialization.
- Solver searches for all possible valid placements of each piece on the board. It iterates the entire width and height of the board minus the piece's width and height, respectively, and determines if the pieces matches the underlying pattern and is a valid placement within the gameboard. It then rotates the piece and repeats, until all orientations have been checked.
- Solver uses the resultant list of valid placements to build its dictionary which represents each column of the Dancing Links matrix i.e. each column represents a position on the matrix, along with one identity column for each piece.
- Solver builds its dictionary representing each row of the Dancing Links Matrix, i.e. each row is a list referencing every column (location within the puzzleboard) in which that placement of that piece holds a brick, plus a reference to that placement's piece's identity column.
- Solver also populates the column dictionary, with each column holding a reference to every row (placement of a piece) which places a brick in the locaiton it represents.
- Solver begins solving the Exact Cover problem using Knuth's Algorithm X modified to work with Python Dictionary and Set primitives. It begins by choosing the column (entry in columnDictionary) with the least number of entries, begins iterating throw each row represented in that column, appending that row to the solution, covering that column, and recursively calling itself to begin solving sub-problems of itself. The program yields a solution only when it's given a "matrix" with no entries, and returns a list of each row appended to the solution in that branch of the programs execution.
- The program finishes once all branches have been explored.


