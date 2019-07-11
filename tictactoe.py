'''
A game of Tic Tac Toe for 2 local players.
Rows are numbered top to bottom (numbers 1 through 3).
Columns are numbered from left to right (numbers 1 through 3).
The winner is the first player to mark 3 adjacent tiles.
'''
from random import randint #Import to randomized first turn.
from os import system #Import to clear cmd after each turn.

# 3 lists with 3 empty spaces. Will each store the player marks and print in adequate spot.
# Will serve as game board with total 9 spaces.
r1 = [' ']*3
r2 = [' ']*3
r3 = [' ']*3

markp1 = "X" # X mark for player 1.
markp2 = "O" # X mark for player 2.
mark = '' # Placeholder for mark which will change depending on whose turn it is.
taken_spots = [] #Empty list to be filled with spots taken by the player.
winner = False #Boolean to determine if someone won in order to take the next actions. 
turn = randint(1,2) #Random integer from 1 to 2 to decide which player goes first.


def gameboard_status():
    '''
    Prints the current layout of the game board using the predetermined lists of rows (r1,r2,r3)
    and the corresponding marks (or spaces if unoccupied).
    '''
    system('cls')
    print('     {0:^3} {1:^3} {2:^3}\n'.format('1','2','3'))
    print('1    {0:^3}|{1:^3}|{2:^3}'.format(r1[0], r1[1], r1[2]))
    print('     {0:^1}+{1:^1}+{2:^1}'.format('---', '---', '---'))
    print('2    {0:^3}|{1:^3}|{2:^3}'.format(r2[0], r2[1], r2[2]))
    print('     {0:^1}+{1:^1}+{2:^1}'.format('---', '---', '---'))
    print('3    {0:^3}|{1:^3}|{2:^3}'.format(r3[0], r3[1], r3[2]))

def player_input():
    '''
    Persistant function that asks for input. Will NOT allow invalid or repeated coordinates
    '''

    while True:
    
        r = int(input("Choose the row of the desired location: "))
        c = int(input("Choose the column of the desired location: "))
            
        if r>3 or c>3:
            print ("Woa! Let's stay inside the gameboard for now...")
        elif (r,c) in taken_spots:
            print ("Oops! Looks like that spot is taken.")
        else:
            taken_spots.append((r,c)) #Will be used to define draw when gameboard is full.
            return r,c

def player_mark(alist1,alist2,alist3):
    '''
    Function that updates the marks inside the lists depicting the gameboard. 
    '''
    
    if r == 1:
        alist1[(c-1)] = mark
        return alist1, alist2, alist3
    elif r == 2:
        alist2[(c-1)] = mark
        return alist1, alist2, alist3
    elif r == 3:
        alist3[(c-1)] = mark
        return alist1, alist2, alist3

gameboard_status() # Calling Gameboard to start the game.

while winner == False: #While Loop to keep gaming running until winner has been decided.
    if turn % 2 == 1: #If-Else Loop that changes players for each turn by using even and odd numbers.
        mark = markp1 #Switches the current mark to match the current player's turn.
        print ("P1's turn") 
        (r,c) = player_input() #Takes in the coordinates being entered by player.
        r1, r2, r3 = player_mark(r1,r2,r3) #Marks the gameboard accordingly.
        gameboard_status() #Displays gameboard once again.
    else:
        mark = markp2
        print ("P2's turn")
        (r,c) = player_input()
        r1, r2, r3 = player_mark(r1,r2,r3)
        gameboard_status()
    
    if r1 == ['X']*3 or r2 == ['X']*3 or r3 == ['X']*3: #Victory for P1 connecting a row.
        print ("P1 horizontalizes past Victory!")
        input("Press <Enter> to Exit...")
        winner = True
    elif r1 == ['O']*3 or r2 == ['O']*3 or r3 == ['O']*3: #Victory for P2 connecting a row.
        print ("P2 horizontalizes past Victory!")
        input("Press <Enter> to Exit...")
        winner = True
    elif (r1[0] == 'X' and r2[0] == 'X' and r3[0] == 'X') or\
        (r1[1] == 'X' and r2[1] == 'X' and r3[1] == 'X') or\
        (r1[2] == 'X' and r2[2] == 'X' and r3[2] == 'X'): #Victory for P1 connecting a column.
        print ("P1 verticalizes to Victory!")
        input("Press <Enter> to Exit...")
        winner = True
    elif (r1[0] == 'O' and r2[0] == 'O' and r3[0] == 'O') or\
         (r1[1] == 'O' and r2[1] == 'O' and r3[1] == 'O') or\
         (r1[2] == 'O' and r2[2] == 'O' and r3[2] == 'O'): #Victory for P2 connecting a column.
        print ("P2 verticalizes to Victory!")
        input("Press <Enter> to Exit...")
        winner = True
    elif (r1[0] == 'X' and r2[1] == 'X' and r3[2] == 'X') or\
         (r1[2] == 'X' and r2[1] == 'X' and r3[0] == 'X'): #Victory for P1 connecting diagonally.
        print ("P1 diagonalizes through Victory!")
        input("Press <Enter> to Exit...")
        winner = True
    elif (r1[0] == 'O' and r2[1] == 'O' and r3[2] == 'O') or\
         (r1[2] == 'O' and r2[1] == 'O' and r3[0] == 'O'): #Victory for P2 connecting a row.
        print ("P2 diagonalizes through Victory!")
        input("Press <Enter> to Exit...")
        winner = True
    elif len(taken_spots) >= 9 and winner == False: #Case where gameboard gets full there hasn't been a winner.
        print("It ain't Victory nor Defeat: DRAW")
        rematch = input("GG, Rematch? (yes or no)") #If draw, game will ask for rematch.
        if rematch.lower() == 'yes' or rematch.lower() == 'y' or rematch.lower() == 'yeah': #if players agree to rematch.
            #Reset game status.
            r1 = [' ', ' ', ' ']
            r2 = [' ', ' ', ' ']
            r3 = [' ', ' ', ' ']
            taken_spots = []
            winner = False
            turn = randint(1,2)
            gameboard_status()
        else:  #Players reject rematch. Game closes.
            break
    
    turn += 1 #Adds 1 to the turn number (alternating between even and odd, and therefore switching succesfully players) 
    continue