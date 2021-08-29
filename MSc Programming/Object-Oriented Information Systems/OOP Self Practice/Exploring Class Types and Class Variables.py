from math import sqrt

## Displaying the class type of various built-in classes ##
print(type(1))
print(type(1.2))
print(type('1'))
print(type(True))
print(type(None))
print(type([1,2,3,4]))
print(type({'a':1, 'b':2}))


class Coord:
    ''' A Coord abstraction storing two points '''
    max_points = 0

    def __init__(self, x, y):
        ''' Initialising points '''
        assert Coord.max_points< 2
        self.x = x
        self.y = y
        Coord.max_points += 1

    def dist(point1, point2):
        ''' Calcualting the distance between two point '''
        return sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

# Creating and testing two point objects #
try: 
    P1 = Coord(1, 2)
    P2 = Coord(3, 4)
    print(Coord.max_points)
    print(Coord.dist(P1, P2))
    P3 = Coord(4,5)

except:
    print('too many points')

