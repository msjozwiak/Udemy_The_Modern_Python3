# EX1 Reverse string
'''
reverse_string('awesome') # 'emosewa'
reverse_string('Colt') # 'tloC'
reverse_string('Elie') # 'eilE'
'''


# add whatever parameters you deem necessary - good luck!


def reverse_string(word_to_reverse):
    new_string = word_to_reverse[::-1]
    return type(new_string)


# def reverse_string(str):
#     s = ''
#     for i, char in enumerate(str[::-1]):
#         s += char
#     return s

# print(reverse_string('Elie'))


# EX2 List Check

'''
list_check([[],[1],[2,3], (1,2)]) # False
list_check([1, True, [],[1],[2,3]]) # False
list_check([[],[1],[2,3]]) # True
'''


# def list_check(list_to_check):
#     check_list = []
#     for element in list_to_check:
#         el = isinstance(element, list)
#         check_list.append(el)
#     if False in check_list:
#         return False
#     return True


def list_check(list_to_check):
    for element in list_to_check:
        if type(element) != list:
            return False
    return True


# EX 3 remove_every_other
'''
remove_every_other([1,2,3,4,5]) # [1,3,5] 
remove_every_other([5,1,2,4,1]) # [5,2,1]
remove_every_other([1]) # [1] 
'''


def remove_every_other(first_list):
    second_list = [num for i, num in enumerate(first_list) if i % 2 == 0]
    return second_list


# print(remove_every_other([1]))


# EX4 Sum Pairs
'''
sum_pairs([4,2,10,5,1], 6) # [4,2]
sum_pairs([11,20,4,2,1,5], 100) # []
'''


def sum_pairs(list_for_check, sum):
    n = len(list_for_check)
    for i in range(0, n):
        for j in range(i + 1, n):
            if list_for_check[i] + list_for_check[j] == sum:
                return [list_for_check[i], list_for_check[j]]
    return []

    # for num in list_for_check:
    #     for i in range(0, len(list_for_check)-1):
    #         if num + list_for_check[i] == num_to_check:
    #             new_list.append(num)
    #             new_list.append(list_for_check)
    # return new_list

    # list_after_sum_pairs =
    # for i, num in enumerate(list_for_check):
    #     if num + list_for_check[i+1] == num_to_check:
    #         return [num, list_for_check[i+1]]
    # pass


# print(sum_pairs([11,20,4,2,1,5], 100))


# EX5 vowel_count
'''
vowel_count('awesome') # {'a': 1, 'e': 2, 'o': 1}
vowel_count('Elie') # {'e': 2, 'i': 1}
vowel_count('Colt') # {'o': 1}
'''


def vowel_count(word):
    splited_word = [char for char in word.lower()]
    new_dict = {}
    for char in splited_word:
        if char in ["a", "ą", "e", "ę", "i", "o", "u", "y"]:
            num = splited_word.count(char)
            new_dict.update({char: num})
    return new_dict


# print(vowel_count('awesome'))


# EX6

'''
titleize('this is awesome') # "This Is Awesome"
titleize('oNLy cAPITALIZe fIRSt') # "ONLy CAPITALIZe FIRSt"
'''


def titleize(string_of_words):
    list_of_words = string_of_words.split()
    list_of_word_with_upper_case = [word[0].upper() + word[1:] for word in list_of_words]
    separator = ' '
    return separator.join(list_of_word_with_upper_case)


# print(titleize("oNLy cAPITALIZe fIRSt"))


# EX7
'''
find_factors(10) # [1,2,5,10 ]
find_factors(11) # [1,11]
find_factors(111) # [1,3,37,111 ]
find_factors(321421) # [1,293,1097,321421 ]
find_factors(412146) # [1,2,3,6,7,9,14,18,21,42,63,126,3271,6542,9813,19626,22897,29439,45794,58878,68691,137382,206073,412146]
'''


def find_factors(number):
    list_of_factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            list_of_factors.append(i)
    return list_of_factors


# print(find_factors(321421))

# EX8
'''
includes([1, 2, 3], 1) # True 
includes([1, 2, 3], 1, 2) # False 
includes({ 'a': 1, 'b': 2 }, 1) # True 
includes({ 'a': 1, 'b': 2 }, 'a') # False
includes('abcd', 'b') # True
includes('abcd', 'e') # False
'''


def includes(collection, value, starting_index=0):
    if type(collection) in [list, str]:
        if value in collection[starting_index:]:
            return True
        return False
    if value in list(collection.values()):
        return True
    return False


# EX9 repeat

'''
repeat('*', 3) # '***' 
repeat('abc', 2) # 'abcabc' 
repeat('abc', 0) # ''
'''


def repeat(some_string, repeat_number):
    return some_string * repeat_number
    pass


# print(repeat("*", 3))


# EX10
'''
truncate("Super cool", 2) # "Truncation must be at least 3 characters."
truncate("Super cool", 1) # "Truncation must be at least 3 characters."
truncate("Super cool", 0) # "Truncation must be at least 3 characters."
truncate("Hello World", 6) # "Hel..."
truncate("Problem solving is the best!", 10) # "Problem..."
truncate("Another test", 12) # "Another t..."
truncate("Woah", 4) # "W..."
truncate("Woah", 3) # "..."
truncate("Yo",100) # "Yo"
truncate("Holy guacamole!", 152) # "Holy guacamole!"
'''


def truncate(some_string, number):
    if number < 3:
        return "Truncation must be at least 3 characters."
    if number > len(some_string):
        return some_string
    end = "..."
    index = number - 3
    new_string = some_string[:index] + end
    return new_string


# print(truncate("Hello World", 6))
# print(truncate("Super cool", 2))
# print(truncate("Super cool", 1))
# print(truncate("Super cool", 0))
# print(truncate("Problem solving is the best!", 10))
# print(truncate("Another test", 12))
# print(truncate("Woah", 4))
# print(truncate("Yo", 5))


# EX11

'''
two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]) # {'a': 1, 'b': 2, 'c': 3, 'd': None}
two_list_dictionary(['a', 'b', 'c']  , [1, 2, 3, 4]) # {'a': 1, 'b': 2, 'c': 3}
two_list_dictionary(['x', 'y', 'z']  , [1,2]) # {'x': 1, 'y': 2, 'z': None}
'''


# def two_list_dictionary(keys, values):
#     res = {}
#     i = -1
#     for key in keys:
#         for value in values:
#             res[key] = value
#             values.remove(value)
#             break
#         i += 1
#     if len(values) == 0:
#         list_without_values = keys[i:]
#         for key in list_without_values:
#             res.update({key: None})
#     return res

def two_list_dictionary(keys, values):
    res = {}
    for i in range(len(keys)):
        if i < len(values):
            res[keys[i]] = values[i]
        else:
            res[keys[i]] = None
    return res


# print(two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]))
# print(two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4]))
# print(two_list_dictionary(['x', 'y', 'z'] , [1,2]))


# EX12
'''
range_in_list([1,2,3,4],0,2) #  6
range_in_list([1,2,3,4],0,3) # 10
range_in_list([1,2,3,4],1) #  9
range_in_list([1,2,3,4]) # 10
range_in_list([1,2,3,4],0,100) # 10
range_in_list([],0,1) # 0
'''


def range_in_list(lst, start=0, end=None):
    end = end or lst[-1]
    return sum(lst[start:end + 1])


# print(range_in_list([1,2,3,4],0,2))
# print(range_in_list([1,2,3,4],0,3))
# print(range_in_list([1,2,3,4],1))
# print(range_in_list([1,2,3,4]))
# print(range_in_list([1,2,3,4],0,100))
# print(range_in_list([],0,1))


# EX13

'''
same_frequency(551122,221515) # True
same_frequency(321142,3212215) # False
same_frequency(1212, 2211) # True
'''


def same_frequency(first_number, second_number):
    first_list = list(str(first_number))
    first_list.sort(key=int)
    second_list = list(str(second_number))
    second_list.sort(key=int)
    first_dictionary = {num: first_list.count(num) for num in first_list}
    second_dictionary = {num: second_list.count(num) for num in second_list}
    if first_dictionary == second_dictionary:
        return True
    return False


# print(same_frequency(551122, 221515))
# print(same_frequency(321142, 3212215))
# print(same_frequency(1212, 2211))

# EX14


'''
nth(['a', 'b', 'c', 'd'], 1)  # 'b' 
nth(['a', 'b', 'c', 'd'], -2) #  'c'
nth(['a', 'b', 'c', 'd'], 0)  # 'a'
nth(['a', 'b', 'c', 'd'], -4) #  'a'
nth(['a', 'b', 'c', 'd'], -1) #  'd'
nth(['a', 'b', 'c', 'd'], 3)  # 'd'
'''


def nth(list, number):
    return list[number]


# print(nth(['a', 'b', 'c', 'd'], 1))
# print(nth(['a', 'b', 'c', 'd'], -2))
# print(nth(['a', 'b', 'c', 'd'], 0))
# print(nth(['a', 'b', 'c', 'd'], -4))
# print(nth(['a', 'b', 'c', 'd'], -1))
# print(nth(['a', 'b', 'c', 'd'], 3))


# EX15

'''
find_the_duplicate([1,2,1,4,3,12]) # 1
find_the_duplicate([6,1,9,5,3,4,9]) # 9
find_the_duplicate([2,1,3,4]) # None
'''


def find_the_duplicate(list):
    for num in list:
        num_of_occurrences = list.count(num)
        if num_of_occurrences == 2:
            return num
    return None


# print(find_the_duplicate([1,2,1,4,3,12]))
# print(find_the_duplicate([6,1,9,5,3,4,9]))
# print(find_the_duplicate([2,1,3,4]))


# EX16

'''
EXAMPLES:


list1 = [
  [ 1, 2 ],
  [ 3, 4 ]
]

sum_up_diagonals(list1) # 10

list2 = [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
]

sum_up_diagonals(list2) # 30

list3 = [
  [ 4, 1, 0 ],
  [ -1, -1, 0],
  [ 0, 0, 9]
]

sum_up_diagonals(list3) # 11

list4 = [
  [ 1, 2, 3, 4 ],
  [ 5, 6, 7, 8 ],
  [ 9, 10, 11, 12 ],
  [ 13, 14, 15, 16 ]
]

sum_up_diagonals(list4) # 68
'''


def sum_up_diagonals(list_of_lists):
    first_diagonal = 0
    second_diagonal = 0
    i = len(list_of_lists)
    x = 0
    while i >= 1:
        first_diagonal += list_of_lists[i - 1][i - 1]
        second_diagonal += list_of_lists[i - 1][x]
        i -= 1
        x += 1
    return sum([first_diagonal, second_diagonal])


# def sum_up_diagonals(arr):
#     total = 0
#
#     for i, val in enumerate(arr):
#         total += arr[i][i]
#         total += arr[i][-1 - i]
#     return total

# print(sum_up_diagonals([
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]))


# EX17

'''
min_max_key_in_dictionary({2:'a', 7:'b', 1:'c',10:'d',4:'e'}) # [1,10]
min_max_key_in_dictionary({1: "Elie", 4:"Matt", 2: "Tim"}) # [1,4]
'''


def min_max_key_in_dictionary(dictionary_to_check):
    sorted_list_of_values = sorted(dictionary_to_check)
    return [sorted_list_of_values[0], sorted_list_of_values[len(sorted_list_of_values) - 1]]


# print(min_max_key_in_dictionary({2:'a', 7:'b', 1:'c',10:'d',4:'e'}))


# EX18

'''
find_greater_numbers([1,2,3]) # 3 
find_greater_numbers([6,1,2,7]) # 4
find_greater_numbers([5,4,3,2,1]) # 0
find_greater_numbers([]) # 0
'''


def find_greater_numbers(arr):
    count = 0
    i = 0
    j = 1
    while i < len(arr):
        while j < len(arr):
            if arr[j] > arr[i]:
                count += 1
            j += 1
        j = i + 1
        i += 1
    return count


# print(find_greater_numbers([1,2,3]))


# EX19

'''
two_oldest_ages( [1, 2, 10, 8] ) # [8, 10]
two_oldest_ages( [6,1,9,10,4] ) # [9,10]
two_oldest_ages( [4,25,3,20,19,5] ) # [20,25]
'''


def two_oldest_ages(ages):
    return sorted(ages)[-2:]


# print(two_oldest_ages([1, 2, 10, 8]))


# EX 20

'''
is_odd_string('a') # True
is_odd_string('aaaa') # False
is_odd_string('amazing') # True
is_odd_string('veryfun') # True
is_odd_string('veryfunny') # False
'''


# def is_odd_string(string):
#     total = sum((ord(c) - 96) for c in string.lower()) or 0
#     return total % 2 == 1


def is_odd_string(string):
    total = 0
    for letter in string.lower():
        total += ord(letter) - 96
    if total % 2 != 0:
        return True
    return False


# print(is_odd_string('a'))
# print(is_odd_string('aaaa'))
# print(is_odd_string('amazing'))
# print(is_odd_string('veryfun'))
# print(is_odd_string('aaaa'))
