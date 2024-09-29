"""Playing Wordle!!! While Loops used"""

__author__ = "730756528"


def main(
    secret: str,
) -> (
    None
):  # main function to put everything together and call other functions in correct order
    """The entry point of the program and main game loop"""
    turn: int = 1  # turn variable to keep track of how many words the player guesses
    won: bool = False
    while turn <= 6 and not won:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {turn}/6 turns!")
            won = True  # making the condition true so the while loop will stop when user won
        turn = turn + 1
    if turn > 6:
        print("X/6 - Sorry, try again tomorrow!")


def input_guess(secret_word_len: int) -> str:
    """Checking if the word given by the player has the same length with secret word"""
    guess_word: str = input(
        f"Enter a {secret_word_len} character word: "
    )  # prompting the user to guess a word
    while not len(guess_word) == secret_word_len:
        guess_word = input(
            f" That wasn't {secret_word_len} chars! Try again: "
        )  # to make this phrase appear in the same line: put everything in input
    print(guess_word)
    return guess_word


def contains_char(secret_word: str, char_guess: str) -> bool:  # returns bool
    """Defining the contains_char function: it searches for the character"""
    assert (
        len(char_guess) == 1
    )  # we know that the character is going to be 1 single char
    index: int = 0
    while index < len(secret_word):  # looking for the char_guess in secret_word loop
        if secret_word[index] == char_guess:
            return True
        else:
            index = index + 1
    return False  # if char not found, return False


def emojified(guess: str, secret: str) -> str:
    """Emojified:compares 2 strs, indicates if chars in correct place w/emoji string"""
    assert len(guess) == len(
        secret
    )  # we know guess and secret are going to have the same number of chars
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = (
        "\U0001F7E9"  # codes for boc emojis, assigned here as variables for easier use
    )
    YELLOW_BOX: str = "\U0001F7E8"
    index_2: int = 0
    emoji_string: str = ""  # emoji string variable to write the emoji string
    while index_2 < len(
        guess
    ):  # while loop to add corrent boxes to the emoji string after searching for the same chars
        if guess[index_2] == secret[index_2]:
            emoji_string = emoji_string + GREEN_BOX
            index_2 = index_2 + 1
        elif contains_char(secret_word=secret, char_guess=guess[index_2]) is True:
            emoji_string = emoji_string + YELLOW_BOX
            index_2 = index_2 + 1
        else:
            emoji_string = emoji_string + WHITE_BOX
            index_2 = index_2 + 1
    return emoji_string  # return emoji string to print later


if __name__ == "__main__":
    main(secret="codes")
