import random

def display_board(board):
    '''
    Print our a board. Set up board as a list, where each index 1-9
    '''
    print('-----')
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-|-|-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-|-|-')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-----')
    
#test_board = ['#','X','O','X','O','X','O','X','O','X']
#display_board(test_board)


def player_input():
    '''
    Take in a player input & assign their marker as 'X' or 'O'
    '''
    marker = input('Do you want to be X or O? ').upper()
    while marker != 'X' and marker!= 'O':
        marker = input('Pick X or O ').upper()

    player1 = marker
    
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
        
    return(player1,player2)

def place_marker(board, marker, position):
    '''
    Takes in the board list object, a marker ('X' or 'O'), and a
    desired position (number 1-9) & assigns it to the board.
    '''
    board[position] = marker
    
#test_board = ['#','X','O','X','O','X','O','X','O','X']
#place_marker(test_board,'$',8)
#display_board(test_board)

def win_check(board,mark):
    '''
    Takes in a board & a mark (X or O) & then checks to see if
    the mark has won.
    '''
    return ((board[1]==board[2]==board[3]==mark) or
    (board[1]==board[4]==board[7]==mark) or
    (board[1]==board[5]==board[9]==mark) or
    (board[4]==board[5]==board[6]==mark) or
    (board[7]==board[8]==board[9]==mark) or
    (board[2]==board[5]==board[8]==mark) or
    (board[3]==board[6]==board[9]==mark) or
    (board[7]==board[5]==board[3]==mark))

#win_check(test_board,'X')
#returns True if it works

def choose_first():
    '''
    Use random module to randomly decide which player goes first.
    Return a string of which plyer went first.
    '''
    x = random.randint(0,1)
    if x == 0:
        print('Player 1 goes first')
    else:
        print('Player 2 goes first')

def space_check(board,position):
    '''
    Returns a boolean indicating whether a space on the board is freely
    available.
    '''
    return board[position] == ' '

def full_board_check(board):
    '''
    Checks if the board if full & returns a boolean value.
    True if full, False otherwise.
    '''
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    '''
    Asks for a player's next position (as a number 1-9) & then uses
    the function from function 6 to check if it's a free position.
    If it is, then return the position for later use.
    '''
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your position: '))

    return position
    

def replay():
    '''
    Asks the player if they want to play again & returns a boolean
    True if they go want to play again.
    '''
    x = input('Do you want to play again? Put Yes or No ')
    return x == 'Yes'

#Use while loops & functions you've made to run the game!
print('Welcome to Tic Tac Toe!')

while True:
    official_board = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    play_game = input('Are you ready to play? Yes or No? ')

    if play_game == 'Yes':
        game_on = True
    else:
        game_on = False
        
    while game_on == True:
        if turn == 'Player 1':
            display_board(official_board)
            position = player_choice(official_board)
            place_marker(official_board, player1_marker, position)
            if win_check(official_board, player1_marker):
                display_board(official_board)
                print('Congratulation, you win!')
                game_on = False
            else:
                if full_board_check(official_board):
                    display_board(official_board)
                    print('It is a tie!')
                    game_on = False
                else:
                    turn = 'Player 2'
                        
                
            
        else:
            display_board(official_board)
            position = player_choice(official_board)
            place_marker(official_board, player2_marker, position)
            if win_check(official_board, player2_marker):
                display_board(official_board)
                print('Congratulation, you win!')
                game_on = False
            else:
                if full_board_check(official_board):
                    display_board(official_board)
                    print('It is a tie!')
                    break
                else:
                    turn = 'Player 1'
                    
    if not replay():
        break
        

    
    


        
    


    






            
