'''
Rotate Matrix inplace
maybe not complete
'''
class Matrix():
    def __init__(self, matrix):
        #matrix should be a square
        self.matrix = matrix
        self.size = len(matrix)

    def rotate(self):
        for row in range(self.size):
            for col in range(row, self.size-row-1):
                holder = self.matrix[row][col]
                self.matrix[row][col] =  self.matrix[col][self.size-1-row]
                self.matrix[col][self.size-1-row] = self.matrix[self.size-1-row][self.size-1-col]
                self.matrix[self.size-1-row][self.size-1-col] = self.matrix[self.size-1-col][row]
                self.matrix[self.size-1-col][row] = holder



if __name__ == "__main__":
    example1 = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]

    a = Matrix(example1)
    a.rotate()
    print(a.matrix)
