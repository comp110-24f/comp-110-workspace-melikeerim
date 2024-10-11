"""Basic syntax of lists"""

my_numbers: list[float] = list()  # constructor
my_numbers: list[float] = []  # literal

print(my_numbers)

my_numbers.append(1.5)

print(my_numbers)

# creating an already populated list
game_points: list[int] = [102, 86, 94]

# subscription notation/ indexing
print(game_points[2])  # indexing with lists works the same way

game_points[1] = (
    72  # we can do this modification because lists are mutable(str are not)
)
print(game_points[1])

# getting the length
print(len(game_points))

game_points.pop(1)
print(game_points)
print(game_points[10])


# write a function called display
# Input: list[int]
# Return Value: None
# print every value
# Try calling it on game_points
def display(input: list[int]) -> None:
    index: int = 0
    while index < len(input):
        print(input[index])
        index += 1


display(input=game_points)
