"""Playing Wordle!!! While Loops used"""

__author__ = "730756528"


def input_guess(secret_word_len: int) -> str:
    guess: str = input(f"Enter a {secret_word_len} character word: ")
    while True:
        if (len(guess) < secret_word_len) or (len(guess) > secret_word_len):
            print(f" That wasn't {secret_word_len} chars!")
            guess = input("Try again: ")
        else:
            print(guess)
            return guess


input_guess(secret_word_len=5)
