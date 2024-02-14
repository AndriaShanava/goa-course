# my_name = "andria"
# my_age = 13
# my_age = my_age + 10

# print(my_age)

# print(my_name + " ათ ი წლ ის მერ ე იქნება " + str(my_age))



from turtle import *

width(6)
begin_fill()
color("purple")
speed(6)
shape("turtle")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()
#end of square

#drawing adoor
begin_fill()
forward(70)
color("yellow")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#start first window

penup()
goto(130, 130)
pendown()

color("blue")
left(120)
forward(50)

left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)



#start second window

penup()
goto(60, 130)
pendown()

right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(25)
right(90)
forward(50)

penup()
goto(130, 130)
pendown()

right(90)
forward(25)
left(90)
forward(50)





penup()
goto(0, 0)
pendown()

color("orange")
begin_fill()
left(90)
forward(200)
right(90)
forward(200)
right(90)
forward(200)
end_fill()

color("blue")
begin_fill()
left(120)
forward(200)
left(120)
forward(200)
end_fill()


penup()
goto(-130, 0)
pendown()


#darwing a door

begin_fill()
left(210)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()


#start first window

penup()
goto(-130, 140)
pendown()

right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(25)
right(90)
forward(50)


#start second window

penup()
goto(-70, 140)
pendown()


forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
right(90)
forward(25)
left(90)
forward(50)


#satrt third home

penup()
goto(-200, 0)
pendown()

color("red")
begin_fill()
left(90)
forward(200)
right(90)
forward(200)
right(90)
forward(200)
end_fill()



color("gray")
begin_fill()
left(120)
forward(200)
left(120)
forward(200)
end_fill()


#drawing a door

penup()
goto(-330, 0)
pendown()


begin_fill()
right(150)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

  
#drawing a first window

penup()
goto(-260, 140)
pendown()

left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(25)
left(90)
forward(50)


#drawing a second window

penup()
goto(-330, 140)
pendown()

left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(25)
right(90)
forward(50)

penup()
goto(-260, 0)
pendown()


color("green")
begin_fill()
right(180)
forward(120)

forward(90)
forward(90)
left(90)
forward(380)
left(90)
forward(300)
end_fill()

penup()
goto(200, 320)
pendown()

color("yellow")
forward(50)
left(180)
forward(100)
left(180)
forward(50)
right(90)
forward(50)
left(180)
forward(100)
left(180)
forward(50)
left(45)
forwward(50)
left(180)
forward(100)









exitonclick()