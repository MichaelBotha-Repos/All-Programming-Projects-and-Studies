import math


class Point:
    def __init__(self, x=0.0, y=0.0):

        self.__xcord = x
        self.__ycord = y

    def getx(self):   
        return self.__xcord

    def gety(self):
        return self.__ycord

    def distance_from_xy(self, x, y): 
        return math.hypot((self.__xcord-x), (self.__ycord-y))
        

    def distance_from_point(self, point):
        x = point.getx()
        y = point.gety()
        return math.hypot((self.__xcord-x), (self.__ycord-y))
        


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
