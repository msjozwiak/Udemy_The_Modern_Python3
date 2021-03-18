# ex1

def return_day(num):
    days_of_the_week = {1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 5: "Thursday", 6: "Friday",
                        7: "Saturday"}
    if num < 1 or num > 7:
        return None
    return days_of_the_week[num]


def return_day(num):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    # Check to see if num valid
    if num > 0 and num <= len(days):
        # use num - 1 because lists start at 0
        return days[num - 1]
    return None


# ex3

def last_element(list_things):
    if len(list_things) > 0:
        return list_things[-1]
    else:
        return None


def last_element(l):
    if l:
        return l[-1]
    return None


# ex4

def single_letter_count(word, letter):
    word = word.upper()
    letter = letter.upper()
    print(word.count(letter))
    return word.count(letter)


def single_letter_count(string, letter):
    return string.lower().count(letter.lower())


# ex5

def multiple_letter_count(word):
    print({char: word.count(char) for char in word})
    return {char: word.count(char) for char in word}


# ex6
'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''


def list_manipulation(some_list, command, location, value=None):
    if command == "remove" and location == "end":
        print(some_list.pop())
        return some_list.pop()
    elif command == "remove" and location == "beginning":
        print(some_list.pop(0))
        return some_list.pop(0)
    elif command == "add" and location == "beginning":
        print(some_list.insert(0, value))
        return some_list.insert(0, value)
    elif command == "add" and location == "end":
        print(some_list.append(value))
        return some_list.append(value)
    pass


# list_manipulation([1, 2, 3], "remove", "end")
# list_manipulation([1, 2, 3], "remove", "beginning")
# list_manipulation([1, 2, 3], "add", "beginning", 20)


# ex7

'''
is_palindrome('testing') # False
is_palindrome('tacocat') # True
is_palindrome('hannah') # True
is_palindrome('robert') # False
is_palindrome('amanaplanacanalpanama') # True
'''


def is_palindrome(word):
    word_reversed = word[::-1]
    if word == word_reversed:
        return True
    return False


def is_palindrome(string):
    return string == string[::-1]


# is_palindrome('testing')
# is_palindrome('tacocat')
# is_palindrome('hannah')
# is_palindrome('robert')
# is_palindrome('amanaplanacanalpanama')


# ex8


def multiply_even_numbers(num_list):
    even_num_list = [num for num in num_list if num % 2 == 0]
    value = 1
    for num in even_num_list:
        value *= num
    return value
    pass


def multiply_even_numbers(lst):
    total = 1
    for val in lst:
        if val % 2 == 0:
            total = total * val
    return total


# multiply_even_numbers([2, 3, 4, 5, 6])


# ex 9


'''
capitalize("tim") # "Tim"
capitalize("matt") # "Matt"
'''


def capitalize(word):
    upper_word = word[0].upper() + word[1:]
    print(upper_word)
    return upper_word
    pass


# capitalize("tim")


# ex10


'''
frequency([1,2,3,4,4,4], 4) # 3
frequency([True, False, True, True], False) # 1
'''


def frequency(num_list, search_term):
    return num_list.count(search_term)
    pass


# frequency([1, 2, 3, 4, 4, 4], 4)


#  ex 11



'''
compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]
'''


def compact(check_list):
    print([value for value in check_list if value])
    return [value for value in check_list if value]
    pass


# compact([0, 1, 2, "", [], False, {}, None, "All done"])


# ex12


# flesh out intersection pleaseeeee
def intersection(list_1, list_2):
    return list(set(list_1) & set(list_2))
    pass


# intersection([1, 2, 3], [2, 3, 4])


# ex13


'''
def isEven(num):
    return num % 2 == 0

partition([1,2,3,4], isEven) # [[2,4],[1,3]]
'''


def is_even(num):
    return num % 2 == 0


def partition(list_1, function):
    truthy_list = [num for num in list_1 if function(num)]
    falsy_list = [num for num in list_1 if not function(num)]
    print([truthy_list, falsy_list])
    return [truthy_list, falsy_list]


# partition([1, 2, 3, 4], is_even)


#  ex14


def contains_purple(*args):
    if "purple" in args:
        return True
    return False


# print(contains_purple(25, "purple"))


# ex15



def combine_words(word, **kwargs):
    if "prefix" in kwargs:
        return kwargs["prefix"] + word
    elif "suffix" in kwargs:
        return word + kwargs["suffix"]
    return word


def combine_words(word, **kwargs):
    if 'prefix' in kwargs:
        return kwargs['prefix'] + word
    elif 'suffix' in kwargs:
        return word + kwargs['suffix']
    return word


# print(combine_words("work"))


# ex 16


def count_sevens(*args):
    return args.count(7)


nums = [90, 1, 35, 67, 89, 20, 3, 1, 2, 3, 4, 5, 6, 9, 34, 46, 57, 68, 79, 12, 23, 34, 55, 1, 90, 54, 34, 76, 8, 23, 34,
        45, 56, 67, 78, 12, 23, 34, 45, 56, 67, 768, 23, 4, 5, 6, 7, 8, 9, 12, 34, 14, 15, 16, 17, 11, 7, 11, 8, 4, 6,
        2, 5, 8, 7, 10, 12, 13, 14, 15, 7, 8, 7, 7, 345, 23, 34, 45, 56, 67, 1, 7, 3, 6, 7, 2, 3, 4, 5, 6, 7, 8, 9, 8,
        7, 6, 5, 4, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9, 8, 7, 8, 7, 6, 5, 4, 3, 2, 1, 7]
# NO TOUCHING! =================================================================

# Write your code below:

# result1 = count_sevens(1, 4, 7)
# print(result1)
# result2 = count_sevens(*nums)
# print(result2)


# ex17



# print(" e " + str(int(2/2)))
'''
calculate(make_float=False, operation='add', message='You just added', first=2, second=4) # "You just added 6"
calculate(make_float=True, operation='divide', first=3.5, second=5) # "The result is 0.7"
'''


def calculate(**kwargs):
    operation_lookup = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
    }
    is_float = kwargs.get('make_float', False)
    operation_value = operation_lookup[kwargs.get('operation', '')]
    if is_float:
        final = "{} {}".format(kwargs.get('message', 'The result is'), float(operation_value))
    else:
        final = "{} {}".format(kwargs.get('message', 'The result is'), int(operation_value))
    return final


# LAMBDA!
# ex1


# Write a lambda that accepts a single number and cubes it. Save it in a variable called cube.
cube = lambda number: number ** 3

# print(cube(3))


# ex2 LAMBDA + MAP()!


decrement_list = list(map(lambda num: num - 1, [1, 2, 3]))


# print(decrement_list)

def decrement_list(single_list):
    return list(map(lambda num: num - 1, single_list))


# print(decrement_list([1, 2, 3]))


# ex3 LAMBDA + FILTER()!
def remove_negatives(check_list):
    return list(filter(lambda n: n >= 0, check_list))


# ANY/ALL!


# Implement your is_all_strings function below:
def is_all_strings(l):
    return all([type(s) == str for s in l])


# MAX/MIN!


def extremes(nums):
    return min(nums), max(nums)


# print(extremes([1,2,3,4,5]))

# REVERSED()/REVERSE()!
l = [1, 2, 3, 4]


# print(list(reversed(l)))
# print(l.reverse())
# print(l)

# ABS()!


def max_magnitude(single_list):
    return max(map(lambda n: abs(n), single_list))


# print(max_magnitude([1, 2, -9]))


# SUM()!


# def sum_even_values(*args):
#     return sum(num for num in args if num % 2 == 0)
#     return sum(filter(lambda num: num % 2 == 0, args))


def sum_even_values_2(*args):
    return sum(num for num in args if num % 2 == 0)


# print(sum_even_values_2(2,3,10))


# SUM float()


def sum_floats(*args):
    # return sum(arg for arg in args if type(arg) == 'float')
    return sum(filter(lambda arg: type(arg) == float, args))


print(sum_floats(1.5, 2.4, 'awesome', [], 1))
