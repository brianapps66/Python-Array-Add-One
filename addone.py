array = [0, 0, 0, 0, 0, 0, 0, 9, 9, 9, 9, 9, 9, 7]


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


print(array)
print(addone(array))
