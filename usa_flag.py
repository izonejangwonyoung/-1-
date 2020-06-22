import turtle

import turtle
os.system("pause")
#콘솔 계속 열어두기 :::스택오버플로우 참고햇츰



turtle.speed(100)


turtle.penup()

turtle.shape("turtle")

turtle.hideturtle()
#터틀때문에 잘 안 보여서 터틀 지워버림




#시작
#시작 좌표 적절히 배치..(0,0)했는데 오류나서 임의 좌표로 set 스택오버플로우에도 안 나옴





start_x = -130
start_y = 250

stripe_height = 20
stripe_width = 500

flag_height=263
flag_width=500


star_size = 12


#fuction 정의 시작
def draw_rectangle(x, y, height, width, color):
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.end_fill()
    turtle.penup()

def draw_star(x,y,color,length) :
    turtle.goto(x,y)
    turtle.setheading(0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color(color)
    for turn in range(0,5) :
        turtle.forward(length)
        turtle.right(144)
        turtle.forward(length)
        turtle.right(144)
    turtle.end_fill()
    turtle.penup()



def draw_stripes():
    x = start_x
    y = start_y
    #for문으로 설ㅇ정
    for stripe in range(0,6):
        for color in ["red", "white"]:
            draw_rectangle(x, y, stripe_height, stripe_width, color)

           
            y = y - stripe_height            

   
    draw_rectangle(x, y, stripe_height, stripe_width, 'red')
    y = y - stripe_height



def draw_square():
    square_height = (0.54) * flag_height
    square_width = (0.8) * flag_height
    draw_rectangle(start_x, start_y, square_height, square_width, 'midnightblue')
    #색상 navy or midnightblue 중에서 택할 것.

def draw_six_stars():
    gap_stars = 35
    gap_lines = stripe_height + 6
    y = 240
    
    for row in range(0,5) :
        x = -130
        
        for star in range (0,6) :
            draw_star(x, y, 'white', star_size)
            x = x + gap_stars
        y = y - gap_lines


def draw_five_stars():
    gap_stars = 35
    gap_lines = stripe_height + 6
    y = 230
   
    for row in range(0,4) :
        x = -115
         
        for star in range (0,5) :
            draw_star(x, y, 'white', star_size)
            x = x + gap_stars
        y = y - gap_lines


#fuction 실행

draw_stripes()

draw_square()

draw_six_stars()

draw_five_stars()


turtle.mainloop()
#종료 방지
