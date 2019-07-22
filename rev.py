def palin(num):
    rev=0
    num=int(input("enter n"))
    while num!=0:
        r=num%10
        rev =rev*10+r
        num =num//10
    return num==rev
def genpalin(n):
    i=1
    c=0
    while True:
        if palin(i):
            c+=1
             

    