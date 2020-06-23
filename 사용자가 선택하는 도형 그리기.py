import turtle
t = turtle.Turtle()
t.shape("turtle")


s = turtle.textinput("","도형 이름을 입력하십시오")
n=int(s)


if s== "사각형":
    s = turtle.textinput("", "가로 길이를 입력하세요")
    w= int(s)
    s = turtle.textinput("", "세로 길이를 입력하십시오")
    h = int(s)


    t.forward(w)
    t.left(90)
    t.forward(h)
    t.left(90)
    t.forward(w)
    t.left(90)
    t.forward(h)


if s=="삼각형":
    s = turtle.textinput("", "한 변의 길이를 입력하세요")
    l=int(s)

    t.forward(l)
    t.left(120)
    t.forward(l)
    t.left(120)
    t.forward(l)



