# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `uv run python tic_tac_toe.py` in the command line the game will start. Try it out! ;)

# 'X' 'O'
player1 = "X"
player2 = "O"
# first player is False, second player is True
currentplayer = False

turn = 1

gameboard = {
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9'
}

def printboard():
    print(f"-------------")
    print(f"| {gameboard[1]} | {gameboard[2]} | {gameboard[3]} |")
    print(f"-------------")
    print(f"| {gameboard[4]} | {gameboard[5]} | {gameboard[6]} |")
    print(f"-------------")
    print(f"| {gameboard[7]} | {gameboard[8]} | {gameboard[9]} |")
    print(f"-------------")

def initplayer():
    global player1,player2
    player1 = input("Player 1: choose X or O: ").upper()
    if not(player1 == "O" or player1 == "X"):
        initplayer()
    if (player1 == "O"):
        player2 = "X"
    return True

def cellisfull(mycell: int):
    if (gameboard[mycell] == 'X') or (gameboard[mycell] == 'O'):
        return True
    return False

def playturn():
    global currentplayer
    global turn
    # shows the current state of the board
    printboard()

    # currentplayer choose a number
    playername = "Player 2" if currentplayer else "Player 1"
    chosencell = input(f"Turn {turn} -- ** {playername} ** choose a number between 1 and 9: ")
    numcell = int(chosencell)
    if not(numcell in range(1,10)) or cellisfull(numcell):
        return False
    else:
        # update board
        if not currentplayer:
            gameboard[numcell] = player1
        else:
            gameboard[numcell] = player2
        #gameboard[numcell] = player1 if currentplayer else gameboard[numcell] = player2

        return True

def haswon(player: bool):
    # 8 possibilities
    # pattern is either "X" or "O"
    pattern = player2 if player else player1
    if (gameboard[1] == pattern) and (gameboard[2] == pattern) and (gameboard[3] == pattern):
        return True
    if (gameboard[4] == pattern) and (gameboard[5] == pattern) and (gameboard[6] == pattern):
        return True
    if (gameboard[7] == pattern) and (gameboard[8] == pattern) and (gameboard[9] == pattern):
        return True
    if (gameboard[1] == pattern) and (gameboard[4] == pattern) and (gameboard[7] == pattern):
        return True
    if (gameboard[2] == pattern) and (gameboard[5] == pattern) and (gameboard[8] == pattern):
        return True
    if (gameboard[3] == pattern) and (gameboard[6] == pattern) and (gameboard[9] == pattern):
        return True
    if (gameboard[1] == pattern) and (gameboard[5] == pattern) and (gameboard[9] == pattern):
        return True
    if (gameboard[3] == pattern) and (gameboard[5] == pattern) and (gameboard[7] == pattern):
        return True
    return False

def initgame():
    global turn,currentplayer
    turn = 1
    currentplayer = False
    if initplayer():
        while (not haswon(currentplayer) and turn <= 9):
            # play turn
            if playturn():        
                # switch player
                currentplayer = not(currentplayer)
                # increment turn
                turn += 1
        if (turn > 9):
            print("********* DRAW *********")
        else:
            winner = "Player 2" if currentplayer else "Player 1"
            print(f"********* {winner} won :D *********")


# Tic-tac-toe game
if __name__ == "__main__":
    # Start a new round of Tic-tac-toe
    print("Welcome to a new round of Tic-Tac-Toe!")
    initgame()