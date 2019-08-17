class KnightTour:
    solution = [] #2d matrix
    path = 0
    
    pos_i = (0, 0)
    
    POSSIBLE_MOVES = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
    

    def __init__(self, N):
        self.solution = [[0 for x in range(N)] for y in range(N)]
     
    def canMove(self, row, column, N):
        if row >= 0 and column >= 0 and row < N and column < N:
            return True
        else:
            return False

    def getCost(self, row, column, N):
        #Fail if out of bounds or location has already been traveled to
        if self.canMove(row, column, N) and (self.solution[row][column] == 0):
            #Get the cost
            result = 0
            for move in self.POSSIBLE_MOVES:
                next_row = row + move[0]
                next_column = column + move[1]
            
                #increment if the next move is possible
                if self.canMove(next_row, next_column, N) and (self.solution[next_row][next_column] == 0):
                    result += 1
                    
            return result
        else:
            return 0
        
        
    def findPath(self, row, column, index, N):
        #return False if the location has already been moved to
        if self.solution[row][column] != 0:
            return False

        #Keep track of the step number
        self.path += 1 
        self.solution[row][column] = self.path

        #Fancy printing
        print('-'*20)
        print('\n'.join([str(e) for e in self.solution]))
        
        #return True if solved
        if index == (N * N-1):            
            return True;

        #Warnsdorff's rule
        cost_move = []
        for move in self.POSSIBLE_MOVES:
            #move[0] = row, move[1] = column
            cost = self.getCost(row + move[0], column + move[1], N)
            if cost != 0:
                cost_move.append((cost, move[0], move[1]))

        cost_move.sort()    

        if len(cost_move) == 0:
            for move in self.POSSIBLE_MOVES:
                next_row = row + move[0]
                next_column = column + move[1]
                
                if self.canMove(next_row, next_column, N) and self.findPath(next_row, next_column, index+1, N):
                    return True
        
        for move in cost_move:
            #move[0] = onwardMoves(...), move[1] = row, move[2] = column
            if self.findPath(row + move[1], column + move[2], index+1, N):
                return True

        #Backtrack if the path fails, set the previous location back to 0
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
                        
#    def kt_print(self):
#        print("\n\n\n\n\n\n\n\n\n\n\n\tarisenthrseinthiaernsdheinasrhda")
#        for row in self.solution:
#            for item in row:
#                print(item, end='\t')

N = 6;
my_KT = KnightTour(N)
my_KT.solve();
