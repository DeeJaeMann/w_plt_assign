#!/usr/bin/env python3.12
class GuessingGame():
    """GuessingGame class"""
    str_last_guess = ""
    def __init__(self, int_answer) :
        """Creates instance of guessing game
        
        Args:
            int_answer - (int) Answer
        Returns:
            None
        """
        self.answer = int_answer
        pass

    def guess(self, int_user_guess) :
        """Submits guess to check
        
        Args:
            int_user_guess - (int) Guess to check
        Returns:
            (string) Result of check: 'high', 'low', 'correct'
        """
        if int_user_guess > self.answer :
            GuessingGame.str_last_guess = "high"
        elif int_user_guess < self.answer  :
            GuessingGame.str_last_guess = "low"
        else :
            GuessingGame.str_last_guess = "correct"
        
        return GuessingGame.str_last_guess

    def solved(self) :
        """Checks if last guess was correct
        
        Args:
            None
        Returns:
            (bool) Result of check: True - Solved, False - Not Solved
        """
        if GuessingGame.str_last_guess == "correct" :
            return True
        else :
            return False
        
game = GuessingGame(10)

print(game.solved())

print(game.guess(5))
print(game.guess(20))
print(game.solved())

print(game.guess(10))
print(game.solved())
