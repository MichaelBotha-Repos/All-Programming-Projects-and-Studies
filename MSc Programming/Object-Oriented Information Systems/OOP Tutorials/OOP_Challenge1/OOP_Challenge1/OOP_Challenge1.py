'''
    In this challenge, you will create five Person objects with appropriate values for first name, last name, weight, and height.
    Once you have all five objects, create a list and store the objects in the list. Recall, an object is simply an instance of a user-defined type, so the syntax is the same as adding any other variable to a list.
    Using a for loop, iterate over your list and print out the first names of each of your Person objects that you created. The output should look something like this:
    Tom
    Fred
    George
    Tanya
    Mary
    Step 4 will require you to think about how you will access each member of the list and then how to access the correct attribute of that object to output it with a print statement
    
'''

class Person:
    def __init__(self, fname,lname, weight, height):
        self.fname = fname
        self.lname = lname
        self.weight = weight
        self.height = height 


P1 = Person('Tom','Jones', 100, 185)
P2 = Person('Fred','Jones', 80, 165)
P3 = Person('George','Jones', 110, 195)
P4 = Person('Tanya','Jones', 65, 165)
P5 = Person('Mary','Jones', 70, 170)

people = [P1, P2, P3, P4, P5]

for person in people:
    print(person.fname)