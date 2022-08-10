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