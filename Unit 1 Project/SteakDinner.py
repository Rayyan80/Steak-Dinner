#--------------INITIALIZE--------------#
import turtle as trtl
wn = trtl.Screen()
pen = trtl.Turtle()

wn.bgcolor("gray")
#--------------------------------------#

#--------------INPUTS--------------#

#--------------------------------------#

def plate(pen): # PLATE FUNCTION #
    pen.fillcolor("white")
    pen.color("white")
    pen.penup()
    pen.setposition(-400, -250)
    pen.pendown()
    pen.forward(800)

    # Draw the semi-circle
    pen.begin_fill()
    pen.penup()
    pen.setposition(-400, -250)
    pen.setheading(-90)
    pen.pendown()
    pen.circle(80,45)
    pen.setheading(0)
    pen.forward(700)
    pen.end_fill()

    pen.penup()
    pen.begin_fill()
    pen.setposition(400, -250)
    pen.pendown()
    pen.setheading(-90)
    pen.circle(-80,45)
    pen.setheading(180)
    pen.forward(700)
    pen.end_fill()

plate(pen)
#--------------DRAW TO SCREEN--------------#
pen.hideturtle()
wn.mainloop()
