'''Write a function called draw_rect that takes a Turtle object and a Rectangle and uses the Turtle to draw the Rectangle.'''

import turtle

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

class Rectangle:
  def __init__(self,w , h, c):
    self.width = w
    self.height = h
    self.corner = c

def draw_rect(turtle_obj, Rect_obj):
  t.penup()
  turtle_obj.goto(Rect_obj.corner.x, Rect_obj.corner.x)
  t.pendown()
  turtle_obj.forward(Rect_obj.width)
  turtle_obj.lt(90)
  turtle_obj.forward(Rect_obj.height)
  turtle_obj.lt(90)
  turtle_obj.forward(Rect_obj.width)
  turtle_obj.lt(90)
  turtle_obj.forward(Rect_obj.height)

t = turtle.Turtle()
t2 = turtle.Turtle()
r = Rectangle(100, 50, Point(200,200))
draw_rect(t, r)

