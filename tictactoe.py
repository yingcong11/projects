#gameboard
def display_board(board):
    print(board[1]+"|"+board[2]+"|"+board[3])
    print(board[4]+"|"+board[5]+"|"+board[6])
    print(board[7]+"|"+board[8]+"|"+board[9])

#start game + player assignment
def game_start():
    print("Welcome to Tic Tac Toe")
    player1 = ""
    while player1 not in ["X", "O"]:
        player1 = input("Player 1, please select X or O: ").upper()
        if player1 not in ["X", "O"]:
            print("invalid input")
    if player1 == "X":
        player2 = "O"
        print("Player 1 is X and Player 2 is O")
    else:
        player2 = "X"
        print("Player 1 is O and Player 2 is X")
    return player1, player2

#Player 1 turn + update board + check win
def position_choice1():
    choice = " "
    while choice not in avail:
        choice = input("Player 1, please pick a position (1 to 9): ")
        if choice not in avail:
            print("Sorry, invalid choice!")
    avail.remove(choice)
    #print(avail)
    return int(choice)

def replacement_choice1(game_board, p1choice):
    game_board[p1choice] = player1
    return game_board

def check_win1():
    if game_board[1] == game_board[2] == game_board[3] == player1:
        print("Player1 Win!")
        return True
    elif game_board[4] == game_board[5] == game_board[6] == player1:
        print("Player1 Win!")
        return True
    elif game_board[7] == game_board[8] == game_board[9] == player1:
        print("Player1 Win!")
        return True
    elif game_board[1] == game_board[4] == game_board[7] == player1:
        print("Player1 Win!")
        return True
    elif game_board[2] == game_board[5] == game_board[8] == player1:
        print("Player1 Win!")
        return True
    elif game_board[3] == game_board[6] == game_board[9] == player1:
        print("Player1 Win!")
        return True
    elif game_board[3] == game_board[5] == game_board[7] == player1:
        print("Player1 Win!")
        return True
    elif game_board[1] == game_board[5] == game_board[9] == player1:
        print("Player1 Win!")
        return True
    else:
        return False

#Player 2 turn + update board + check win
def position_choice2(game_won1):
    choice = " "
    if game_won1:
        return " "
    elif avail == []:
        print("No more moves! Tie!")
        return " "
    else:
        while choice not in avail:
            choice = input("Player 2, please pick a position (1 to 9): ")
            if choice not in avail:
                print("Sorry, invalid choice!")
        avail.remove(choice)
        #print(avail)
        return int(choice)

def replacement_choice2(game_board, p2choice):
    if p2choice == " ":
        return game_board
    else:
        game_board[p2choice] = player2
        return game_board

def check_win2(game_won1):
    if not game_won1:
        if game_board[1] == game_board[2] == game_board[3] == player2:
            print("Player 2 Win!")
            return True
        elif game_board[4] == game_board[5] == game_board[6] == player2:
            print("Player 2 Win!")
            return True
        elif game_board[7] == game_board[8] == game_board[9] == player2:
            print("Player 2 Win!")
            return True
        elif game_board[1] == game_board[4] == game_board[7] == player2:
            print("Player 2 Win!")
            return True
        elif game_board[2] == game_board[5] == game_board[8] == player2:
            print("Player 2 Win!")
            return True
        elif game_board[3] == game_board[6] == game_board[9] == player2:
            print("Player 2 Win!")
            return True
        elif game_board[3] == game_board[5] == game_board[7] == player2:
            print("Player 2 Win!")
            return True
        elif game_board[1] == game_board[5] == game_board[9] == player2:
            print("Player 2 Win!")
            return True
        else:
            return False
    else:
        pass

#continue game if no win
def gameon_choice(game_won1, game_won, p2choice):
    while not game_won1 and not game_won and p2choice != " ":
        return True
    while game_won1 or game_won or p2choice == "":
        print("Game Over!")
        return False

#start new game if game ended
def new_game(game_on):
    if not game_on:
        choice = ""
        while choice not in ["Y", "N"]:
            choice = input("Start new game? (Y or N): ").upper()
            if choice not in ["Y", "N"]:
                print("Sorry, I dont' understand, please choose Y or N")
        if choice == "Y":
            return True
        else:
            print("Game Over!")
            return False

start_game = True
while start_game:
    player1, player2 = game_start()
    game_on = True
    game_won = False
    game_board = [" "]*10
    avail = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    display_board(game_board)
    while game_on:
        p1choice = position_choice1()
        game_board = replacement_choice1(game_board, p1choice)
        display_board(game_board)
        game_won1 = check_win1()
        p2choice = position_choice2(game_won1)
        game_board = replacement_choice2(game_board, p2choice)
        if not game_won1 and p2choice != " ":
            display_board(game_board)
        else:
            pass
        game_won = check_win2(game_won1)
        game_on = gameon_choice(game_won1, game_won, p2choice)
    start_game = new_game(game_on)
