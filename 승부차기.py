import random


options=["L","M","R"]




computer_choice=random.choice(options)
user_choice=input("어디를 수비하시겠어요?::")
while True:
    if computer_choice==user_choice:
        print("수비에 성공하셨습니다. 골키퍼는",user_choice,"로 힘차게 다이빙했고, 성공적으로 방어했습니다.")
        break

    if computer_choice!= user_choice:
        print("페널티 킥이 성공하였습니다.",computer_choice,"로 정확하게 꽂아넣습니다!")
        break
