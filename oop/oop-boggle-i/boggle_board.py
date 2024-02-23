#!/usr/bin/env python3.12
import random

class BoggleBoard:

  DIE_DICT = {
    1 : 'AAEEGN',
    2 : 'ELRTTY',
    3 : 'AOOTTW',
    4 : 'ABBJOO',
    5 : 'EHRTVW',
    6 : 'CIMOTU',
    7 : 'DISTTY',
    8 : 'EIOSST',
    9 : 'DELRVY',
    10 : 'ACHOPS',
    11 : 'HIMNQU',
    12 : 'EEINSU',
    13 : 'EEGHNW',
    14 : 'AFFKPS',
    15 : 'HLNNRZ',
    16 : 'DEILRX'
  }

  def __init__(self, board_size=4, column_size=4):
    """Outputs new board when initialized
  
    """
    self.board_size = board_size
    self.column_size = column_size
    self.display_board()
    print('****************')

  def shake(self):
    """"Modifies the board by filling each cell with a random upper-case letter [A-Z] with no restrictions on letters

    """
    """
      Get random index from die_list
      Retrieve key/value from dict 
      Remove selected index from die_list
      Generate random letter from value of die
      remove die from dictionary
      Repeat until no dice left
    """
    die_list = [i for i in range(1,17)]

    rolled_dice = random.sample(die_list, k=16)

    row_count = 1
    str_output = ""

    # print(rolled_dice)

    # print(BoggleBoard.DIE_DICT[rolled_dice[0]])
    
    for str_die in range(0,len(rolled_dice)) :
      this_die = rolled_dice[str_die]

      this_die_line = BoggleBoard.DIE_DICT[this_die]
      # print(BoggleBoard.DIE_DICT[this_die])

      letter = this_die_line[random.randint(0,5)]

      # print(letter)

      if 'Q' in letter :
        letter = 'Qu '
      elif row_count < self.column_size:
        letter += "  "

      str_output += letter

      if row_count == self.column_size :
        print(f'* {str_output:^{13}}*')
        str_output = ""
        row_count = 1
      else:
        row_count += 1
    
    print('****************')
    


  def display_board(self):
    for _ in range(self.board_size):
      print('_'* self.column_size)

  def random_letter(self):
    """Generates random letter for each column in row
    """
    # ASCII A - 65
    # ASCII Z - 90
    line = ''

    for _ in range(self.column_size):
      line += chr(random.randint(65,90))

    return line

new_game = BoggleBoard()
new_game.shake()
new_game.shake()
new_game.shake()
new_game.shake()


# print(chr(random.randint(65,90)))
# print(chr(random.randint(65,90)))
# print(chr(random.randint(65,90)))
# print(chr(random.randint(65,90)))


# for _ in range(self.board_size):
#       print(self.random_letter())

#     print('****************')