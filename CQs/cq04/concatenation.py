"""Practice Importing: Concatenation"""

__author__ = "730756528"


def concat(str_1: str, str_2: str) -> str:
    """Defining the concat function"""
    return str_1 + str_2  # returns the concatenation of the two strings


word1: str = "happy"  # global variables
word2: str = "tuesday"


def main() -> None:
    """Main function"""
    print(concat(word1, word2))


if (
    __name__ == "__main__"
):  # the function call still occurs when run this file but not when import
    main()
