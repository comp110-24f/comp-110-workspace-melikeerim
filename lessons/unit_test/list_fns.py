def get_first(input: list[str]) -> str:
    """Return first element"""
    return input[0]


def remove_first(input_2: list[str]) -> None:
    """Remove first element."""
    input_2.pop(0)


def get_and_remove_first(input_3: list[str]) -> str:
    """Remove and return first element."""
    first_elem: str = input_3[0]
    input_3.pop(0)
    return first_elem
