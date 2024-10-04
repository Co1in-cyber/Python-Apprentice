
"""
Turtles with a loop. 

This program has four identical lines of code to draw a square, 
but you know you can use a loop to make the program simpler. 

"""


import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window


tina = turtle.Turtle()       
tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)    
            
for i in range(4):
    print('Loop Iteration', i)



    tina.forward(150)
    tina.left(90)


turtle.exitonclick()                    # Close the window when we click on it
