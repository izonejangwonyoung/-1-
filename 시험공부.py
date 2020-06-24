# num=0;
#
# while num!=1:
#     num=int(input("몇단출력?:"))
#     i=1
#     while i<10:
#         print(num,"X",i,"=",num*i)
#         i=i+1




num=0;
while num!=1:
    num = int(input("숫자입력?:"))
    i=1
    sum_n=0
    while i<num+1:
        sum_n=sum_n+i
        i=i+1
    print(sum_n,end="")
    break