#--------------48 Different Dinner Options--------------#

#--------------INITIALIZE--------------#
import turtle as trtl
wn = trtl.Screen()
pen = trtl.Turtle()
wn.bgpic("Table.png")
#--------------------------------------#

#--------------INPUTS--------------#
steakRareity = input("How do you want your steak cooked? [Rare, Medium Rare, Well Done]")
chimi = input("Do you want Chimichurri (Steak Sauce)? [y/n]")
Mpotatos = input("Do you want Mashed Potatoes? [y/n]")
MpotatosGravy = input("Do you want gravy on your Potatoes? [y/n]")
Bspouts = input("Do you want brussle sprouts? [y/n]")
BspoutsGrilled = input("Do you want brussle Sprouts grilled? [y/n]")
#--------------------------------------#

#--------------STEAK VARABLES--------------#
rare = "#e87968"
medumRare = "#a14b3a"
wellDone = "#612b20"
#--------------------------------------#

def plate(pen): # PLATE FUNCTION #
    pen.fillcolor("#808080")
    pen.color("#808080")
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
    elif(steakRareity == "Medium Rare"):
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
    pen.setposition(-380, -236)
    pen.color("#d9c9ab")
    pen.pendown()

    pen.setheading(90)
    pen.forward(120)
    pen.left(90)
    pen.forward(10)
    pen.left(90)
    pen.forward(120)

def chimichurri(pen):
    pen.penup()
    pen.setposition(-378, -116)
    pen.color("#0f4d1a")
    pen.fillcolor("#0f4d1a")
    pen.setheading(-90)
    pen.pendown()
    pen.begin_fill()

    # First shape
    x = 1
    while x < 20:
        pen.forward(5)
        pen.left(10)
        x += 1

    # Second shape
    pen.setheading(-90)
    y = 1
    while y < 25:
        pen.forward(7)
        pen.left(8)
        y += 1

    # Third shape
    pen.setheading(-90)
    z = 1
    while z < 20:
        pen.forward(6.5)
        pen.left(10)
        z += 1

    pen.setheading(180)
    pen.setposition(-378, -116)
    pen.end_fill()  # End fill after all shapes are drawn

def mashed_potatoes(pen):
    # Move to the specified starting position
    pen.penup()
    pen.setposition(-3,-150)
    pen.setheading(90)
    pen.width(0)
    pen.pendown()

    # Define the base circle size and spacing
    base_size = 50  # Circle size
    spacing = 18
    pencolor = "burlywood"

    if(MpotatosGravy == "y" and Mpotatos == "y"):
        pencolor = "#75512a"

    

    # Draw the bottom layer of the pyramid
    for i in range(3):  # 3 circles at the bottom
        pen.penup()
        pen.goto(35 - base_size + (i * (base_size + spacing)), -220)  # Adjust x position
        pen.pendown()
        pen.begin_fill()
        pen.color("burlywood")  # Color for mashed potatoes
        pen.circle(base_size)
        pen.end_fill()

    # Draw the middle layer of the pyramid, shifted to the right
    for i in range(2):  # 2 circles in the middle
        pen.penup()
        pen.goto(35 - base_size // 2 + (i * (base_size + spacing * 1.5)), -220 + base_size + spacing)  # Adjust x and y position
        pen.pendown()
        pen.begin_fill()
        pen.color(pencolor)
        pen.circle(base_size)
        pen.end_fill()

    # Draw the top layer of the pyramid
    pen.penup()
    pen.goto(35, -220 + 2 * (base_size + spacing))  # Center the top circle
    pen.pendown()
    pen.begin_fill()
    pen.color(pencolor)
    pen.circle(base_size)
    pen.end_fill()


steak(pen, steakRareity)

if(chimi == "y"):
    chimichurri(pen)
if(Mpotatos== "y"):
    mashed_potatoes(pen)


def brusslegreens(pen):

    cookedorNAH = "#3d8039"
    if(BspoutsGrilled == "y"):
        cookedorNAH = "#1c331b"

    pen.penup()
    pen.setposition(360, -258)
    pen.setheading(90)
    pen.width(2)
    pen.color(cookedorNAH)
    pen.fillcolor(cookedorNAH)
    pen.begin_fill()
    pen.pendown()

    y = 1
    while y < 3:

        pen.circle(55,180)
        pen.end_fill()

        pen.setheading(90)
        pen.begin_fill()
        y += 1


if(Bspouts == "y"):
    brusslegreens(pen)


plate(pen)


#--------------DRAW TO SCREEN--------------#
pen.hideturtle()
wn.mainloop()
