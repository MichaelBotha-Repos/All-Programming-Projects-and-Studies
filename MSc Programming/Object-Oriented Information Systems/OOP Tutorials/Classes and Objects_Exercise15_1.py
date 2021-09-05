'''Write a definition for a class named Circle with attributes center and radius, where center is a Point object and radius is a number.
Instantiate a Circle object that represents a circle with its center at   (150,100)  and radius 75.
Write a function named point_in_circle that takes a Circle and a Point and returns True if the Point lies in or on the boundary of the circle.
Write a function named rect_in_circle that takes a Circle and a Rectangle and returns True if the Rectangle lies entirely in or on the boundary of the circle.
Write a function named rect_circle_overlap that takes a Circle and a Rectangle and returns True if any of the corners of the Rectangle fall inside the circle.
Or as a more challenging version, return True if any part of the Rectangle falls inside the circle.'''

class Point:
  pass
  #def __init__(self, x, y):
  # self.x = x
  #self.y = y
    

class Circle:
  pass
  #def __init__(self, r, center):
  #self.center = center
  # self.radius = r
    
def point_in_circle(point_obj, circle_obj):
  if (circle_obj.radius < ((point_obj.x - circle_obj.center.x) + (point_obj.y - circle_obj.center.y))):
    return False
  else:
    return True

## My Tests ##
#Test_circle = Circle(75, Point(150, 100))
#print(point_in_circle(Test_circle,Point(300, 100)))
## See how python can pass a data structure with values without reference 
## to a particular variable name/assignment just like an int or char

class Rectangle:
  pass
  #def __init__(self,w=None , h=None, c):
    #self.width = w
    #self.height = h
    #self.corner = c
    #self.cornerRT = Point(self.corner.x + self.width, self.corner.y)
    #self.cornerRB = Point(self.corner.x + self.width, self.corner.y - self.height)
    #self.cornerLB = Point(self.corner.x, self.corner.y - self.height)
    

def rect_in_circle(rectangle_obj, circle_obj):
  rectangle_obj.cornerRT = Point()
  rectangle_obj.cornerRT.x = rectangle_obj.corner.x + rectangle_obj.width
  rectangle_obj.cornerRT.y = rectangle_obj.corner.y
  
  rectangle_obj.cornerRB = Point()
  rectangle_obj.cornerRB.x = rectangle_obj.corner.x + rectangle_obj.width
  rectangle_obj.cornerRB.y = rectangle_obj.corner.y - rectangle_obj.height
  
  rectangle_obj.cornerLB = Point()
  rectangle_obj.cornerLB.x = rectangle_obj.corner.x
  rectangle_obj.cornerLB.y = rectangle_obj.corner.y - rectangle_obj.height
                                 
  if(point_in_circle(rectangle_obj.corner, circle_obj) and point_in_circle(rectangle_obj.cornerRT, circle_obj)\
  and point_in_circle(rectangle_obj.cornerRB, circle_obj) and point_in_circle(rectangle_obj.cornerLB, circle_obj)):
  
    return True
  else:
    return False
    
def rect_circle_overlap(rectangle_obj, circle_obj):
  if(point_in_circle(rectangle_obj.corner, circle_obj) or point_in_circle(rectangle_obj.cornerRT, circle_obj)\
  or point_in_circle(rectangle_obj.cornerRB, circle_obj) or point_in_circle(rectangle_obj.cornerLB, circle_obj)):
  
    return True
  else:
    return False
  

def main():
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 50.0
    box.corner.y = 50.0

    circle = Circle
    circle.center = Point()
    circle.center.x = 150.0
    circle.center.y = 100.0
    circle.radius = 75.0

    print(point_in_circle(box.corner, circle))
    print(rect_in_circle(box, circle))
    print(rect_circle_overlap(box, circle))


if __name__ == '__main__':
    main()
  
