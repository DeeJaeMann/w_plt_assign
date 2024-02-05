#!/usr/bin/env python3.11

from rich.table import Table
from rich.console import Console
from rich import box

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

    table.add_row("1",f'{lst_board[0][0]}',f'{lst_board[1][0]}',f'{lst_board[2][0]}')
    table.add_row("2",f'{lst_board[0][1]}',f'{lst_board[1][1]}',f'{lst_board[2][1]}')
    table.add_row("3",f'{lst_board[0][2]}',f'{lst_board[1][2]}',f'{lst_board[2][2]}')

    return table

# End Helper Functions

def play_game() :
    """Runs the main Tic-Tac-Toe game
    
    Args:
        none
    Returns:
        Status of whether the player won or not
    """

    # Create a blank tic-tac-toe board
    lst_board = [
        ['','',''],
        ['','',''],
        ['','',''],
    ]
    console = Console()
    console.print(display_board(lst_board))

print(play_game())


