#Harry Derouich
#30/09/14
#Gross pay

print("Hello user")
total_hours = float(input("Please enter the number of hours you have worked this week: "))
hourly_pay = float(input("Please enter your hourly pay £"))

if total_hours > 40:
    normal_hours = 40
    extra_hours = total_hours - 40
else:
    normal_hours = total_hours
    extra_hours = 0

extra_pay = hourly_pay * 1.5

total_pay = (hourly_pay * normal_hours) + (extra_hours * extra_pay)

print("Your total pay for this week is: £{0}".format(total_pay))

#to check the entered data was processed correctly
#print("Total hours {0}".format(total_hours))
#print("Hourly pay {0}".format(hourly_pay))
#print("Normal hours {0}".format(normal_hours))
#print("Extra hours {0}".format(extra_hours))
#print("Extra pay {0}".format(extra_pay))

