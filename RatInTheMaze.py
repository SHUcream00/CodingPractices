'''
Backtracking  practice #2
Rat In The Maze
Fixed
'''
class Maze():
    def __init__(self, maze):
        self.maze = maze
        self.solution = [[0 for _ in range(len(self.maze))] for _ in range(len(self.maze[0]))]

    def isopen(self, coord):
        if 0 <= coord[0] < len(self.maze[0]) and 0 <= coord[1] < len(self.maze) and self.maze[coord[0]][coord[1]] == 1: return True
        return False

    def printsolution(self):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                print(self.solution[i][j], end = ' ')
            print('\n')

    def traverse(self, current, dest, moves):

        if current == dest:
            self.solution[current[0]][current[1]] = 1
            return True

        if self.isopen(current):
            self.solution[current[0]][current[1]] = 1

            for i in moves:
                next = current + i
                if self.traverse(next, dest, moves): return True

            self.solution[current[0]][current[1]] = 0
            return False

    def ratitmaze(self):
        #NESW, but shouldn't it be more efficient to go East first, South next?
        #Idk
        start = (0,0)
        dest = (len(self.maze[0])-1, len(self.maze)-1)
        moves = [(0,-1),(1,0),(0,1),(-1,0)]

        if not self.traverse(start, dest, moves):
            print("The rat can't escape this maze")
            return False

        self.printsolution()
        return True

if __name__ == "__main__":
    # Initialising the maze
    maze = [ [1, 0, 0, 0],
             [1, 1, 0, 1],
             [0, 1, 0, 0],
             [1, 1, 1, 1] ]
    A = Maze(maze)
    A.ratitmaze()
