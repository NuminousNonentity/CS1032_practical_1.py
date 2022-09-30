Days = int(input("Enter a whole number of days: "))
Hours = int(input("Enter a whole number of hours: "))
Minutes = int(input("Enter a whole number of minutes: "))
Seconds = int(input("Enter a whole number of seconds: "))

hours = (Days * 24) + Hours
minutes = (hours * 60) + Minutes 
seconds = (minutes * 60) + Seconds 
print("That comes to a total of",seconds,"seconds ")
