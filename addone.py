import sys
import ast
import argparse

parser = argparse.ArgumentParser(
    description="""addone takes a number as an array with an element for each digit.
                    It adds one to the number, using recursion if necessary,
                    and returns the result as a similar array.
                    Any leading zeroes will be removed."""
)
parser.add_argument('array', help="An array of ints. It must not have spaces")
args = parser.parse_args()


def addone(arg):
    """
    addone function takes a number as an array with an element for each digit.
    It adds one to the number and returns the result as a similar array.
    Any leading zeroes will be removed.

    :param arg: array
    :return: array
    """
    for s in arg[:]:
        if s == 0:  # Remove any leading zeroes
            arg.remove(s)
    if arg[len(arg) - 1] != 9:
        arg[len(arg) - 1] += 1  # Add one to the last element.
    else:  # If the last number is nine then the second last
        # element must also be changed.
        if len(arg) > 1:  # If the number has more than one digit then
            arg.pop(len(arg) - 1)  # the last element is set to zero and one
            addone(arg)  # is added to the previous element.
            arg.append(0)
        else:  # This is for cases where all the digits are nines.
            arg.pop(0)
            arg.insert(0, 0)  # There will be one more digit in the returned array.
            arg.insert(0, 1)  # A one must be placed in front of all the zeroes.

    return arg


array = ast.literal_eval(sys.argv[1])  # Creates an array from the argument
print(addone(array))
