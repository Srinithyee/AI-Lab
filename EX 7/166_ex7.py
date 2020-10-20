class TicTacToe:
    

    def __init__(self):
        
        self.board = [['.', '.', '.'],
                      ['.', '.', '.'],
                      ['.', '.', '.']]

        self.turn = 'X'
        self.checker_moves = 0

    
    def __str__(self):
        

        board_str = "=============\n| "

        for i in range(0, 3):
            for j in range(0, 3):
                board_str += self.board[i][j] + " || "
            board_str += "\n=============\n| "
        board_str = board_str[:-2:]
        board_str += "\n"

        return board_str


    def checker_validity(self, x, y):
        

        if x < 0 or x > 2 or y < 0 or y > 2:    
            return False
        elif self.board[x][y] != '.':           
            return False
        else:                                   
            return True


    def finisher(self):
        
        board = self.board

        winning_config = [[board[0][0], board[0][1], board[0][2]],    
                            [board[1][0], board[1][1], board[1][2]],
                            [board[2][0], board[2][1], board[2][2]],

                            [board[0][0], board[1][0], board[2][0]],    
                            [board[0][1], board[1][1], board[2][1]],
                            [board[0][2], board[1][2], board[2][2]],

                            [board[0][0], board[1][1], board[2][2]],    
                            [board[0][2], board[1][1], board[2][0]]]    
        
        
        if ['X', 'X', 'X'] in winning_config:
            return 'X'
        
        
        if ['O', 'O', 'O'] in winning_config:
            return 'O'

        
        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[i][j] == '.':
                    return False        

        return True                     

    
    def max(self):
        
        
        max_value = -2  

        x, y = None, None

        result = self.finisher()

        if result == 'X':       
            return (-1, 0, 0)

        elif result == 'O':     
            return (1, 0, 0)

        elif result == True:    
            return (0, 0, 0)

        
        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[i][j] == '.':
                    self.checker_moves += 1     

                    
                    self.board[i][j] = 'O'
                    m, min_i, min_j = self.min() 
                    
                    if m > max_value:
                        max_value = m
                        x = i
                        y = j

                    
                    self.board[i][j] = '.'
        
        return max_value, x, y


    def min(self):
        

        min_value = 2   

        x, y = None, None

        result = self.finisher()

        if result == 'X':       
            return (-1, 0, 0)

        elif result == 'O':     
            return (1, 0, 0)

        elif result == '.':     
            return (0, 0, 0)

        
        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[i][j] == '.':
                    self.checker_moves += 1     

                    
                    self.board[i][j] = 'X'
                    m, max_i, max_j = self.max() 

                    if m < min_value:
                        min_value = m
                        x = i
                        y = j
                    
                    
                    self.board[i][j] = '.'

        return min_value, x, y


    def game_visualiser(self):
        

        while True:
            print(self)
            self.result = self.finisher()

            
            if self.result == True:
                if self.result == 'X':
                    print("The winner is X!")
                
                elif self.result == 'O':
                    print("The winner is O!")
                
                else:
                    print("It is a tie!")

                self.__init__()
                return

            
            if self.turn == 'X':
                while True:
                    self.checker_moves = 0  
                    start = time.time()
                    m, x, y = self.min()    
                    end = time.time()

                    
                    print("I'LL SUGGEST YOU TO MOVE TO THIS COORDINATE\t: X = {0}, Y = {1}".format(x, y))
                    print("Moves checked\t\t: {0}\n".format(self.checker_moves))

                    x = int(input("Enter the X co-ordinate of your move: "))
                    y = int(input("Enter the Y co-ordinate of your move: "))

                    if self.checker_validity(x, y):
                        self.board[x][y] = 'X'
                        self.turn = 'O'
                        break
                    
                    else:
                        print("Invalid move. Try again.")
            
            
            else:
                self.checker_moves = 0
                start = time.time()
                m, x, y = self.max()
                end = time.time()

                print("Moves checked\t\t: {0}\n".format(self.checker_moves))

                self.board[x][y] = 'O'
                self.turn = 'X'

if __name__ == "__main__":
    game = TicTacToe()
    game.game_visualiser()