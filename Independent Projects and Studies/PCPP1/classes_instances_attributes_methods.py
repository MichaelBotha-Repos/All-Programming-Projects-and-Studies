"""
Scenario
create a class representing a mobile phone;
your class should implement the following methods:
__init__ expects a number to be passed as an argument; this method stores the number in an instance variable self.number
turn_on() should return the message 'mobile phone {number} is turned on'. Curly brackets are used to mark the place to insert the object's number variable;
turn_off() should return the message 'mobile phone is turned off';
call(number) should return the message 'calling {number}'. Curly brackets are used to mark the place to insert the object's number variable;
create two objects representing two different mobile phones; assign any random phone numbers to them;
implement a sequence of method calls on the objects to turn them on, call any number. Print the methods' outcomes;
turn off both mobiles.

"""

class Mobile:
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def turn_on(self):
        print(f"mobile phone {self.phone_number} is turned on")

    def turn_off(self):
        print(f"mobile phone is turned on off")

    def call_number(self, called_number):
        self.called_number = called_number
        print(f"calling {self.called_number}")



nokia = Mobile("0460863194")
samsung = Mobile("0460874482")

nokia.turn_on()
nokia.call_number("10111")
nokia.turn_off()

samsung.turn_on()
samsung.call_number("112")
samsung.turn_off()