n=100
i=1
c=0
while True:


    sum=0
    num =i
    tnum  =num
    while num!=0:
        r=num%10
        sum =sum +r**3
        num =num//10
    if sum==tnum:
        print("amstrong")
    else:
        print("not amstrong")        