import turtle

turtle.pensize(3)
turtle.speed(5)

distance = 10
for i in range(0, 300, 10):
    turtle.left(90)
    turtle.forward(distance+i)




turtle.Screen().exitonclick()