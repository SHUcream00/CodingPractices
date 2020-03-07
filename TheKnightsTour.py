'''
Backtracking  practice #1
The Knights Tour
'''
class Chessboard():

    def __init__(self, size):
        self.size = size

    def steppable(self, coord, board):
        if 0 <= coord[0] < self.size and 0 <= coord[1] < self.size and board[coord[0]][coord[1]] == -1: return True
        return False

    def printboard(self, board):
        for i in range(self.size):
            for j in range(self.size):
                print(board[i][j], end = ' ')
            print('\n')

    #Traversing function
    def traverse(self, board, cur_loc, moves, steps):
        if steps == self.size ** 2: return True

        for i in range(self.size):
            next = (cur_loc[0] + moves[i][0], cur_loc[1] + moves[i][1])
            if self.steppable(next, board):
                board[next[0]][next[1]] = steps
                if self.traverse(board, next, moves, steps+1): return True
                board[next[0]][next[1]] = -1

        return False


    def knights_tour(self):
        board = [[-1 for _ in range(self.size)] for _ in range(self.size)]
        moves = [(1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1), (-2,-1), (-1,-2)] #possible moves
        steps = 1 #total steps

        initial = (0,0) #initial position on the board
        board[initial[0]][initial[1]] = 0 #initialize the loc on board

        if not self.traverse(board, initial, moves, steps): print("Impossible")
        else: self.printboard(board)

if __name__ == "__main__":
    A = Chessboard(8)
    A.knights_tour()
