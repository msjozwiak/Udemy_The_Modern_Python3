# EX1

# import keyword
#
#
# def contains_keyword(*args):
#     for arg in args:
#         if keyword.iskeyword(arg):
#             return True
#     return False
#
#
# print(contains_keyword("d", "g"))

# EX2
from pyfiglet import figlet_format
from termcolor import colored

def print_art(msg, color):
    valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")
    if color not in valid_colors:
        color = "magenta"
    ascii_art = figlet_format(msg)
    ascii_colored = colored(ascii_art, color)
    print(ascii_colored)


msg = input("What would you like to print? ")
color = input("What color? ")
print_art(msg, color)
