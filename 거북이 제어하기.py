import turtle
t = turtle.Turtle()


for i in range(1000):
    command= input("명령을 입력하세요.::")
    if command =="l":
        t.left(90)
        t.forward(100)

    elif command=="r":
        t.right(90)
        t.forward(100)


    elif command=="quit":
        break

