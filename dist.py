person=int(input("enter the no of per"))
dist=int(input("enter the dist"))
milage=int(input("enter the milage"))
fuel_price=int(input("enter the price"))

lit=dist/milage
tot=lit*fuel_price
pice=tot/person
print(f"total cost per persson is:{pice}")