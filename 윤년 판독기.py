years=int(input("판단하려는 연도를 입력하세요.:"))

if (years%4==0) and (years%100!=0) or (years%400==0):
    print("입력하신" ,years,"년은 윤년입니다.")

else:
    print("입력하신" ,years,"년은 윤년이 아닙니다.")
