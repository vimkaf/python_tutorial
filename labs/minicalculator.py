<<<<<<< HEAD
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
=======
def menu():
	menu = """
	MINI Calculator \n
	A. \t Addition
	B. \t Subtraction
	C. \t Division
	D. \t Multiplication
	E. \t Exponential
	Q. \t Quit
	\n
	"""
	menu.replace(" ", "")
	print(menu)

	option = input("Choose an option: ")
	option = option.lower()

	return option

def calculate(a,b,option):
	operation = operands[option]

	if operation == '+': 
		result = a + b

	elif operation == '-':
		result = a - b

	elif operation == '*':
		result = a * b

	elif operation == '/':
		result = a / b

	elif operation == '**':
		result = a ** b

	else:
		result = "Error"

	return result

def display(a, b,result, option):
	operand = operands[option]
	print(f"{a} {operand} {b} = {result} ")



option = menu()
operands = {
	'a' : '+',
	'b' : '-',
	'c' : '/',
	'd' : '*',
	'e' : '**'
}

while option != 'q':
	a = int( input("a: " ) )
	b = int( input("b: " ) )

	result = calculate(a,b, option)

	display(a,b,result,option)

	option = menu()
>>>>>>> 51ec166319db6c4931a8ab422aec35999d51022c
