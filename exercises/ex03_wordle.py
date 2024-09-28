"""Playing Wordle!!! While Loops used"""

__author__ = "730756528"


def input_guess(secret_word_len: int) -> str:
    """Checking if the word given by the player has the same length with secret word"""
    guess: str = input(f"Enter a {secret_word_len} character word: ")
    while not len(guess) == secret_word_len:
        print(f" That wasn't {secret_word_len} chars! Try again: ")
        guess = input()
    print(guess)
    return guess


def contains_char(secret_word: str, char_guessed: str) -> bool:
    """Looking for the character"""
    assert len(char_guessed) == 1
    index: int = 0
    while index < len(secret_word):
        if secret_word[index] == char_guessed:
            return True
        else:
            index = index + 1
