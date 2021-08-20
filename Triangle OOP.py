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


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):

        self.__len1 = vertice1.distance_from_point(vertice2)
        self.__len2 = vertice1.distance_from_point(vertice3)
        self.__len3 = vertice2.distance_from_point(vertice3)

    def perimeter(self):
        return self.__len1 + self.__len2 + self.__len3
        
        


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
