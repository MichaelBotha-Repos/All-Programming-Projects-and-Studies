
from turtle import clear


try:

    user_input = int(input())
    x = 10/user_input

except BaseException as e:
    for att in e.args:
        print(att)
else:
    print(x)
finally:
    print("finished")
