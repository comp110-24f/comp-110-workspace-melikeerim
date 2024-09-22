"""Practice with Conditionals, Local Variables, and User Input"""

__author__: str = "730756528"


def guess_a_number() -> None:
    """guess a number conditional"""
    secret: int = 7  # local variable secret
    guess = int(input("Guess a number:"))  # local variable guess
    print("Your guess was " + str(guess))
    if guess == secret:
        print("You got it!")
    elif guess < secret:  # elif statement: used instead of additional if
        print(
            "Your guess was too low! The secret number is " + str(secret)
        )  # printing feedback
    else:
        print(
            "Your guess was too high! The secret number is " + str(secret)
        )  # printing feedback


# calling the function
if __name__ == "__main__":
    guess_a_number()
