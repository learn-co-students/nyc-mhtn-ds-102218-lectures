# module level scope

def area(length, width):
    # functional scope
    _area = length*width
    # trapped inside of the function
    return _area # catapults the argument over thewalls

def volume(length = 1, width = 1, height = 1, something = 0):
    volume = area(length, width)*height
    return volume + something

# module level scope
my_list = [1, 2, 3]
