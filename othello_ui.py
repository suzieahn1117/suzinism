# PROJECT 4
# othello_ui

import othello_logic

def user_input(): # ASK USER FOR INITIAL SET UP
    
    result = []
    for numbers in range(5):
        x = input( )
        result.append(x)
    return result

def move_input() -> str:
    x = input()
    for element in x:
        y = x.split(' ')
    print(y)
    return y

if __name__ == "__main__":
    result = user_input()
    x = othello_logic.game(result)
    x.disc_center()
    x.count_dock()
    x.print_count()
    x.print_board()


    while(True):
        if x.turn == 1:
            print('TURN: B')
        elif x.turn == 2:
            print('TURN: W')
        x.set_move(move_input())
        if x.valid_move() == True:
            print('VALID')
        x.count_dock()
        x.print_count()
        x.print_board()
        if x.quit_game() == True:
            break
    x.winner()


    

