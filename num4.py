n=int(input("n"))
c=0
i=1
while True:
    if i%3==0 and i%6==0 and i%9!=0:
        print(i,end="")
        c+=1
    if c==n:
        break
    i=i+1    