"""
Below is what a decorator represents by using syntactic sugar:

def func():
    print("in func")

def decorator(func):
    print("decorator")
    return func

wrapped_func = decorator(func)
wrapped_func()

"""

"""
# Using the decorator syntactic sugar

def decorator(func):
    print("in decorator")
    return func

@decorator
def func():
    print("in function")

func()
"""

"""
# A decorator accessing function variables:

def decorator(func):
    print(f"decorator")
    def wrapper(*args, **kwargs):
        print(args, kwargs)
        func(*args, **kwargs)
    return wrapper

@decorator
def func(*args, **kwargs):
    print("in func")
    for elem in args:
        print(elem)

func(1,3,5, me="hell0")
"""

"""
# A decorator with its own variables

def decorator(decor_var):
    def wrap_func(func):
        def wrap_func_vars(**kwargs):
            print(f"decorator: {decor_var}\nfunction: {kwargs}")
            func(**kwargs)

        return wrap_func_vars
    return wrap_func


@decorator("hello")
def func(**kwargs):
    print("in func")

func(john = 10)

"""

class Decorator:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        print(f"in class {args}, {kwargs}")
        self.func(*args, **kwargs)
        print("in class")

@Decorator
def func(*args, **kwargs):
    print("in func")
    print(args)
    print(kwargs)

func(1,2,3, john=14, michael=2)