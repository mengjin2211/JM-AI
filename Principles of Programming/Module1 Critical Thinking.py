"""Part 1:
Write a Python program to find the addition and subtraction of two numbers.
Ask the user to input two numbers (num1 and num2). Given those two numbers, add them together to find the output. 
Also, subtract the two numbers to find the output.
"""
def get_numbers(message):
    while True:
        try:
            num1 = float(input(message+"Enter the first number: "))
            num2 = float(input(message+"Enter the second number: "))
            return num1, num2  # return the numbers when valid input is received
        except ValueError:
            print("Invalid input. Please enter numbers only")

# Perform adding and substraction
def add_substr():
    message="Addition and Division. "
    num1, num2 = get_numbers(message)  # call get_numbers() once and unpack the returned tuple
    sum = num1 + num2
    difference = num1 - num2

    # Print results  
    print("Sum of "+str(num1)+" and "+str(num2)+" is:", sum)
    print("Difference of "+str(num1)+" and "+str(num2)+" is:", difference)

"""Part 2:
Write a Python program to find the multiplication and division of two numbers.
Ask the user to input two numbers (num1 and num2). 
Given those two numbers, multiply them together to find the output. Also, divide num1/num2 to find the output."""
# Perform multiplication and division    
def multi_div():
    message="Multiplication and Division. "
    while True:
        
        num1, num2 = get_numbers(message)  # call get_numbers() once and unpack the returned tuple
        multi= round(num1 *num2, 2)
            # Handle division by zero error
        if num2 != 0:
            div = round(num1 / num2, 2)
            print("Multiplication of "+str(num1)+" and "+str(num2)+" results:", multi)
            print("Division of "+str(num1)+" and "+str(num2)+" results:", div)
            break
        else:
            print("Cannot divide by zero. Enter a non-zero for second number. Try again.")
            continue
add_substr()
multi_div()

