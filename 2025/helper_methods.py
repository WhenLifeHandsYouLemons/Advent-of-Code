import math

def gridPrint(grid: list[list], newline: bool = True, join_row: bool = True, spacing: str = " ", join_all: bool = False) -> None:
    """Prints the given grid in a cleaner way to the running console.

    Args:
        grid (list): The grid to print out.
        newline (bool, optional): Whether a new line should be printed before the entire grid. Defaults to True.
        join_row (bool, optional): Whether each row should be printed as a list or joined together into a string. The rows are still printed separately. Defaults to True.
        spacing (str, optional): The character between each column item of the array that's printed. This is ignored if join_row is False. Defaults to " ".
        join_all (bool, optional): Whether the entire grid should be printed as a single string. This ignores the value of join_row, if given. Defaults to False.
    """
    if newline:
        print()

    if join_all:
        print_str = ""
        for i in grid:
            k = [str(j) for j in i]
            print_str = f"{print_str}{''.join(k)}"

        print(print_str)
    else:
        for i in grid:
            if join_row:
                k = [str(j) for j in i]
                print(spacing.join(k))
            else:
                print(i)

def arrayPrint(ar: list, newline: bool = True, separate: bool = False, spacing: str = " ") -> None:
    """Prints the given array in a cleaner way to the running console.

    Args:
        ar (list): The list to print out.
        newline (bool, optional): Whether a new line should be printed before the entire array. Defaults to True.
        separate (bool, optional): Whether each item should be printed on a separate line or all on the same line. Defaults to False.
        spacing (str, optional): The character between each item of the array that's printed. This is ignored if separate is True. Defaults to " ".
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
