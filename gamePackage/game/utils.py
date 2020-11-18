import random
def print_bold(msg, end='\n'):
    print("\033[1m" + msg + "\033[0m", end=end)

def print_dotted_line(width=72):
    print('-'*width)

def weighted_random_selection(obj1, obj2):
    weighted_list = 3 * [id(obj1)] + 6 * [id(obj2)] + 1 * [None]
    selection = random.choice(weighted_list)

    if selection == id(obj1):
        return obj1

    return obj2