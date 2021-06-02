# EX1

'''
add_user("Dwayne", "Johnson") # None
# CSV now has two data rows:

# First Name,Last Name
# Colt,Steele
# Dwayne,Johnson
'''
from csv import writer, reader


def add_user(first_name, last_name):
    with open("users.csv", "a") as file:
        csv_writer = writer(file)
        csv_writer.writerow([first_name, last_name])


# add_user("Dwayne", "Johnson")


# EX2
'''
print_users() # None
# prints to the console:
# Colt Steele
'''


def print_users():
    with open("users.csv") as file:
        csv_reader = reader(file)
        next(csv_reader)
        for row in csv_reader:
            print("{0} {1}".format(row[0], row[1]))


# print_users()


# EX3
'''
find_user("Colt", "Steele") # 1
find_user("Alan", "Turing") # 3
find_user("Not", "Here") # 'Not Here not found.'
'''


# first_name, last_name


def find_user(first_name, last_name):
    with open("users1.csv") as file:
        csv_reader = list(reader(file))
        if [first_name, last_name] in csv_reader:
            return csv_reader.index([first_name, last_name])
        else:
            return "{0} {1} not found".format(first_name, last_name)


# print(find_user("Not", "Here"))


# EX4

'''
update_users("Grace", "Hopper", "Hello", "World") # Users updated: 1.
update_users("Colt", "Steele", "Boba", "Fett") # Users updated: 2.
update_users("Not", "Here", "Still not", "Here") # Users updated: 0.
'''


def update_users(old_first_name, old_last_name, new_first_name, new_last_name):
    with open("users2.csv") as file:
        csv_reader = list(reader(file))

    count = 0
    with open("users2.csv", "w") as file:
        csv_writer = writer(file)
        for row in csv_reader:
            if [old_first_name, old_last_name] == row:
                csv_writer.writerow([new_first_name, new_last_name])
            else:
                csv_writer.writerow(row)
    return "Users updated: {}.".format(count)


# update_users("Grace", "Hopper", "Hello", "World")


# EX5

'''
delete_users("Grace", "Hopper") # Users deleted: 1.
delete_users("Colt", "Steele") # Users deleted: 2.
delete_users("Not", "Here") # Users deleted: 0.
'''


def delete_users(first_name, last_name):
    with open("users3.csv") as file:
        csv_reader = list(reader(file))

    count = 0
    with open("users3.csv", "w") as file:
        csv_writer = writer(file)
        for row in csv_reader:
            if [first_name, last_name] == row:
                count += 1
            else:
                csv_writer.writerow(row)
    return "Users updated: {}.".format(count)


# delete_users("Grace", "Hopper")
