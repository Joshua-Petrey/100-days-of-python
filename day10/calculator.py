from art import logo

def add(n1, n2):
	'''Returns the sum of the two args'''
	return n1 + n2

def sub(n1, n2):
	'''Returns the difference of the two args'''
	return n1 - n2

def mult(n1, n2):
	'''Returns the product of the two args'''
	return n1 * n2

def div(n1, n2):
	'''Returns the quotient of the two args'''
	return n1 / n2

# map a symbol to a specific function
operations = {
	"+": add,
	"-": sub,
	"*": mult,
	"/": div,
}

def calculator():
	print(logo)
	num1 = float(input("Enter the first number.\n"))

	for symbol in operations:
		print(symbol)

	should_continue = True
	while should_continue:

		op = input("What operation do you want to perform?\n")
		num2 = float(input("Enter another number.\n"))
		# operations[op] is the function the symbol mapped to. 
		calc_function = operations[op]
		answer = calc_function(num1, num2)

		print(f"{num1} {op} {num2} = {answer}")
		
		if input(f"Type 'y' to keep calulating with {answer}, or 'n' to start new calculation ") == 'y':
			num1 = answer
		else:
			# if users types anything but 'y' exit the loop and recursively call calculator() again
			# to enter a new num1 
			should_continue = False
			calculator()

calculator()
