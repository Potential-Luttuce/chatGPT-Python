# - 2 Saimple Calculator: 
# Create a calculator program that takes two numbers as input 
# from the user and performs basic arithmetic operations like 
# addition, subtraction, multiplication, and division.
import os 
os.system("clear && neofetch")

print('Welcome to the Calculator')

# Obtain Number 1
num1 = int(input('Number 1: '))
if isinstance(num1, int):
    print("Number 1 entered...")
else:
    print('Error: "' + num1 + '" Not Recognized as an integer\n')
    print('Please enter valid number.\nTry Again, please.')
    exit()

# Obtain Operator 
print('\nOperators Key-[+ = additon, - = subtraction, / = division, * = multiplication]')
op = input('Select an operator (+, -, / , *) : ')
if op == '+' or op == '-'or op == '/' or op == '*':
    print('Operator entered...\n')
else:
    print('\nError: "' + op + '" Not Recognized as an operator\n')
    print('Please enter correct operator.\nTry Again, please.')
    exit()

# Obtain Number 2
num2 = int(input('Number 2: '))
if isinstance(num2, int):
    print("Number 2 entered...\n")
else:
    print('\nError: "' + num2 + '" Not Recognized as an integer\n')
    print('Please enter valid number.\nTry Again, please.')
    exit()

# Display Outputs
operators = {
    '+' : 'Addition',
    '-' : 'Subtraction',
    '/' : 'Division',
    '*' : 'Multiplication'
}
print('Selected operator: ' + operators[op])
answer = 0
if op == '+':
    answer = (num1 + num2)
elif op == '-':
    answer = (num1 - num2)
elif op == '/':
    answer = (num1 / num2)
elif op == '*':
    answer = (num1 * num2)

print('Answer: ', answer)






