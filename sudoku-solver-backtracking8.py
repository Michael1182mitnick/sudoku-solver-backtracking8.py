# Implement a solver for a Sudoku puzzle using backtracking to fill in the missing numbers while satisfying all Sudoku rules.

def is_valid(board, row, col, num):
    """
    Check if placing 'num' in board[row][col] is a valid move
    according to Sudoku rules.
    """
    # Check if 'num' is not in the current row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check if 'num' is not in the current column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check if 'num' is not in the current 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def solve_sudoku(board):
    """
    Solve the Sudoku puzzle using backtracking.
    """
    # Find the next empty cell (represented by 0)
    empty_cell = find_empty(board)
    if not empty_cell:
        return True  # Puzzle is solved

    row, col = empty_cell

    # Try numbers 1 through 9
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            # Place 'num' in the current cell
            board[row][col] = num

            # Recursively attempt to solve the rest of the board
            if solve_sudoku(board):
                return True

            # If placing 'num' does not lead to a solution, backtrack
            board[row][col] = 0

    return False


def find_empty(board):
    """
    Find the next empty cell in the Sudoku board.
    """
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None


def print_board(board):
    """
    Print the Sudoku board in a readable format.
    """
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            print(board[i][j], end=" ")
        print()


if __name__ == "__main__":
    # Example Sudoku board with empty cells represented by 0
    sudoku_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Original Sudoku Board:")
    print_board(sudoku_board)

    if solve_sudoku(sudoku_board):
        print("\nSolved Sudoku Board:")
        print_board(sudoku_board)
    else:
        print("No solution exists for the given Sudoku board.")
