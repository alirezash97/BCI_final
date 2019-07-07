# ################################     BackTracking     ################################
import numpy as np
import time
# from memory_profiler import profile
import os

start_time = time.time()
N = int(input("Please enter the number of queen: "))


# This is the main function.
# It returns false if queens cannot be placed, otherwise return true and placement of queens in the form of 1s.
# There might be more than one solution! this function returns one of them.
# @profile(precision=4)
def main():
    board = np.zeros((N, N), dtype=np.int)

    # If there is no valid answer(with no threats), return false
    if not solve(board, 0):
        print("Solution does not exist")
        return False

    for i in range(N):
        print(board[i])

    return True


# Check if a queen can be placed on board[row][col]
# This function is called when "col" queens are already placed in columns from 0 to col-1
# We only need to check the left side for potential threats
def is_safe(board, row, col):
    # Check left side of row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve(board, col):

    # If all queens are placed, return true
    if col >= N:
        return True

    # Take this column and try placing this queen in all rows one by one S.T there isn't any threat
    for i in range(N):

        if is_safe(board, i, col):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # Redo for other queens
            if solve(board, col + 1):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution, eliminate queen from board[i][col]
            board[i][col] = 0

    # If the queen can not be placed in any row in this column then return false
    # Meaning it has threat in that column
    return False


# call the functions
main()

# calculate the time the program takes
total_time = time.time() - start_time
print("--------- %s seconds ---------" % total_time)

if os.path.exists("BackTracking_time.txt"):
    os.remove("BackTracking_time.txt")
f = open("BackTracking_time.txt", "w+")
f.write(str(round(total_time, 2)))
f.close()
