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


month = (input(f"Please enter the month of the year (Jan- Dec) as first letter Uppercase and the rest lowercase. ")).lower()
new_month = month[0].upper() + month[1:]
day = int(input(f"Please enter the day of the month in 2 digits"))
season = " "
if new_month in ("Jan", "Feb", "Mar"):
  season = "Winter!"
  
elif new_month in ("Mar", "Apr", "May", "Jun"):
  season = "Spring!"
  
elif new_month in ("Jun", "Jul", "Aug", "Sep"):
  season = "Summer!"
  
elif new_month in ("Sep", "Oct", "Nov", "Dec"):
  season = "Fall!"
  
if new_month == "Mar" and day > 19:
  season = "Spring!"
  
elif new_month == "Jun" and day > 20: 
  season = "Summer!"
  
elif new_month == "Sep" and day > 21:
  season = "Fall!"
  
elif new_month == "Dec" and day > 20:
  season = "Winter!"

print(f"{new_month} {day} is in the {season}")

# Everything returns as in the fall! Need to troubleshoot more. 