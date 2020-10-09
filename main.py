import random
def board_view(b):
    b11, b12, b13=str(b[0][0]), str(b[0][1]), str(b[0][2])
    b21, b22, b23=str(b[1][0]), str(b[1][1]), str(b[1][2])
    b31, b32, b33=str(b[2][0]), str(b[2][1]), str(b[2][2])
    print(b11+' | '+b12+' | '+b13)
    print('---------')
    print(b21+' | '+b22+' | '+b23)
    print('---------')
    print(b31+' | '+b32+' | '+b33)
def players_com():
    print("----Players---")
    print("-Player vs. Player(1)")
    print("-Player vs. COM(2)")
    i=input(":")
    print("\n")
    return i
def options_menu(num=0):
    print("----Options---")
    if num==0:
        print("-Players:",'\t', "Two")
    else:
        print("-Players:",'\t', "One")
    print("-Exit")
    i=input(":")
    print("\n")
    return i
def menu():
    print("-----MENU-----")
    print("-PLAY")
    print("-Options")
    print("-Exit")
    i=input(":")
    print("\n")
    return i
def make_board():
    m=[['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    return m
def print_board(board):
    for i in range(len(board)):
        print(board[i])
def clear(board):
    return make_board()
def make_move(who,row,col, board):
#   	кто, строка, колонка, доска
#   "Сделать ход на позицию row, col"
    if board[col-1][row-1]=='_':
        if who == 'x':
            board[col-1][row-1]='x'
            print_board(board)
        else:
            board[col-1][row-1]='o'
            print_board(board)
    else:
        print('Error. Repeat Values')
        row=int(input('Row?: '))
        col=int(input('Col?: '))
        make_move(who, row, col, board)
def COMrandom(board):
    c=[]
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == '_':
                c.append([i, j])
    rand = 0
    rand = random.randint(0, len(c)-1)
    return c[rand]
def hasWon(who,board):
    for i in range(len(board)):
        if board[i][0]==who:
            if board[i][1] == who:
                if board[i][2] == who:
                    print(who,'won')
                    return who
        if board[0][i] == who:
            if board[1][i]==who:
                if board[2][i]==who:
                    print(who,'won')
                    return who
    if board[0][0]==who:
        if board[1][1] ==who:
            if board[2][2]==who:
                print(who,'won')
                return who
    elif board[0][2] == who:
        if board[1][1] ==who:
            if board[2][0]==who:
                print(who,'won')
                return who
    return False

def gameOver(board):
    c=0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] !='_':
                c=c+1
    if c<len(board)**2:
        return False
    print('Draw!')
    return True
def game():
    global pla_c
    global FirstRun
    if FirstRun == 0:
        pla_c=1
        FirstRun = 1
    print("--------------")
    print(" TIC-TAC-TOE")
    men = menu()
    if men == "PLAY":
        print(pla_c)
        if pla_c == 1:
            b = make_board()
            #print_board(b)
            board_view(b)
            Player1 = input('First player name: ')
            xoro = input('x or o?: ')
            Player2=input('Second player name: ')
            if xoro == 'x':
                x1='x'
                x2='o'
                print(Player1+' - x')
                print(Player2+' - o')
            else:
                x1='o'
                x2='x'
                print(Player1+' - o')
                print(Player2+' - x')
            t=0
            who=input('Who start first?: ')
            while t==0:
                if who == ( x1 or Player1 ):
                    print(Player1+', your turn')
                elif who == ( x2 or Player2 ):
                    print(Player2+', your turn')
                row=int(input('Row?: '))
                col=int(input('Col?: '))
                make_move(who,row,col, b)
                if hasWon(who,b) == who:
                    t+=1
                    if who == x1 or Player1:
                        print(Player1+', you won!')
                    else:
                        print(Player2+', you won!')
                if gameOver(b) == True:
                    t+=1
                if who == ( x1 or Player1 ):
                    who = x2
                elif who == (x2 or Player2 ):
                    who = x1
            clear(b)
            NewGame=input('New Game?: ')
            while NewGame=='yes':
                game()
                NewGame=input('New Game?: ')
        if pla_c != 1:
        
        
        
        
            b = make_board()
            #print_board(b)
            board_view(b)
            Player1 = input('Player name: ')
            xoro = input('x or o?: ')
            COM="COM"
            if xoro == 'x':
                x1='x'
                x2='o'
                print(Player1+' - x')
                print(COM+' - o')
            else:
                x1='o'
                x2='x'
                print(Player1+' - o')
                print(COM+' - x')
            t=0
            who=input('Who start first?: ')
            while t==0:
                if who == ( x1 or Player1 ):
                    print(Player1+', your turn')
                    row=int(input('Row?: '))
                    col=int(input('Col?: '))
                    make_move(who,row,col, b)
                elif who == ( x2 or COM ):
                    print(COM+' turn')
                    COMturn=[]
                    COMturn = COMrandom(b)
                    row = COMturn[0]
                    col = COMturn[1]
                    make_move(who,row,col, b)
                if hasWon(who,b) == who:
                    t+=1
                    if who == x1 or Player1:
                        print(Player1+', you won!')
                    else:
                        print(COM+' won!')
                if gameOver(b) == True:
                    t+=1
                if who == ( x1 or Player1 ):
                    who = x2
                elif who == (x2 or COM ):
                    who = x1
            clear(b)
            NewGame=input('New Game?: ')
            while NewGame=='yes':
                game()
                NewGame=input('New Game?: ')
        
        
        
        
        
        
        
        
        menu()
    elif men == "Options":
        omen=options_menu()
        while omen == "Players":
            pla_c=players_com()
            if pla_c == '1':
                pla_c == 1
                omen = options_menu()
            else:
                pla_c == 2
                omen =options_menu(1)
        game()
    else:
        print('Exit in process...')

FirstRun=0
game()