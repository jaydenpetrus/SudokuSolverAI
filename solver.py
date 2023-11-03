board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    #this part tries numbers 1-9 in the square and if it is valid it recursively calls itself and continues to solve it
    for i in range(1,10):
        if valid(board, i,(row,col)):
            board[row][col] = i

            #If it makes it to the end, it will return True
            if solve(board):
                return True
            #If the solution is invalid, it will change it back to default of 0 and return False, backtracking
            board[row][col] = 0

    return False



def valid(board, num, pos):
    """
    Check to see if the inserted number works for the sudoku and passes all the criteria
    :param board:
    :param num:
    :param pos:
    :return:
    """
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    #Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True

def print_board(board):
    """
    prints the board
    :param board:
    :return:
    """
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def find_empty(board):
    """
    finds an empty space in the board
    :param board:
    :return:
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) #row, column
    return None

print_board(board)
solve(board)
print("______________________________")
print_board(board)