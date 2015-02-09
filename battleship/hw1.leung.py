#!usr/bin/python 2.7
#Audrey Leung

from random import randint

def main():
    print "Let's play Battleship!"
    print "You have 4 turns to guess the location of 2 ships."
    board = []
    for x in range(5):
        board.append(["O"] * 5)
    print_board(board)
    ship1 = ship1_location(board)
    ship2 = ship2_location(board)
    while check_overlap(ship1,ship2) == True:
        ship2 = ship2_location(board)
    play_game(ship1,ship2,board)

def print_board(board):
    for row in board:
        print " ".join(row)

#randomize ship1 3 x 1 location
def ship1_location(board):
    orientation1 = randint(0,1)
    ship1_rows = []
    ship1_cols = []
    ship1_loc = []
    if orientation1 == 0: # if horizontal
        ship1_row1 = randint(0, len(board)-1)
        ship1_row2 = ship1_row1
        ship1_row3 = ship1_row1

        ship1_col1 = randint(0, 2)
        ship1_col2 = ship1_col1 + 1
        ship1_col3 = ship1_col2 + 1

        ship1_rows = [ship1_row1, ship1_row2, ship1_row3]
        ship1_cols = [ship1_col1, ship1_col2, ship1_col3]
        ship1_loc = zip(ship1_rows,ship1_cols) 

    elif orientation1 == 1: # if vertical
        ship1_col1 = randint(0, len(board[0])-1)
        ship1_row1 = randint(0,2)

        ship1_rows = range(ship1_row1, ship1_row1 + 3)
        ship1_cols = [ship1_col1] * 3
        ship1_loc =  zip(ship1_rows,ship1_cols)
        
    return ship1_loc

#adding the second 2 x 1 ship 
def ship2_location(board):
    orientation2 = randint(0,1)
    ship2_rows = []
    ship2_cols = []
    ship2_loc = []
    if orientation2 == 0: # if horizontal
        ship2_row1 = randint(0, len(board)-1)
        ship2_col1 = randint(0, 3)
      
        ship2_rows = [ship2_row1] * 2
        ship2_cols = range(ship2_col1, ship2_col1 + 2)
        ship2_loc = zip(ship2_rows,ship2_cols)
        
    elif orientation2 == 1: # if vertical
        ship2_col1 = randint(0, len(board[0])-1)
        ship2_row1 = randint(0,3)
    
        ship2_rows = range(ship2_row1, ship2_row1 + 2)
        ship2_cols = [ship2_col1] * 2
        ship2_loc = zip(ship2_rows,ship2_cols)

    return ship2_loc

#making sure it doesn't overlap or touch the first one. True if overlap. 
def check_overlap(coordinate_list1,coordinate_list2):
    for coordinate in coordinate_list1:
        if coordinate in coordinate_list2:
           return True
    return False

def play_game(ship1,ship2,board):
    turn = 1
    while turn <= 4:
        print "You are on turn", turn

        guess_row = int(raw_input("Guess Row:"))
        guess_col = int(raw_input("Guess Col:"))
        guess_coord = [(guess_row,guess_col)]
        
        if check_overlap(guess_coord,ship1) == True:
            print "Congratulations! You sunk my battleship!"
            break
        if check_overlap(guess_coord,ship2):
            print "Congratulations! You sunk my battleship!"
            break
        if guess_row == 17 and guess_col == 17:
            print 'Secret coordinates hit! Location of ship 1 is',ship1
            print 'Secret coordinates hit! Location of ship 2 is',ship2 
            # for coordinate in ship1:
            #     print_board()print "You are on turn", turn, "."
        elif (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
            turn += 1
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
            turn += 1
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
            turn += 1
            print_board(board)
    if turn == 5:
        print "No more turns. Game Over!"
        

if __name__ == "__main__":
    main()
    
    
    