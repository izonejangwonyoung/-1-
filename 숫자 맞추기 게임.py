import random
number=random.randint(1,100)
count_game=0
print("1부터 100사이 숫자를 맞추시오")
while True:

    number_quiz=int(input("숫자를 입력하시오:"))
    print("입력값은",number_quiz,"입니다.")
    count_game=count_game+1

    if number>number_quiz:
        print("입력값보다 큽니다.")

    elif number<number_quiz:
        print("입력값보다 작습니다.")


    elif number==number_quiz:
        print("입력값과 같습니다.")
        print(count_game,"번 수행되었습니다.")


        break

