
#Harry Derouich
#03/10/14
#Stretch and challenge exercise 2

date = input("Please enter the date in the format dd mm yy, (e.g. 10th October 1997 = 10 10 97): ")

#string splitting
day = int(date[:2])
month = int(date[3:5])
year = int(date[6:8])


##day calculations below##
if day == 0o1:
    day_format = ("1st")
    day_num = int(1)
elif day == 0o2:
    day_format = ("2nd")
    day_num = int(2)
elif day == 0o3:
    day_format = ("3rd")
    day_num = int(3)
elif day == 21:
    day_format = ("21st")
elif day == 22:
    day_format = ("22nd")
elif day == 23:
    day_format = ("23rd")
    day_num = "23"
elif day == 31:
    day_format = ("31st")
    day_num = int(31)
#Or statement to prevent dates such as 32th and 0th
elif day > 31 or day < 1:
    day_format = ("error")
else:
    day_format = ("{0}th".format(day))
    day_num = int(day)



#print(day_format)   

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
#Else statement prevents months anything above or below 1 and 12.
else:
    month_format = "error"

#print(month_format)

###end month calculations###



####year calculations below####
if 00 <= year <= 9:
    year_format = "200{0}".format(year)
elif 10 <= year <= 30:
    year_format = "20{0}".format(year)
else:
    year_format = "19{0}".format(year)

#print(year_format)

####end year calculations####

if month_format == "April" or month_format == "June" or month_format == "July" or month_format == "November":
    if day_num > 30:
        day_format = "Error"
elif month_format == "February":
    if day_num >= 29:
        day_format = "Error"
else:
    month_format = month_format


print("The date is: {0} {1} {2}".format(day_format, month_format, year_format))



    
