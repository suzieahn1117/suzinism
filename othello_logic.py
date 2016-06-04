# Project 4
# othello_logic




#import othello_ui

from collections import namedtuple

NONE = 0
BLACK = 1
WHITE = 2



class game:
    def __init__ (self, result):
        self.row = int(result[0])
        self.col = int(result[1])
        self.center = str(result[2]).upper()
        self.center = str(result[3]).upper()
        self.method = str(result[4])
        self.turn = BLACK
        self.opponent = WHITE
        self.board = []
        self.board = self._new_game_board()
        self.row_move = 0
        self.col_move = 0
        self.total_B = 0
        self.total_W = 0

    def set_move(self,move):
        self.row_move = int(move[0])
        self.col_move = int(move[1])
        

    def _new_game_board(self) -> [[int]]:
        '''creates a game board the size of input'''
        for row in range(int(self.row)):
            self.board.append([])
            for col in range(int(self.col)):
                self.board[-1].append(NONE)
        return self.board

    def print_board(self) -> None:
        for a_row in range(self.row):
            for a_col in range(self.col):
                if self.board[a_row][a_col] == 0:
                    print('.', sep=" ", end=" ")
                elif self.board[a_row][a_col] == 1:
                    print('B', sep=" ", end=" ")
                elif self.board[a_row][a_col] == 2:
                    print('W', sep=" ", end=" ")
            print()
        return self.board

    
    def disc_center(self) -> None:
        if self.center == 'B':
            self.board[int((self.row/2)-1)][int((self.col/2)-1)] = BLACK
            self.board[int((self.row/2))][int((self.col/2))] = BLACK
            self.board[int((self.row/2))][int((self.col/2)-1)] = WHITE
            self.board[int((self.row/2)-1)][int((self.col/2))] = WHITE
            
        elif self.center == 'W':
            self.board[int((self.row/2)-1)][int((self.col/2)-1)] = WHITE
            self.board[int((self.row/2))][int((self.col/2))] = WHITE
            self.board[int((self.row/2))][int(self.col/2)-1] = BLACK
            self.board[int((self.row/2)-1)][int((self.col/2))] = BLACK
            
            return self.board 

    def count_dock(self) -> None:
        total_B = 0
        total_W = 0
        for black in self.board:
            x = black.count(1)
            total_B += x
        for white in self.board:
            y = white.count(2)
            total_W += y
        self.total_B = total_B
        self.total_W = total_W

    def print_count(self):
        print("B: {} W: {}".format(self.total_B, self.total_W))
        

    def alternate_turn(self):
        if self.turn == BLACK:
            self.turn = WHITE
            self.opponent = BLACK
        else:
            self.turn = BLACK
            self.opponent = WHITE
        return self.turn
            

    def valid_cell(self):
        if self.board[(self.row_move)-1][(self.col_move)-1] == NONE:
            return True
        else:
            return False

    def place_move(self, row, col):
        while True:
            if self.invalid_move_check() == False:
                print('TRY AGAIN')
                x = othello_ui.move_input()
                self.row_move = int(x[0])
                row = int(x[0]) - 1
                self.col_move = int(x[1])
                col = int(x[1]) - 1
                
            else:
                break
                
        self.board[row][col] = self.turn
        self.alternate_turn()


    def valid_move(self):
        if self.valid_cell() == False:
            print('Invalid Movement')
            return False

        for row_index in range(self.row_move-1,self.row_move+1):
            for col_index in range(self.col_move-1, self.col_move+1):

                if row_index < 0 or row_index > len(self.board) or col_index < 0 or col_index > len(self.board[0]):
                    print('Invalid Cell')
                    continue
                
                self.place_move(row_index, col_index)
                return True


    def invalid_move_check(self):
        direction = [[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1]]
        position = [self.row_move - 1,self.col_move - 1]
        result = []
        for element in direction:
            x = element[0] + position[0]
        
            y = element[1] + position[1]

            if x < 0 or y< 0 or x >= len(self.board) or y >= len(self.board[0]):
                continue
            if self.board[x][y] == self.turn:
                continue
            
            temporary = [] # list of coordinates (flipping disc coordinates)
            while x < len(self.board) and y < len(self.board[0]) and self.board[x][y] != self.turn:
                temporary.append([x,y])
                
                if x < 0 or y< 0 or x >= len(self.board) or y >= len(self.board[0]):
                    temporary = []
                    break 
                if self.board[x][y] == NONE:
                    temporary = []
                    break
                
                x += element[0]
                y += element[1]



            result.append(temporary)
        
        s = set()
        for coordinate in result:
            if len(coordinate) != 0:
                
                for point in coordinate:
                    s.add((point[0],point[1]))

        if len(s) != 0:
            for pt in s:
                self.flip(pt)
            return True
        return False 
                

        
    
    def flip(self, point):
        if self.board[point[0]][point[1]] == 1:
            self.board[point[0]][point[1]] = 2
        else:
            self.board[point[0]][point[1]] = 1
            
          
    def winner(self):
        if self.method == '>':
            if self.total_B > self.total_W:
                print('WINNER: BLACK')
            if self.total_B == self.total_W:
                print('WINNER: NONE')
            else:
                print('WINNER: WHITE')
        elif self.method == '<':
            if self.total_B < self.total_W:
                print('WINNER: BLACK')
            if self.total_B == self.total_W:
                print('WINNER: NONE')
            else:
                print('WINNER: WHITE')
    

    def quit_game(self):
        if self.total_B + self.total_W == (len(self.board)*len(self.board[1])):
            return True
            
            
            

