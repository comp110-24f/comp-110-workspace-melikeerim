from CQs.cq04.concatenation import concat  # importing concat
from CQs.cq04.coordinates import get_coords

"""Practice Importing: Visualize"""

__author__ = "730756528"

x: str = "123"  # global variables
y: str = "abc"

print(concat(x, y))  # calling and printing concat
print(get_coords(xs=x, ys=y))  # calling and printing get_coords
