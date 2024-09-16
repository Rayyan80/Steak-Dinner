import turtle as trtl



wn = trtl.Screen()
    
# Create a turtle object
pen = trtl.Turtle()
pen.speed(2)  # Set the drawing speed (1 is slowest, 10 is fastest)
    
# Draw the plate (a circle)
pen.penup()  # Lift the pen to move it without drawing
pen.goto(0, -100)  # Move to the starting position
pen.pendown()  # Lower the pen to start drawing
pen.circle(100)  # Draw a circle with radius 100
    
# Draw the turtle (a smaller circle in the center)
pen.penup()
pen.goto(0, -50)  # Move to the starting position for the turtle
pen.pendown()
pen.circle(50)  # Draw a smaller circle with radius 50
    
# Draw turtle’s head
pen.penup()
pen.goto(0, -30)  # Move to the starting position for the head
pen.pendown()
pen.circle(20)  # Draw the head
    
# Draw turtle’s legs
leg_positions = [(40, -60), (-40, -60), (40, -20), (-40, -20)]
for (x, y) in leg_positions:
    pen.penup()
    pen.goto(x, y)  # Move to the position for each leg
    pen.pendown()
    pen.circle(10)  # Draw each leg

# Hide the turtle
pen.hideturtle()




wn = trtl.Screen()
wn.mainloop()