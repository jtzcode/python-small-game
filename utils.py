def print_bold(msg, end='\n'):
    print("\033[1m" + msg + "\033[0m", end=end)

def print_dotted_line(width=72):
    print('-'*width)