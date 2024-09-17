#--------------INITIALIZE--------------#
import turtle as trtl
wn = trtl.Screen()
pen = trtl.Turtle()
wn.bgpic("Table.png")
#--------------------------------------#

#--------------INPUTS--------------#
steakRareity = input("How do you want your steak cooked? [Rare, Meduim Rare, Well Done]")
#--------------------------------------#

#--------------STEAK VARABLES--------------#
rare = "#e87968"
medumRare = "#a14b3a"
wellDone = "#612b20"
#--------------------------------------#

def plate(pen): # PLATE FUNCTION #
    pen.fillcolor("white")
    pen.color("white")
    pen.width(1)
    pen.penup()
    pen.setposition(-400, -250)
    pen.setheading(0)
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

def steak(pen, steakRareity):   # STEAK FUNCTION #
    pen.penup()
    pen.width(30)
    pen.color("#543421")

    if(steakRareity == "Rare"):
        pen.fillcolor(rare)
    elif(steakRareity == "Meduim Rare"):
        pen.fillcolor(medumRare)
    elif(steakRareity == "Well Done"):
        pen.fillcolor(wellDone)
        
    pen.setposition(-370, -236)
    pen.pendown()

    pen.begin_fill()
    pen.setheading(90)
    pen.forward(120)
    pen.right(90)
    pen.forward(230)
    pen.right(90)
    pen.forward(120)
    pen.right(90)
    pen.forward(230)
    pen.end_fill()

    pen.penup()
    pen.setposition(-400, -236)
    pen.color("#d9c9ab")
    pen.pendown()

    pen.setheading(90)
    pen.forward(120)
    pen.left(90)
    pen.forward(10)
    pen.left(90)
    pen.forward(120)


steak(pen, steakRareity)
plate(pen)
#--------------DRAW TO SCREEN--------------#
pen.hideturtle()
wn.mainloop()
