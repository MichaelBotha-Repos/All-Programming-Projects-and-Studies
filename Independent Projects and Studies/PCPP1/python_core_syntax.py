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
        self.time1_dict = self.convert(self.total_time)
        self.time2_dict = other.convert(other.total_time)
        """
        total_dict = {'hour' : time1_dict['hour'] + time2_dict['hour'], 
                      'min' : time1_dict['min'] + time2_dict['min'],
                      'sec' : time1_dict['sec'] + time2_dict['sec']}
        """
        return [self.time1_dict, self.time2_dict]


time1 = TimeInterval(4, 5, 30)
time2 = TimeInterval (sec = 500)

print(time1 + time2)