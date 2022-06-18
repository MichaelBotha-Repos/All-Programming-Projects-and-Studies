def without_arg():
    print('Hello')

def with_arg(arg1=7, arg2=2, arg3=3):
    print(f'{arg1}:{arg2}:{arg3}')

def new(*args, **kwargs):
    for elem in args:
        print(elem)
    for key in kwargs:
        print(f"{key}->{kwargs[key]}")
    new2(*args, **kwargs)

def new2(*args,**kwargs):
    print(args, kwargs)


without_arg()
with_arg(arg3=7)
new(6,7,8,9,blob=10,add='h')
new(1,2,3,4, breakfast="cereal", lunch="chops", supper="salad")


