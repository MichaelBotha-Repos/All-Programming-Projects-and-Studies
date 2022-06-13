"""
Scenario
Imagine that you receive a task description of an application that monitors the process of apple packaging before the apples are sent to a shop.
A shop owner has asked for 1000 apples, but the total weight limitation cannot exceed 300 units.
Write a code that creates objects representing apples as long as both limitations are met. 
When any limitation is exceeded, then the packaging process is stopped, 
and your application should print the number of apple class objects created, and the total weight
Your application should keep track of two parameters:
the number of apples processed, stored as a class variable;
the total weight of the apples processed; stored as a class variable. 
ssume that each apple's weight is random, and can vary between 0.2 and 0.5 of an imaginary weight unit;
Hint: Use a random.uniform(lower, upper) function to create a random number between the lower and upper float values.

"""
import random

class Apple:
    total_number= 0
    total_mass = 0
    def __init__(self):
        self.mass = random.randrange(2, 6)/10
        Apple.total_number += 1
        Apple.total_mass += self.mass

apples = []
while (Apple.total_mass <= 300) and (Apple.total_number <= 1000):
    apples.append(Apple())
    if Apple.total_mass > 300:
        Apple.total_number -= 1
        Apple.total_mass -= apples[-1].mass
        del apples[-1]
        break

print(f"Total apples {Apple.total_number} \nTotal mass {Apple.total_mass}")





