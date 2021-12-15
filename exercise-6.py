# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.


month = input (f"Please enter the month of the year (Jan- Dec) as three characters")
day = int(input(f"Please enter the day of the month in 2 digits"))
season = " "
if month in ("Jan", "Feb", "Mar"):
  season = "Winter!"
  print(f"{month} {day} is in the {season}")
elif month in ("Apr", "May", "Jun"):
  season = "Spring!"
  print(f"{month} {day} is in the {season}")
elif month in ("Jul", "Aug", "Sep"):
  season = "Summer!"
  print(f"{month} {day} is in the {season}")
if month == "March" and day > 19:
  season = "Spring!"
  print(f"{month} {day} is in the {season}")
elif month == "Jun" and day > 20: 
  season = "Summer!"
  print(f"{month} {day} is in the {season}")
elif month == "Sep" and day > 21:
  season = "Fall!"
  print(f"{month} {day} is in the {season}")
elif month == "Dec" and day > 20:
  season = "Winter!"
  print(f"{month} {day} is in the {season}")
else:
  season = "Fall!"
  print(f"{month} {day} is in the {season}")

# Everything returns as in the fall! Need to troubleshoot more. 