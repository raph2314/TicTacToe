from IPython.display import clear_output

def play_game():
    board = generate_board()
    take_turns(board)
    pass

def generate_board():
    board = []
    for entry in xrange(10):
        board.append('     ')
    return board
    pass

def display_board(board):
    clear_output()
    print('       |   ' + '    |     ')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' ')
    print('-----------------------')
    print('       |   ' + '    |     ')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' ')
    print('-----------------------')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' ')
    print('       |   ' + '    |     ')
    pass

def get_input(player_num, board):
    try:
        location = int(raw_input('Player #' + str(player_num) + ', where would you like to play?'))
    except ValueError:
        #Pass out of range value that will be caught by is_valid_input
        location = 1000
    if not is_valid_input(location, board):
        clear_output()
        display_board(board)
        print('Invalid input. Please try again')
    return location

def is_valid_input(location, board):
    is_valid = True
    #Deal with invalid strings
#     try: 
#         int(location)
#     except ValueError:
#         is_valid = True
        
    #Deal with invalid ranges
    if location >= 10 or location <= 0:
        is_valid = False
        
    #Deal with filled slots
    elif board[location - 1] != '     ':
        is_valid = False
        
    return is_valid
    pass

def update_board(player_num, location, board):
    if player_num == 1:
        board[location - 1] = '  X  '
    if player_num == 2:
        board[location - 1] = '  O  '
    display_board(board)
    pass

def is_win(player_num, board):
    winning_combinations = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for combo in winning_combinations:
        if(board[combo[0]] == 'X' and board[combo[1]] == 'X' and board[combo[2]] == 'X'):
            print('Player 1 has won the game!!!')
            return True
        elif(board[combo[0]] == 'O' and board[combo[1]] == 'O' and board[combo[2]] == 'O'):
            print('Player 2 has won the game!!!')
            return True
    #Return true for any winning combination, and false otherwise
    return False
    pass

def take_turns(board):
    turn = 1
    player_num = 1
    winning_turn = is_win(player_num, board)
    winning_combinations = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    won = False

    while not won and turn < 10:
        #Determine player_num
        if turn % 2 == 1:
            player_num = 1
        else:
            player_num = 2
            
        location = get_input(player_num, board)
        if not is_valid_input(location, board):
            continue
        update_board(player_num, location, board)
         
        for combo in winning_combinations:
            if(board[combo[0]-1] == '  X  ' and board[combo[1]-1] == '  X  ' and board[combo[2]-1] == '  X  '):
                print('Player 1 has won the game!!!')
                won = True
            elif(board[combo[0]-1] == '  O  ' and board[combo[1]-1] == '  O  ' and board[combo[2]-1] == '  O  '):
                print('Player 2 has won the game!!!')
                won = True
        turn += 1
            
    pass

play_game()
