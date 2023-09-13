"""
This script includes functions of turtle library
"""




# step01: import turtle
import turtle

#Step 2: Create a turtle control: window/board
win = turtle.Screen()        # create a graphcs window as win
win.title("My First Screen") # giving the title as my first window
win.bgcolor("light blue")    # assign the light blue color to window

# Step3: my window now is ready and i need to create a turtle to control
turta = turtle.Turtle()  # I gave the name turta to my turtle
turta.shape("square")    # changing the turtle shape: turtle, circle, triangle, square
#turta.hideturtle()      # to hide the turtle from the screen
#turta.showturtle()      # to show the turtle
turta.color("red")       # make turta red (default color is black)
turta.pensize(4)         # set the width of turta as 4
turta.pencolor("yellow") # set the line color to yellow
#turta.pendown()         # start the turtle drawing again. Similar function which is down()
#turta.penup()           # Stop the turtle from drawing. Similar function which is up()
turta.speed(1)           # the speed is set to 1 (slowest). 10 is fastest

# Step4: draw around using the turtle methodes
###01. forward(distance) : moves the turtle forward by a specific distance
# turta.forward(200) #turta.fd(200)

###02. backward(distance): moves turta backard by a specific number of units (distance)
#turta.backward(100)
###03 right - turns the turtle clockwise
# turta.right(90)
# turta.forward(200)
# turta.right(90)
# turta.forward(200)
# turta.right(90)
# turta.forward(200)
#turta.setheading(80) # make the turtle point in a specific direction

###04 left(angle) - turns the turtle anti-clockwise
# turta.left(90)
# turta.forward(200)
# turta.left(90)
# turta.forward(200)
# turta.left(90)
# turta.forward(200)

#07 goto(x, y)
#turta.goto(10, 100)
#turta.forward(200)
#turta.home()                    # turtle to the center point (home)

# Step turtle fonctionality
turta.circle(80) # draw to a circle 
turta.dot(50)
turta.forward(200)

turta.begin_fill() # start filling a shape
turta.fillcolor("blue") # set fill color to blue
turta.circle(80)
turta.end_fill()   #end filling a shape


# Step x: last step -line in my code
#turtle.done() # same as:  
win.exitonclick()                   # set the screen to close when clicked
