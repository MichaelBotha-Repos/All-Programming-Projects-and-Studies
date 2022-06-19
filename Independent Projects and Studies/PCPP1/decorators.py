"""
Scenario
Create a function decorator that prints a timestamp (in a form like year-month-day hour:minute:seconds, eg. 2019-11-05 08:33:22)
Create a few ordinary functions that do some simple tasks, like adding or multiplying two numbers.
Apply your decorator to those functions to ensure that the time of the function executions can be monitored.

Hint
To print the current time, you could use the following code:

# import module responsible for time processing
from datetime import datetime

# get current time using now() method
timestamp = datetime.now()

# convert timestamp to human-readable string, following passed pattern:
string_timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')

print(string_timestamp)

"""

from datetime import datetime
from random import randrange
from time import sleep

execution = []

def timestamp(func):
    global execution
    def wrapper(*args):
        timestamp = datetime.now()
        string_timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')
        execution.append([string_timestamp, func.__name__])
        return func(*args)
    return wrapper 

@timestamp
def add(*args):
        return sum(args) 
@timestamp
def sub(*args):
    total = args[0]
    for i in range(1, len(args)-1):
        total -= args[i]
    return total 

if __name__ == "__main__":
    #functions = [add, sub]
    num = 0
    while num != 3:
        #print(functions[randrange(0, 2)](10, 7 , 6))
        print(add(10, 7 , 6))
        sleep(1)
        print(sub(10, 7 , 6))
        sleep(1)
        num += 1


print(execution)