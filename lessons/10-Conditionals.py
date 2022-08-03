"""
If - Else statements

Syntax
if condtion:    
    do something
else:
    do something else
"""

x = 15
y = 7

if x > y :
    print("x is greater than y")
else: 
    print("x is less than y")

age = 20
gender = "Male"

if age >= 18 and gender == "Male":
    print("You are eligible to vote!")
else:
    print("Sorry, you are not eligible.")


"""
If-ElseIf-Else
"""

score = 45

if score >= 50:
    print("You are above average")

elif score < 50:
    print("You are below average")

elif score == 0:
    print("You have no score")

else: 
    print("You must be dull")