# Python Program to Add and Subtract Two Numbers
#version 1
def main():


    num1 = ask_for_number("Enter the first Number: ")
    num2 = ask_for_number("Enter the second Number: ")

    add_result = num1 + num2
    sub_result = num1 - num2

    print(num1, " + ",  num2, " = ", add_result)
    print(num1, " - ",  num2, " = ", sub_result)

def ask_for_number(text):
    not_number = True
    while not_number: 
        res = input(text)
        try:
            return float(res)        
        except ValueError:
            not_number = True
            print("Please provide a number.\n")

if __name__ == '__main__' : main()

#version 2
 
import sys
 
redoInput = True

 
while redoInput:
    # Get the user input and validate the input type
    in1 = input('Enter your first integer:\n')
    in2 = input('Enter your second integer:\n')

    try:
        num1 = int(in1)
        num2 = int(in2)
        redoInput = False
    except ValueError:
        print('A provided input was not an integer, please try input again.')
        redoInput = True


 
print('The sum of', num1, 'and', num2, 'is', num1 + num2)
 
print('The difference between', num1, 'and', num2, 'is', num1 - num2)

 