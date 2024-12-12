import math

def gridPrint(grid: list, join: bool = False) -> None:
    """Prints the given grid in a cleaner way to the running console.

    Args:
        grid (list): The grid to print out.
        join (bool, optional): Whether each line should be printed as a list or joined together into a string. Defaults to False.
    """
    print()
    for i in grid:
        if join:
            print("".join(i))
        else:
            print(i)

def arrayPrint(ar: list, newline: bool = False, separate: bool = False, spacing: str = "") -> None:
    """Prints the given array in a cleaner way to the running console.

    Args:
        ar (list): The list to print out.
        newline (bool, optional): Whether a new line should be printed before the entire array. Defaults to False.
        separate (bool, optional): Whether each item should be printed on a separate line or all on the same line. Defaults to False.
        spacing (str, optional): The character between each item of the array that's printed. This is ignored if separate is True. Defaults to "".
    """
    if newline:
        print()

    if separate:
        for i in ar:
            print(i)
    else:
        print(spacing.join([str(i) for i in ar]))

def readfile(file_path: str) -> list[str]:
    """Reads the contents of the given file.

    Args:
        file_path (str): The file path that the file is stored at.

    Returns:
        list: The list of lines read from the file.
    """
    all_lines = []

    with open(file_path, "r") as f:
        content = f.read()
        lines = content.splitlines()
        for line in lines:
            all_lines.append(line)

    return all_lines
