c=int(input("enter the credit:"))
if c>=0 and c<1000:
    print("welcome silver card member")
elif c>=1000 and c<10000:
    print("welcome gold card member")
elif c>10000:
    print("welcome platinum card member")        