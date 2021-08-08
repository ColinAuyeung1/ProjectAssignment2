month = int(input("enter a month (1-12):"))
year = int(input("enter a year:"))
isLeap = False
days = 0

if (year % 400 == 0):
    isLeap = true
elif (year % 100 == 0):
    isLeap = False
elif (year % 4 == 0):
    isLeap = True

if (isLeap and month == 2):
    days = 29

elif month == 1:
    days = 31
elif month == 2:
    days = 28
elif month == 3:
    days = 31
elif month == 4:
    days = 30
elif month == 5:
    days = 31
elif month == 6:
    days = 30
elif month == 7:
    days = 31
elif month == 8:
    days = 31
elif month == 9:
    days = 30
elif month == 10:
    days = 31
elif month == 11:
    days = 30
elif month == 12:
    days = 31

print("This month has ",days,"Days")