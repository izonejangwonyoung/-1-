num: int=int(input("입력: "))
sum=0
i=1
count=0

while sum < num:
    sum=sum+i
    i=i+1
    count=count+1
    if sum>num:
        sum=sum-(i-1)
        break



for i in range(1,count):
    if i==count-1:
        print(i,end='')
    else:
        print("%d+"%i,end='')

print("=%d" %(sum))