# Classes
# Import turtle from Turtle class
from turtle import Turtle, Screen

# Assign timmy object to Turtle class
timmy = Turtle()
# Print object
print(timmy)
# calling the shape,color & forward method from the turtle class
timmy.shape("turtle")
timmy.color("blue")
timmy.forward(100)

# Assign the my_screen object to the Screen class
my_screen = Screen()
# printing the attribute from the screen class
print(my_screen.canvheight)
# close the screen once someone has clikced
my_screen.exitonclick()




