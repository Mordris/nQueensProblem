def is_safe(board, row, col, n):
    # Check if there's a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens_util(board, row, n, solutions):
    if row == n:
        # If all queens are placed, add the current board configuration to solutions
        solutions.append([row[:] for row in board])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            # Place the queen and move to the next row
            board[row][col] = 1
            solve_n_queens_util(board, row + 1, n, solutions)

            # Backtrack and remove the queen for other possible placements
            board[row][col] = 0


def solve_n_queens(n):
    # Initialize the chessboard
    board = [[0] * n for _ in range(n)]
    solutions = []

    # Call the utility function to find all solutions
    solve_n_queens_util(board, 0, n, solutions)

    return solutions


def print_board(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print()


# Take input from the user for the number of queens
while True:
    try:
        n = int(input("Enter the number of queens (N): "))
        if n <= 0:
            print("Please enter a positive integer greater than zero.")
        else:
            break
    except ValueError:
        print("Invalid input! Please enter an integer.")

solutions = solve_n_queens(n)
print("Number of solutions for", n, "queens:", len(solutions))
for i, solution in enumerate(solutions):
    print("Solution", i + 1)
    print_board(solution)
