"""Playing Wordle!!! While Loops used"""

__author__ = "730756528"


def input_guess(secret_word_len: int) -> str:
    """Checking if the word given by the player has the same length with secret word"""
    guess_word: str = input(f"Enter a {secret_word_len} character word: ")
    while not len(guess_word) == secret_word_len:
        print(f" That wasn't {secret_word_len} chars! Try again: ")
        guess_word = input()
    print(guess_word)
    return guess_word


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Defining the contains_char function: it searches for the character"""
    assert len(char_guess) == 1
    index: int = 0
    while index < len(secret_word):
        if secret_word[index] == char_guess:
            return True
        else:
            index = index + 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Emojified:compares 2 strs, indicates if chars in correct place w/emoji string"""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index_2: int = 0
    emoji_string: str = ""
    while index_2 < len(guess):
        if guess[index_2] == secret[index_2]:
            emoji_string = emoji_string + GREEN_BOX
            index_2 = index_2 + 1
        elif contains_char(secret_word=secret, char_guess=guess[index_2]) is True:
            emoji_string = emoji_string + YELLOW_BOX
            index_2 = index_2 + 1
        else:
            emoji_string = emoji_string + WHITE_BOX
            index_2 = index_2 = 1
    return emoji_string


emojified(guess="hello", secret="world")
