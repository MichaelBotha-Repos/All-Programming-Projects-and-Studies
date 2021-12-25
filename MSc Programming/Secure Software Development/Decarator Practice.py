def f1_decorator(func):
    def inner(a, b):
        func(a, b)
        print("bells and whistles")
    return inner


@f1_decorator
def f1(a, b):
    print("main function" + a + b)

f1(" smells", " good")
