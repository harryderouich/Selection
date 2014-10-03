#Harry Derouich
#03/10/14
#Stretch and challenge exercise 2

date = input("Please enter the date in the format dd mm yy, (e.g. 10th October 1997 = 10 10 97): ")

#string splitting
day = int(date[:2])
month = int(date[3:5])
year = int(date[6:])

print(day)
print(month)
print(year)

##day calculations below##
if day == 0o1:
    day_format = ("1st")
elif day == 0o2:
    day_format = ("2nd")
elif day == 0o3:
    day_format = ("3rd")
elif day == 21:
    day_format = ("21st")
elif day == 22:
    day_format = ("22nd")
elif day == 23:
    day_format = ("23rd")
elif day == 31:
    day_format = ("31st")
else:
    day_format = ("{0}th".format(day))
print(day_format)   

##end month calculations##


###month calculations below###

if month >= 10:
    month = month
else:
    month = date[4:5]

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

print(month_format)

###end month calculations###



####year calculations below####
#if year == 00:
   # year_format = "2000"
#elif year == 01:
   # year_format = "2001"
#else:
   # year_format = "I'll do this later"

#print(year_format)

####end year calculations####

print("The date is: {0} {1}".format(day_format, month_format))



    
