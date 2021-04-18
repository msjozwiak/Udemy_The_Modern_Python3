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
# from pyfiglet import figlet_format
# from termcolor import colored
#
# def print_art(msg, color):
#     valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")
#     if color not in valid_colors:
#         color = "magenta"
#     ascii_art = figlet_format(msg)
#     ascii_colored = colored(ascii_art, color)
#     print(ascii_colored)
#
#
# msg = input("What would you like to print? ")
# color = input("What color? ")
# print_art(msg, color)

# EX3
# print(__name__)

print("before import")
import math

print("before functionA")


def functionA():
    print("Function A")


print("before functionB")


def functionB():
    print("Function B {}".format(math.sqrt(100)))


print("before __name__ guard")
if __name__ == '__main__':
    functionA()
    functionB()
print("after __name__ guard")

print(math)
