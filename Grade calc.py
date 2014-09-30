#Harry Derouich
#30/09/14
#Grade calculator

print("Hello user")
mark = int(input("Please enter your mark: "))

if 100 >= mark >= 81:
    print("Grade A")
elif 80 > mark >= 71:
    print("Grade B")
elif 70 > mark >= 61:
    print("Grade C")
elif 60 > mark >= 51:
    print("Grade D")
elif 50 > mark >= 41:
    print("Grade E")
elif 40 > mark >= 0:
    print("Grade U")
else:
    print("This mark is out of the range")
