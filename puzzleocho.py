import copy 
import heapq

class PuzzleState: 
    def __init__(self, board, parent= None, action= None, depth = 0): 
        self.board = board
        self.parent = parent 
        self.action = action 
        self.depth = depth
        self.heuristic = self.calculate_heuristic()
        self.key = self.calculate_key()

    def calculate_key(self):
        return tuple(map(tuple, self.board))

    def goal(self):
        goal = [[1,2,3],
                [4,5,6],
                [7,8,0]]
        return self.board == goal
    
    def calculate_heuristic(self):
        h = 0 
        for i in range(3): 
            for j in range(3):
                if self.board != 0: 
                    goalRow, goalCol = divmod(self.board[i][j] - 1, 3)
                    h += abs(i-goalRow) + abs(j -goalCol)
        return h
    
    def generate_successors(self): 
        successor = []
        zeroRow, ZeroCol = self.findZero()
        actions = [ (0, 1), (0, 1), (1, 0), (-1,0)]

        for dr, dc in actions: 
            newRow, newCol = zeroRow + dr, ZeroCol + dc

            if 0 <= newRow < 3 and 0 <= newCol < 3:
                p


    def findZero(self):
        for i in range(3): 
            for j in range(3):
                if self.board[i][j]== 0:
                    return i, j 
    

def hola(): 
    return "hola mundo"

