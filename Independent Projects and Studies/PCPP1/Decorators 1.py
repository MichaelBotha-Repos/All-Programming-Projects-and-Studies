def decorator(func):
    print("in decorator")
    return func

@decorator
def base():
    print("in base")


base()
        
