import turtle
import random

screen=turtle.Screen()
image1="C:\\front.gif"
image2="C:\\back.gif"
screen.addshape(image1)
screen.addshape(image2)

t1=turtle.Turtle()


print("동전 던지기 게임을 시작합니다.")

coin=random.randrange(2)


if coin==0:
    print("앞면입니다.")
    t1.shape(image1)
    t1.stamp()
if coin==1:
    print("뒷면입니다.")
    t1.shape(image2)
    t1.stamp()

# else:
print("게임이 종료되었습니다.")

