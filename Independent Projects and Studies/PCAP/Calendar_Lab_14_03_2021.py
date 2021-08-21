from calendar import Calendar 

class MyCalendar(Calendar):

    def __init__(self):
        Calendar.__init__(self)

    def count_weekday_in_year(self, year, weekday):
        count = 0
        for month in range(1,13):
            eachmonth = self.monthdays2calendar(year, month)
            for WeekDays in eachmonth:
                print(WeekDays)
                for i in WeekDays:
                    if (i[1] == weekday) and (i[0]!=0): 
                        print(i[1])
                        count+=1
        print(count)


m = MyCalendar()

m.count_weekday_in_year(2019,4)