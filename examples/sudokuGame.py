from sudoku import Sudoku as SudokuGenerator


class SudokuGame:
    def __init__(self):
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.strategy = ""

    def describeRules(self):
        rules = '''The rules for Sudoku are simple:
1. Each row must contain the digits from 1 to 9 without repetition.
2. Each column must contain the digits from 1 to 9 without repetition.
3. Each of the nine 3x3 squares must contain the digits from 1 to 9 without repetition.'''
        return {'rules': rules}

    def makePrettyBoard(self, board):
        # Prettify output
        pretty_board = "\n"
        for i, row in enumerate(self.board):
            if i % 3 == 0 and i != 0:
                pretty_board += "------+-------+------\n"
            for j, val in enumerate(row):
                #change None to 0
                
                if j % 3 == 0 and j != 0:
                    pretty_board += "| "
                pretty_board += str(val) + " "
            pretty_board += "\n"
        return pretty_board

    def generateExampleProblem(self):
        # Generate a random solvable Sudoku board using the `sudoku` library
        puzzle = SudokuGenerator(3).difficulty(0.1)
        self.board = puzzle.board

        #replace none with 0's in board
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == None:
                    self.board[i][j] = 0

        return {'state': self.board, 'pretty_state': self.makePrettyBoard(self.board)}

    def isValid(self, board, x, y, val):
        # Check row
        if val in board[x]:
            return False
        # Check column
        if val in [board[i][y] for i in range(9)]:
            return False
        # Check square
        startRow, startCol = 3 * (x // 3), 3 * (y // 3)
        for i in range(startRow, startRow + 3):
            for j in range(startCol, startCol + 3):
                if board[i][j] == val:
                    return False
        return True

    def find_empty_cell(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return i, j
        return -1, -1

    def getNextStep(self, problem):
        x, y = self.find_empty_cell(problem)
        if x == -1:
            return {'status': 'Done', 
                    'message': 'Sudoku solved!',
                    'state': problem, 
                    'pretty_state': self.makePrettyBoard(self.board)}

        for val in range(1, 10):
            if self.isValid(problem, x, y, val):
                problem[x][y] = val
                self.strategy = "Filled ({}, {}) with {} using Sole Candidate strategy".format(
                    x, y, val)
                return {'message': self.strategy,
                        'state': problem,
                        'pretty_state': self.makePrettyBoard(self.board),
                        'status': 'Continue'}

        return {'status': 'error', 
                'state': problem,
                'pretty_state': self.makePrettyBoard(self.board),
                'message': 'No valid next step found'}


if __name__ == "__main__":
    sudoku = SudokuGame()
    #setup game
    print("USER:")
    print(sudoku.describeRules()['rules'])
    print("Please solve this problem:")
    problem = sudoku.generateExampleProblem()
    print(problem['pretty_state'])
    #first step
    next_step = sudoku.getNextStep(problem['state'])
    print("ASSISTANT:")
    print(next_step['pretty_state'])
    print(next_step['status'])
    #rest of game
    while next_step['status']=='Continue':
        print("USER:\n please keep going!")
        print("ASSISTANT:")
        next_step = sudoku.getNextStep(next_step['state'])
        if 'message' in next_step:
            print(next_step['message'])
        print(next_step['pretty_state'])

