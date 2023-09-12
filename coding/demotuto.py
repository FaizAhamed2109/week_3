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

turta.forward(200) #You can also use turta.fd(200) ---> used for moving the cursor forward
# turta.backward(100)


turta.right(90) #Used for turning the cursor clockwise
turta.forward(200)

turta.right(90) #Used for turning the cursor clockwise
turta.forward(200)

turta.penup()
turta.right(90) #Used for turning the cursor clockwise
turta.forward(200)

turta.left(90) #Used for turning the cursor anit-clockwise
turta.forward(200)

turta.right(90) #Used for turning the cursor clockwise
turta.forward(200)

turta.right(90) #Used for turning the cursor clockwise
turta.forward(200)

turta.pendown() # Used for not making the pen create a mark
turta.right(90) #Used for turning the cursor clockwise
turta.forward(200)

turta.goto(10, 100)
turta.forward(100)

turtle.done() # This can be also written as win.exitonclick() OR win.bye()