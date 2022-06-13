"""
Scenario
Create a class representing a time interval;
the class should implement its own method for addition, subtraction on time interval class objects;
the class should implement its own method for multiplication of time interval class objects by an integer-type value;
the __init__ method should be based on keywords to allow accurate and convenient object initialization, but limit it to hours, minutes, and seconds parameters;
the __str__ method should return an HH:MM:SS string, where HH represents hours, MM represents minutes and SS represents the seconds attributes of the time interval object;
check the argument type, and in case of a mismatch, raise a TypeError exception.

Scenario
Extend the class implementation prepared in the previous lab to support the addition and subtraction of integers to time interval objects;
to add an integer to a time interval object means to add seconds;
to subtract an integer from a time interval object means to remove seconds.

"""

class TimeInterval:
    def __init__(self, hours= 0, min= 0, sec= 0):
        if type(hours).__name__ != 'int':
            raise TypeError("wrong type for 'hours'")
        elif type(min).__name__ != 'int':
            raise TypeError("wrong type for 'min'")
        elif type(sec).__name__ != 'int':
            raise TypeError("wrong type for 'sec'")
        else:
            self.hours = hours
            self.min = min
            self.sec = sec 
        self.total_time = (self.hours * 60 * 60) + (self.min * 60) + sec

    def convert(self,total):
        time_dict = {}
        if total < 60:
            time_dict = {'sec' : total}
        elif (total >= 60) and (total < 3600):
            sec = total % 60
            min = int(total/60)
            time_dict = {'min' : min, 'sec' : sec}
        else:
            hour = int(total / 3600)
            min = int((total % 3600) / 60)
            sec = int((total % 3600) % 60)  
            time_dict = {'hour' : hour, 'min' : min, 'sec' : sec}
        return time_dict

    def __add__(self, other):
        if type(other).__name__ == 'int':
            return self.convert(self.total_time + other)
        else:
            return self.convert(self.total_time + other.total_time)

    def __sub__(self, other):
        if type(other).__name__ == 'int':
            return self.convert(self.total_time - other)
        else:
            return self.convert(self.total_time - other.total_time)

    def __mul__(self, other):
        return self.convert(self.total_time * other)

    def __str__(self):
        time_dict = self.convert(self.total_time)
        return f"{time_dict['hour']}:{time_dict['min']}:{time_dict['sec']}" 


time1 = TimeInterval(4, 5, 30)
time2 = TimeInterval (sec = 500)

print(time1 + time2)
print(time1 - time2)
print(time1 + 1000)
print(time2 -30)
print(time1 * 5)
print(time1)
