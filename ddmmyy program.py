#Harry Derouich
#03/10/14
#Stretch and challenge exercise 2

date = input("Please enter the date in the format dd mm yy: ")

day = int(date[:3])
month = int(date[3:5])
year = int(date[6:])

print(day)
print(month)
print(year)

#if day == "01":
  #  day_format = "1st"
#elif day == "02":
 #   day_format = "2nd"
#elif day == "03":
 #   day_format = "3rd"
#else:
   # day_format = "error"
#^^Come back to this later
    #print(day_format)

#month calculations below
if month == "01":
    month_format = "January"
elif month == "02":
    month_format = "February"
elif month == "03":
    month_format = "March"
elif month == "04":
    month_format = "April"
elif month == "05":
    month_format = "May"
elif month == "06":
    month_format = "June"
elif month == "07":
    month_format = "July"
elif month == "08":
    month_format = "August"
elif month == "09":
    month_format = "September"
elif month == "10":
    month_format = "October"
elif month == "11":
    month_format = "November"
elif month == "12":
    month_format = "December"
else:
    month_format = "This isnt working"

#year calculations below

if 20 >= year >= 99:
    year_format = ("19{0}".format(year))
elif 0 >= year >= 19:
    year_format = ("20{0}".format(year))
else:
    year_format = ("This isnt working")

print(year_format)

    
