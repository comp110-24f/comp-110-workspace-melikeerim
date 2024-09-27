"""Practice Importing: Coordinates"""

__author__ = "730756528"


def get_coords(xs: str, ys: str) -> None:
    """Defining get_coords function"""
    index_xs: int = 0
    while index_xs < len(xs):  # first while loop for xs
        index_ys: int = 0
        while index_ys < len(ys):  # nested while loop for ys
            print("(" + xs[index_xs] + "," + ys[index_ys] + ")")
            index_ys = index_ys + 1
        index_xs = index_xs + 1
    exit()
