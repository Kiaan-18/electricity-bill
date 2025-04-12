units= int(input("Enter the number of units consumed:"))
if units<=50:
    amount=units*2.60
    surtax=25
elif(units<=100 ):
    amount=130+(units -50)*3.25
    surtax=35
elif(units<=200):
    amount=130+162.50+(units-100)*5.26
    surtax=45
else:
    amount=130+162.50+526+(units-200)*8.45
total=surtax+amount
print("The electricity Bill is",total)
