"""
a = 1
b = 2
action: add, sub, mul, div


Create a function called calculate
The function should take 3 parameters (a, b, action)
Depending on the action supplied perform the operation on a and b
return the result of the action

Exected Output

a: 2
b: 5
action(+,-,*,/): +

Output: 2 + 5 = 7 
"""

def calculate(a,b, action):
    result = 0

    if action == "+":
        result= a+b 
    elif action == "-":
        result= a - b
    elif action == "*":
        result = a * b
    elif action == "/":
        result = a / b
    elif action == "**":
        result = a**b
    else:
        result = "Error"
    

    return result



a = int(input("a: "))
b = int(input("b: "))
action = input("action(+,-,*,/,**): ")
output = calculate(a,b, action)

print(f"Output: {a} {action} {b} = {output}")
""" """
