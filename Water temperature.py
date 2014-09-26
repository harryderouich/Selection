#Harry Derouich
#26/09/14
#Is my water boiling or frozen - or neither?

print("Hello User")
temp = float(input("Please enter the temperature of your water: "))

if temp >= 100:
    print("Your water is boiling - be careful")
elif temp < 0:
    print("Your water is frozen, brr!")
else:
    print("Your water is neither frozen or boiling")
    
