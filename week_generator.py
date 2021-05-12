# EX1
'''
days = week()
next(days) # 'Monday'
next(days) # 'Tuesday'
next(days) # 'Wednesday'
next(days) # 'Thursday'
next(days) # 'Friday'
next(days) # 'Saturday'
next(days) # 'Sunday'
next(days) # StopIteration

Remember - Generator functions returns a generator. Generator is an iterator.
'''


def week():
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for day in days_of_week:
        yield day
    # raise StopIteration


# days = week()
# print(next(days))
# print(next(days))
# print(next(days))
# print(next(days))
# print(next(days))
# print(next(days))
# print(next(days))
# print(next(days))
# print(list(days))


# EX2
'''
gen = yes_or_no()
next(gen) # 'yes'
next(gen) # 'no'
next(gen) # 'yes'
next(gen) # 'no'
'''


def yes_or_no():
    yes_no = ["yes", "no"]
    while True:
        for answer in yes_no:
            yield answer
    pass


# gen = yes_or_no()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))


# EX3
'''
kombucha_song = make_song(5, "kombucha")
next(kombucha_song) # '5 bottles of kombucha on the wall.'
next(kombucha_song) # '4 bottles of kombucha on the wall.'
next(kombucha_song) # '3 bottles of kombucha on the wall.'
next(kombucha_song) # '2 bottles of kombucha on the wall.'
next(kombucha_song) # 'Only 1 bottle of kombucha left!'
next(kombucha_song) # 'No more kombucha!'
next(kombucha_song) # StopIteration

default_song = make_song()
next(default_song) # '99 bottles of soda on the wall.'
'''


# My solution


def make_song(count=99, beverage="soda"):
    while True:
        if count > 1:
            yield "{0} bottles of {1} on the wall.".format(count, beverage)
            count -= 1
        elif count == 1:
            yield "Only 1 bottle of {} left!".format(beverage)
            count -= 1
        elif count == 0:
            yield "No more {}!".format(beverage)
            count -= 1
        else:
            raise StopIteration


# kombucha_song = make_song(5, "kombucha")
# print(next(kombucha_song))
# print(next(kombucha_song))


# solution from Udemy
# def make_song(verses=99, beverage="soda"):
#     for num in range(verses, -1, -1):
#         if num > 1:
#             yield "{} bottles of {} on the wall.".format(num, beverage)
#         elif num == 1:
#             yield "Only 1 bottle of {} left!".format(beverage)
#         else:
#             yield "No more {}!".format(beverage)


# EX4

'''
evens = get_multiples(2, 3)
next(evens) # 2
next(evens) # 4
next(evens) # 6
next(evens) # StopIteration

default_multiples = get_multiples()
list(default_multiples) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''

# My solution

def get_multiples(number=1, count=10):
    for i in range(1, count+1):
        yield number*i

# print(list(get_multiples()))
# evens = get_multiples()
# print(next(evens))

# solution from Udemy

def get_multiples(num=1, count=10):
    next_num = num
    while count > 0:
        yield next_num
        count -= 1
        next_num += num


# EX5
'''
sevens = get_unlimited_multiples(7)
[next(sevens) for i in range(15)] 
# [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105]

ones = get_unlimited_multiples()
[next(ones) for i in range(20)]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
'''

def get_unlimited_multiples(num=1):
    next_num = num
    while True:
        yield next_num
        next_num += num


# ones = get_unlimited_multiples(6)
# print([next(ones) for i in range(20)])
