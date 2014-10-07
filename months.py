#Harry Derouich
#07/10/14
#Month calculations

month = int(input("Please enter the number of the month: "))


if month == ("1"):
    month_format = "January"
elif month == ("2"):
    month_format = "February"
elif month == ("3"):
    month_format = "March"
elif month == ("4"):
    month_format = "April"
elif month == ("5"):
    month_format = "May"
elif month == ("6"):
    month_format = "June"
elif month == ("7"):
    month_format = "July"
elif month == ("8"):
    month_format = "August"
elif month == ("9"):
    month_format = "September"
elif month == 10:
    month_format = "October"
elif month == 11:
    month_format = "November"
elif month == 12:
    month_format = "December"
else:
    month_format = "This isnt working"

print("The month is: {0}".format(month_format))
