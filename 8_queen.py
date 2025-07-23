def is_safe(board,row,col):
    for i in range(row):
        if board[i]==col or board[i]- i == col - row or board[i]+ i == col - row:
            return False
    return True

def solve(n,row,board):
    if row == n:
        return board[:]
    for col in range(n):
        if is_safe(board,row,col):
            board[row] = col
            solution = solve(n,row+1,board)
            if solution:
                return solution
    return None

def print_board(board):
    n = len(board)
    for row in range(n):
        for col in range(n):
            print("Q" if board[row] == col else ".",end = " ")
        print()

n = 8
board = [-1]*n
solution = solve(n,0,board)
if solution:
    print("The Solution is : ")
    print_board(solution)
else:
    print("No solution exists.")