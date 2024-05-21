"""Write a program that calculates the total amount of a meal purchased at a restaurant. 
Approach: 
Use input function to obtain food price. Then use expressions to calculate food with tip and total price. Print out variables. Use while loop to handle input errors. 
Challenges: 
•	Printed varied decimal points. I used round(price, 2) so it makes sense of the price scenario. 
•	I didn’t give prompt to enter an integer and it throws an error when you enter non-numerical value. “ValueError: could not convert string to float”. 
•	I created a while loop to handle the exceptions and alert message.
•	I used a while loop to test whether the input is numerical, if not, loop back. But I accidentally created infinite loop. Below. If fixed it by moving the input_price =input() in the while  loop.
"""
 

def price_func():    
    n=0
    while True:
        try:
            input_price=input("Enter the base price for the food.") 
            input_price = float(input_price)
            break
        except ValueError:
            print("Invalid input! Please enter a numerical value.")            
            n+=1
            if n<5:
                continue
            elif n==5:
                print("You have 1 last chance to enter a numerical value.")
                continue
            else: 
                print("Unable to process your request. Exiting...")
                return
            
    mealPrice=round(input_price,2)
    mealPricePlusTip=round(mealPrice*(1+0.18),2)
    totalPrice=round(mealPricePlusTip*(1+0.07),2)
    print ("food price is: ", mealPrice,"food price with tip is: ", mealPricePlusTip,
       "total price is: ", totalPrice,
       sep='\n')

if __name__ == "__main__": price_func()