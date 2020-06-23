import turtle
t = turtle.Turtle()
t.shape("turtle")


s = turtle.textinput("??","입력하십시오")
n=int(s)


for i in range(n):
    t.forward(50)
    t.left(360/n)




