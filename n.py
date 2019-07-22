n=int(input("n:"))
for i in range(1,n+1):
    if i%3==0 and i%6==0 and i%9!=0:
        print(i)