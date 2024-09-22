"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730756528"


def main() -> None:
    """defining the main function"""
    contains_char(
        word=input_word(), letter=input_letter()
    )  # main function puts everything together bby calling other functions defined


def input_word() -> str:
    """defining the input_word function to ask for a 5-character word"""
    five_character_word: str = input("Enter a 5-character word:")
    if (
        len(five_character_word) == 5
    ):  # if the length of the input is equal to 5, then return the input
        return five_character_word
    else:
        print("Error: Word must contain 5 characters.")
        exit()  # Exit here if the word doesn't have 5 characters, no need to continue
        return five_character_word


def input_letter() -> str:
    """defining the input_letter function to ask for a single_character letter"""
    single_character: str = input("Enter a single character:")
    if len(single_character) == 1:
        return single_character
    else:
        print("Error: Character must be a single character.")
        exit()  # exit here if the input is not a single_character
        return single_character


def contains_char(word: str, letter: str) -> None:
    """defining the contains_char function"""
    # check each five indices of the word to see if it is equal to the letter
    print("Searching for " + letter + " in " + word)
    count: int = 0  # count variable to count mathcing characters
    if word[0] == letter:  # don't use loop in this exercise
        print(letter + " found at index 0")
        count = count + 1  # increase count by 1
    if word[1] == letter:
        print(letter + " found at index 1")
        count = count + 1
    if word[2] == letter:
        print(letter + " found at index 2")
        count = count + 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count = count + 1
    if word[4] == letter:
        print(letter + " found at index 4")
        count = count + 1
    if count == 0:  # in case there is no match
        print("No instances of " + letter + " found in " + word)
    elif count == 1:
        print("1 instance of " + letter + " found in " + word)
    else:  # there's more than one match
        print(str(count) + " instances of " + letter + " found in " + word)


if __name__ == "__main__":
    main()  # to import functions in this file + to run it as a module
