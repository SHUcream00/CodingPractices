'''
Rotate Matrix inplace
maybe not complete
'''
class Matrix():
    def __init__(self, matrix):
        #matrix should be a square
        self.matrix = matrix
        self.size = len(matrix)

    def rotateleft(self):
        for row in range(self.size):
            for col in range(row, self.size-row-1):
                holder = self.matrix[row][col] # holding the first item
                self.matrix[row][col] =  self.matrix[col][self.size-1-row] #right to top
                self.matrix[col][self.size-1-row] = self.matrix[self.size-1-row][self.size-1-col] #bottom to right
                self.matrix[self.size-1-row][self.size-1-col] = self.matrix[self.size-1-col][row] #left to bottom
                self.matrix[self.size-1-col][row] = holder #return back to left

    def rotateright(self):
        for row in range(self.size):
            for col in range(row, self.size-row-1):
                holder = self.matrix[row][col] # holding the first item
                self.matrix[row][col] = self.matrix[self.size-1-col][row] #left to top
                self.matrix[self.size-1-col][row] = self.matrix[self.size-1-row][self.size-1-col] #bottom to left
                self.matrix[self.size-1-row][self.size-1-col] = self.matrix[col][self.size-1-row] # right to bottom
                self.matrix[col][self.size-1-row] = holder #return back to right

    def printmatrix(self):
        for i in range(self.size):
            print(self.matrix[i], end = '\n')
        print('\n')


if __name__ == "__main__":
    example1 = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
    example2 = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]

    print("Turning the original matrix to left\n")
    a = Matrix(example1)
    a.rotateleft()
    a.printmatrix()

    print("Turning the original matrix to right\n")
    b = Matrix(example2)
    b.rotateright()
    b.printmatrix()
