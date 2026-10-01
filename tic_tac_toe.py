# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `uv run python tic_tac_toe.py` in the command line the game will start. Try it out! ;)

# Function for ... (displaying the board?)
def blabla():
    pass


# Function for... (choosing a player?)
def blablabla():
    pass


# ... write as many functions as you need


# Tic-tac-toe game
if __name__ == "__main__":
    # Start a new round of Tic-tac-toe
    print("Welcome to a new round of Tic-Tac-Toe!")

# 'X' 'O'
# playerA
# playerB
# gameboard = dict()

def initgame():
    gameboard = {
        1: ' ',
        2: ' ',
        3: ' ',
        4: ' ',
        5: ' ',
        6: ' ',
        7: ' ',
        8: ' ',
        9: ' '
    }

def printboard():
    print(f"| {gameboard[1]} | {gameboard[2]} | {gameboard[3]} |")
    print(f"| {gameboard[4]} | {gameboard[5]} | {gameboard[6]} |")
    print(f"| {gameboard[7]} | {gameboard[8]} | {gameboard[9]} |")