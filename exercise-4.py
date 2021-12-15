# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

input("enter the lengths of three sides of a triangle")
a = input ("a: ")
b = input ("b: ")
c = input ("c: ")
if a == b and b == c:
  print(f"This is an equalateral triangle - all three sides, {a}, {b}, {c}, are equal in length")
elif a !=b and a !=c and b !=c:
  print(f"This is a scalene triangle - all three sides, {a}, {b}, {c}, are not equal in length ")
elif a == b or a == c or b == c:
  print(f"This is an isosceles triangle. Two sides out of {a}, {b}, and {c}, match in length. ")
  
