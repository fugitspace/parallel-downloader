import functools

def get_function():
    print("Inside get_function")
    def returned_function():
        print("Inside returned_function")
        return 1
    print("Outside returned_function")
    return returned_function

#returned_function() # doesn't work, undefined
x = get_function() # prints inside and outside and assigns returned_function to x
x # prints nothing
x() # prints inside

def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we build the nation"

def greet_bob(greeter_func):
    return greeter_func("Bob")

def parent(num):
    def first_child():
        return "I am first born"

    def second_child():
        return "I am second born"
    
    if num == 1:
        return first_child
    return second_child

def my_decorator(func):
    def wrapper():
        print("Something happening before the function is called")
        func()
        print("Something happening after the function is called")
    return wrapper

# @my_decorator
def say_whee():
    print("Wheeeeeel")

# with args
def hello(name):
    print("Hello {0}".format(name))

def greet_twice(func):
    @functools.wrap(func)
    def wrapper_hello(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper_hello

hello = greet_twice(hello)

hello("Sovello")

list(map(lambda x: (x, (float(9)/5)*x + 32), temp), map(lambda x: (x, x+273), temp))