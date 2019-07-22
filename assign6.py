rev=0
num=int(input("enter n"))
while num!=0:
    r=num%10
    rev =rev*10+r
    num =num//10
print(rev)
