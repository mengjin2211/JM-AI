"""
Module 3 Critical Thinking -Part One Price
Write a program that calculates the total amount of a meal purchased at a restaurant. 
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