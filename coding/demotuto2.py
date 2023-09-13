import turtle

#To create a turtle control: window/board
win=turtle.Screen()



win.title("My First Screen") # Used to change the title of the screen
win.bgcolor("black") # Used to change the color of the screen

turta = turtle.Turtle() #gave name to my turtle as turta(cursor)
turta.color("white") #make turta color white as default colour is black
turta.pensize(4) #setting the width of the turta to size 4
turta.pencolor("white") #changing the turta colour
turta.speed(1) #setting the speed of the cursor movement from 0 to 200 (1-slowest) & (10-fastest)
turta.shape("triangle") # setting the shape of the turtle


turta.setheading(0) # making the turtle to start at an initial direction

turta.forward(200) #You can also use turta.fd(200) ---> used for moving the cursor forward
# turta.backward(100)


turta.right(90) #Used for turning the cursor clockwise
turta.forward(200)

turta.right(90) #Used for turning the cursor clockwise
turta.forward(200)

# turta.penup()
turta.right(90) #Used for turning the cursor clockwise
turta.forward(200)

# turta.left(90) #Used for turning the cursor anit-clockwise
# turta.forward(200)

# turta.right(90) #Used for turning the cursor clockwise
# turta.forward(200)

# turta.right(90) #Used for turning the cursor clockwise
# turta.forward(200)

# # turta.pendown() # Used for not making the pen create a mark
# turta.right(90) #Used for turning the cursor clockwise
# turta.forward(200)

# turta.goto(100, 100)
# turta.forward(100)

# turta.hideturtle() # used for hiding the turtle cursor
turta.circle(20)
turta.dot(20)

turta.begin_fill()
turta.forward(100)

turta.circle(20)
turta.fillcolor("red")
turta.end_fill()
 
turta.home() # making the turtle back to the center point (home)

turtle.done() # This can be also written as win.exitonclick() OR win.bye()