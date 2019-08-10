class KnightTour:
    solution = [] #2d matrix
    path = 0
    
    pos_i = (0, 0)
    
    POSSIBLE_MOVES = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
    

    def __init__(self, N):
        self.solution = [[0 for x in range(N)] for y in range(N)]
     
    def canMove(self, row, col, N):
        if row >= 0 and col >= 0 and row < N and col < N:
            return True
        else:
            return False
        
    def findPath(self,row, column, index, N):
        if self.solution[row][column] != 0:
            return False
        
        print('-'*20)
        print('\n'.join([str(e) for e in self.solution]))        
        self.path += 1 
        self.solution[row][column] = self.path

        #solved here V
        if index == (N * N-1):
            return True;
         
        for move in self.POSSIBLE_MOVES:
            if self.canMove(row + move[0], column + move[1], N) and self.findPath(row + move[0], column + move[1], index+1, N):
                return True;


        print("Backtrack!")
        self.solution[row][column] = 0
        self.path -= 1
        return False
        
         
        
    def solve(self):
        if self.findPath(self.pos_i[0], self.pos_i[1], 0, len(self.solution)):
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
                        
    def kt_print(self):
        for row in self.solution:
            for item in row:
                        
                print(item, end='\t')

N = 6;
my_KT = KnightTour(N)
my_KT.solve();
