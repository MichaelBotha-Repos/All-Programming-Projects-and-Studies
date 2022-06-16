# Normal function invocation:
def without_arg():
    print('Hello')

def with_arg(arg1, arg2=2, arg3=3):
    print(f'{arg1}:{arg2}:{arg3}')

def new(*args, **kwargs):
    for elem in args:
        print(elem)
    for key in kwargs:
        print(f"{key}->{kwargs[key]}")

without_arg()
with_arg(5, arg3=7)
new(6,7,8,9,blob=10,add='h')
