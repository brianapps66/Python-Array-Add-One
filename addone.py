import sys
import ast
import argparse

parser = argparse.ArgumentParser(
    description = """addone function takes a number as an array with an element for each digit.
    It adds one to the number and returns the result as a similar array.
    Any leading zeroes will be removed."""
)
parser.add_argument('array', help = "An array of ints. It must not have spaces")
args=parser.parse_args()

def addone(arg):
    """
    addone function takes a number as an array with an element for each digit.
    It adds one to the number and returns the result as a similar array.
    Any leading zeroes will be removed.

    :param arg: array
    :return: array
    """
    for s in arg[:]:
        if s == 0:
            arg.remove(s)
    if arg[len(arg) - 1] != 9:
        arg[len(arg) - 1] += 1
    else:
        if len(arg) > 1:
            arg.pop(len(arg) - 1)
            addone(arg)
            arg.append(0)
        else:
            arg.pop(0)
            arg.insert(0, 0)
            arg.insert(0, 1)

    return arg

array = ast.literal_eval(sys.argv[1])
print(addone(array))
