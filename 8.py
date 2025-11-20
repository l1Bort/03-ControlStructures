###
# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.   
# 
number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")
operator = input("Enter an operator (+, -, *, /): ")

if operator == "+":
    result = float(number1) + float(number2)
elif operator == "-":
    result = float(number1) - float(number2)
elif operator == "*":
    result = float(number1) * float(number2)
elif operator == "/":
    result = float(number1) / float(number2)
else:
    result = "Invalid operator"

# print result
print(f'{number1} {operator} {number2} = {result}')