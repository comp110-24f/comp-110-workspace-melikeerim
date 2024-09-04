"""Ex01 Planning a tea party: find the amount of tea bags/treats, and cost!"""

__author__: str = "730756528"


# conventional to write “main” functions as the first function definition in a program
# reading newspaper/main_planner calls all other functions&produces output
def main_planner(guests: int) -> None:
    """Bringing everything together: calls each function and produces output"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


# Assume everyone will drink two cups of tea
def tea_bags(people: int) -> int:
    """find the tea bags needed: people*2"""
    return 2 * people


# Assume everyone wants 1.5 treats to accompany a tea!Convert data to int b4 returning!
def treats(people: int) -> int:
    """calculate treats needed: 1.5 treat per tea! convert to int!"""
    return int(1.5 * tea_bags(people=people))


# Return type float!
def cost(tea_count: int, treat_count: int) -> float:
    """finding the total cost!teabags=0.50 and treats=0.75"""
    return tea_count * 0.50 + treat_count * 0.75


# at the end of the program
if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
