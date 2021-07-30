first_number = int(input('please enter a number : '))
second_number = int(input("please enter the second number to calculate : "))

operator_selecing = input('please choose your operator : '))

if operator_selecting == '+':
	print('sum of two numbers that you entered is : {first_number + second_number}')
elif operator_selecting == '-':
	print('mines of two numbers that you entered is : {first_number - second_number}')
elif operator_selecting == '*':
	print('multiply of two numbers that you entered is : {first_number * second_number}')
elif operator_selecting == '/':
	print('division of two numbers that you entered is : {first_number / second_number}')
else :
	print('Wrong operator entering')	
