'''This program uses OOP to receive three values (hrs, mins, secs) and
then allows one to decrement or increment by one sec and then print the time'''

class Timer:
    def __init__(self,hr=0,mins=0,sec=0):
        
        self.hr = hr
        self.mins = mins
        self.sec = sec   

    def __str__(self):

        if self.sec < 10:
            self.str_sec = '0' + str(self.sec)
        else:
            self.str_sec = str(self.sec)
        if self.mins < 10:
            self.str_mins = '0' + str(self.mins)
        else:
            self.str_mins = str(self.mins)
        if self.hr < 10:
            self.str_hr = '0' + str(self.hr)
        else:
            self.str_hr = str(self.hr)
            
        return self.str_hr + ':' + self.str_mins + ':' + self.str_sec
        

    def next_second(self):
        
        if self.sec == 59:
            self.sec = 0
            if self.mins == 59:
                self.mins = 0
                if self.hr == 23:
                    self.hr = 0
                else:
                    self.hr += 1
            else:
                self.mins += 1
        else:
            self.sec += 1

    def prev_second(self):
        
        if self.sec == 0:
            self.sec = 59
            if self.mins == 0:
                self.mins = 59
                if self.hr == 0:
                    self.hr = 23
                else:
                    self.hr -= 1
            else:
                self.mins -= 1
        else:
            self.sec -= 1
          

timer = Timer(23,59,59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
