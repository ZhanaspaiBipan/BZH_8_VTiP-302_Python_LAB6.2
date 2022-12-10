import turtle

t = turtle.Pen()

t.fillcolor('blue')
t.begin_fill()
t.circle(100)
t.up()
t.goto(0, 130)
t.down()
t.end_fill()


t.fillcolor('red')
t.begin_fill()
t.circle(20)
t.down()
t.end_fill()
t.right(60)
t.circle(-140, 55)
t.down()


t.penup()
t.goto(-13, 135)
t.down()
t.pendown()
t.right(50)
t.circle(90, 82)


t.penup()
t.goto(-20, 150)
t.right(130)
t.pendown()
t.circle(60, 72)


t.penup()
t.goto(-10, 167)
t.right(110)
t.pendown()
t.circle(60, 40)
t.end_fill()

t.penup()
t.goto(17, 157)
t.right(80)
t.pendown()
t.circle(60,38)


t.penup()
t.goto(20, 150)
t.right(140)
t.pendown()
t.circle(-160, 47)

turtle.done()
