sub1=int(input("enter the sub1 marks:"))
sub2=int(input("enter the sub2 marks:"))
sub3=int(input("enter the sub3 marks:"))
if sub1>40 and sub2>40 and sub3>40:
    avg=(sub1+sub2+sub3)/3
    if avg>=40 and avg<60:
        print("c")
    elif avg>=60 and avg<90:
        print("b")
    elif avg>=90 and avg<=100:
        print("a")
else:
    print("better luck next time")                