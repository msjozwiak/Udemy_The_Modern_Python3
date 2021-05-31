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


print_users()
