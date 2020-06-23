import turtle
import random

screen=turtle.Screen()
image1="C:\\front.gif"
image2="C:\\back.gif"
screen.addshape(image1)
screen.addshape(image2)

t1=turtle.Turtle()


print("동전 던지기 게임을 시작합니다.")
while True:

    pause=input("돌려라: ")
    coin = random.randrange(2)

    if coin==0:

        t1.shape(image1)
        t1.stamp()


    else:

        t1.shape(image2)
        t1.stamp()


    if pause =="q":
        break
# else:
print("게임이 종료되었습니다.")

