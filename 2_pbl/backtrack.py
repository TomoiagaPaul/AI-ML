class KnightTour:
    solution = [] #2d matrix
    path = 0
    
    pos_i = (0, 0)

    n_row = 0
    n_col = 0
    
    POSSIBLE_MOVES = ((2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2))
    

    def __init__(self, rows, cols):
        self.solution = [[0 for x in range(cols)] for y in range(rows)]
        self.n_row = rows
        self.n_col = cols
     
    def canMove(self, row, col, rows, cols):
        if row >= 0 and col >= 0 and row < rows and col < cols:
            return True
        else:
            return False
        
    def findPath(self,row, column, index, rows, cols):
        if self.solution[row][column] != 0:
            return False
        
        print('-'*20)
        print('\n'.join([str(e) for e in self.solution]))        
        self.path += 1 
        self.solution[row][column] = self.path

        #solved here V
        if index == (rows * cols-1): #???
            return True;
         
        for move in self.POSSIBLE_MOVES:
            if self.canMove(row + move[0], column + move[1], rows, cols) and self.findPath(row + move[0], column + move[1], index+1, rows, cols):
                return True;


        print("Backtrack!")
        self.solution[row][column] = 0
        self.path -= 1
        return False
        
         
        
    def solve(self):
        if self.findPath(self.pos_i[0], self.pos_i[1], 0, self.n_row, self.n_col):
            import time
            
            message = '''Traceback (most recent call last):
  File "backtrack.py", line 59, in <module>
    my_KT.solve();
  File "backtrack.py", line 46, in solve
    if self.findPath(self.pos_i[0], self.pos_i[1], 0, len(self.solution)):
TypeError: findPath() takes 4 positional arguments but 5 were given'''

            time.sleep(1.5)
            print(message)
            time.sleep(1.5)
            print("\n\nJust kidding!\n\n")
            print('\n'.join([str(e) for e in self.solution]))
        else:
            print("No path found!")
                        

rows = 6;
cols = 5;
my_KT = KnightTour(rows, cols)
my_KT.solve();
