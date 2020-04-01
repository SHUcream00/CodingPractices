def checklim(board, loc):
    return True if 0 <= loc[0] < len(board[0]) and 0 <= loc[1] < len(board) else False


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
print(len(board[0]), len(board))
print(checklim(board, (1,3)))
print(checklim(board, (0,0)))
