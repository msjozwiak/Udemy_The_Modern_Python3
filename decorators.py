# EX1
'''
@show_args
def do_nothing(*args, **kwargs):
    pass

do_nothing(1, 2, 3,a="hi",b="bye")

# Should print (on two lines):
# Here are the args: (1, 2, 3)
# Here are the kwargs: {"a": "hi", "b": "bye"}
'''

from functools import wraps


def show_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Here are the args:", args)
        print("Here are the kwargs:", kwargs)
        return func(*args, **kwargs)

    return wrapper


@show_args
def do_nothing(*args, **kwargs):
    pass


# do_nothing(1, 2, 3, a="hi", b="bye")


# EX2
'''
@double_return 
def add(x, y):
    return x + y

add(1, 2) # [3, 3]

@double_return
def greet(name):
    return "Hi, I'm " + name

greet("Colt") # ["Hi, I'm Colt", "Hi, I'm Colt"]
'''


def double_return(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return [result for i in range(2)]

    return wrapper


@double_return
def add(x, y):
    return x + y


@double_return
def greet(name):
    return "Hi, I'm " + name


# print(add(1, 2))
# print(greet("Colt"))


# EX3
'''
@ensure_fewer_than_three_args
def add_all(*nums):
    return sum(nums)

add_all() # 0
add_all(1) # 1
add_all(1,2) # 3
add_all(1,2,3) # "Too many arguments!"
add_all(1,2,3,4,5,6) # "Too many arguments!"
'''


def ensure_fewer_than_three_args(my_fn):
    @wraps(my_fn)
    def wrapper(*args, **kwargs):
        if len(args) < 3:
            return my_fn(*args, **kwargs)
        else:
            return "Too many arguments!"

    return wrapper


@ensure_fewer_than_three_args
def add_all(*nums):
    return sum(nums)


# print(add_all(1))


# EX4

'''
@only_ints 
def add(x, y):
    return x + y

add(1, 2) # 3
add("1", "2") # "Please only invoke with integers."
'''


def only_ints(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        for i in args:
            if type(i) != int:
                return "Please only invoke with integers."
        else:
            return f(*args, **kwargs)

    return wrapper


@only_ints
def add(x, y):
    return x + y


# print(add(2, '2'))


# EX5
'''
@ensure_authorized
def show_secrets(*args, **kwargs):
    return "Shh! Don't tell anybody!"

show_secrets(role="nobody") # "Unauthorized"
show_secrets(a="b") # "Unauthorized"
show_secrets(role="admin") # "Shh! Don't tell anybody!"
'''


def ensure_authorized(f_n):
    @wraps(f_n)
    def wrapper(*args, **kwargs):
        for key, value in kwargs.items():
            if key == "role" and value == "admin":
                return f_n(*args, **kwargs)
        else:
            return "Unauthorized"

    return wrapper


@ensure_authorized
def show_secrets(*args, **kwargs):
    return "Shh! Don't tell anybody!"


# print(show_secrets(role="nobody"))
# print(show_secrets(a="b"))
# print(show_secrets(role="admin"))

# EX6
def enforce(*types):
    def decorator(f):
        def new_func(*args, **kwargs):
            # convert args into something mutable
            newargs = []
            for (a, t) in zip(args, types):
                newargs.append(t(a))  # feel free to have more elaborated convertion
            return f(*newargs, **kwargs)

        return new_func

    return decorator


@enforce(str, int)
def repeat_msg(msg, times):
    for time in range(times):
        print(msg)


@enforce(float, float)
def divide(a, b):
    print(a / b)


# repeat_msg("hello", '5')
# divide('1', '4')


# EX7

'''
@delay(3)
def say_hi():
    return "hi"

say_hi()
# should print the message "Waiting 3s before running say_hi" to the console
# should then wait 3 seconds
# finally, should invoke say_hi and return "hi"
'''

from time import sleep


def delay(time):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            print("Waiting {}s before running say_hi".format(time))
            sleep(time)
            return fn(*args, **kwargs)

        return wrapper

    return inner


@delay(3)
def say_hi():
    return "hi"


# print(say_hi())








