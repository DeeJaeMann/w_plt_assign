#!/usr/bin/env python3.11

from rich.table import Table
from rich.console import Console
from rich import box
import re
import random

'''
    Features:
    High-Level Features:
     - Human player turn
     - Computer player turn
     - Getting human player input
     - Printing the board for the human player to see
     - Check after every move to verify:
        - Someone won
        - Cats game
     
    Computer AI
     - Long Term: Smart AI
     - Short Term: functional - simple (random gen)

    User Input:
     - User inputs their move for each turn
        - Input Row & Column for move
        - Long Term: Allow user to specify X or O
        - Display current board state

    Flow:
     - Who goes first -> Player A (Human)
     - A makes move
     - Player B turn (AI)
     - ... until game finished

    Human Player:
     - Need to be able to see the board
     - Prompt for move
     - Instructions on how to enter move

    AI:
     - Random gen move
     - Need to know if generated move is valid or not
'''

# Constants for positions
X = "X"
O = "O"
EMPTY = ""



# Begin Helper Functions

def display_board(lst_board) :
    """Displays the current board state
    Args:
        lst_board: List of current board status
    Returns:
        Pretty formated game board
    """
    table = Table(title="Tic-Tac-Toe", show_lines=True, box=box.ROUNDED)

    table.add_column("")
    table.add_column("A", justify="center")
    table.add_column("B", justify="center")
    table.add_column("C", justify="center")

    table.add_row("1",f'{lst_board[0][0]}',f'{lst_board[0][0]}',f'{lst_board[0][0]}')
    table.add_row("2",f'{lst_board[1][0]}',f'{lst_board[1][1]}',f'{lst_board[1][2]}')
    table.add_row("3",f'{lst_board[2][0]}',f'{lst_board[2][1]}',f'{lst_board[2][2]}')

    return table

def get_row(str_move) :
    """Converts the row to an index by subracting 1
    Args:
        str_move String with the coordinates of the player move
    Returns:
        Converted index for use in the board list
    """
    return int(str_move[1])-1

def get_col(str_move) :
    """Converts the column from a letter to an index
    Args:
        str_move String with the coordinates of the player move
    Returns:
        Converted index for use in the board list
        """
    # Convert the column from a letter to a position
    match str_move[0].upper() :
        case "A" :
            return 0
        case "B" :
            return 1
        case _:
            return 2

def validate_move(str_move, lst_board) :
    """Validates the move entered to open board positions

    Args:
        str_move Character and Number for board position
        lst_board Current board state (list)
    Returns:
        True if move is valid
        False if position is taken
    """

    int_col = get_col(str_move)
    int_row = get_row(str_move)

    if lst_board[int_row][int_col] == EMPTY : 
        return True
    
    return False

def update_move(str_move, lst_board, str_turn) :
    int_col = get_col(str_move)
    int_row = get_row(str_move)

    if str_turn == "player" :
        lst_board[int_row][int_col] = X
    else :
        lst_board[int_row][int_col] = O

    return lst_board

def generate_ai_move() :
    int_col = random.choice([0,1,2])
    int_row = random.choice([0,1,2])

    return f'{int_row}{int_col}'

def check_rows_and_columns(lst_board) :

    for int_row in lst_board:
        if len(set(int_row)) == 1:
            return int_row[0]
        
    for int_col in range(len(lst_board)) :
        if len(set(lst_board[int_row][int_col] for int_row in range(len(lst_board)))) == 1:
            return lst_board[0][int_col]
        
    return None

def check_board(lst_board) :

    str_rows_cols_winner = check_rows_and_columns(lst_board)

    return str_rows_cols_winner
    

# End Helper Functions

def play_game() :
    """Runs the main Tic-Tac-Toe game
    
    Args:
        none
    Returns:
        Status of whether the player won or not
    """

    # Game state
    game_over = False
    str_turn = "player"

    console = Console()

    # Create a blank tic-tac-toe board
    lst_board = [
        [EMPTY,EMPTY,EMPTY],
        [EMPTY,EMPTY,EMPTY],
        [EMPTY,EMPTY,EMPTY],
    ]

    # Main game loop
    while game_over == False :
        # Display the game board
        console.print(display_board(lst_board))

        if str_turn == "player" :
            # Get user input
            str_player_move = input("Enter your move (Letter then Number ie. A1): ")

            # Validate user input
            regex_pattern = re.compile("^[ABC][123]$", re.I)

            if re.search(regex_pattern, str_player_move) :
                # We have valid input
                if validate_move(str_player_move, lst_board) :
                    lst_board = update_move(str_player_move, lst_board, str_turn)

                    console.print(display_board(lst_board))

                    str_turn = "ai"   
                else :
                    print("That position is taken!")
                pass
            else :
                # Invalid input
                print("That is not a valid move!")
        else :
            str_ai_move = generate_ai_move()
            while validate_move(str_ai_move, lst_board) == False :
                str_ai_move = generate_ai_move()
            
            lst_board = update_move(str_ai_move, lst_board, str_turn)
            str_turn = "player"
        
        #game_over = True
        if(check_board(lst_board)) :
            game_over = True


    return str_player_move

print(play_game())


