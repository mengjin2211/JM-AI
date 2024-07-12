#import libraries
#from dateutil import parser
from datetime import datetime
import pandas as pd
 
#Step 1 ItemToPurchase Build class
class ItemToPurchase:
    """Build the ItemToPurchase class """
    def __init__(self,item_name='none',item_price=0,item_quantity=0,item_description='none'):
        self.item_name: str = str(item_name)   
        self.item_price: float = float(item_price)  
        self.item_quantity: int = int(item_quantity)   
        self.item_description=str(item_description)
    # calculate price. 
    def print_item_cost (self, print_output=True):
        price=self.item_price * self.item_quantity
        if print_output:
            print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${price:.2f}")
        return price
    # make the class object iterable
    def __iter__(self):
        return iter([self.item_name, self.item_price, self.item_quantity])

      
def get_item():
    """helper function to create ItemToPurchse class instance"""
    while True:
        try:
            item_name=input("Enter the item name (text): ")
            item_price=float(input("Enter the item price (float): "))
            item_quantity=int(input("Enter the item quantity (integer): "))
            
            if item_price < 0:
                raise ValueError("Price cannot be negative.")
            if item_quantity < 0:
                raise ValueError("Quantity cannot be negative.")
            
            item_description = input("Enter the item description (text): ")
            return ItemToPurchase(item_name, item_price, item_quantity,item_description)
        
        except ValueError as e:
            print ("Invalid Input.",
                "\nItem name only in text; item price fload; item quality integer; item description only in text.",
                "\nError Message: ",str(e))
            continue

##Step 4 build ShoppingCart class
class ShoppingCart:
    """ShoppingCart class creation with attributes (customer_name, date and cart_items) 
    and methods (add_item, remove_item, modify_item, get_num_items_in_cart, 
    get_cost_of_cart, print_total, print_descriptions)"""

    def __init__(self,customer_name='none',date='January 1, 2020'):
        self.customer_name: str=str(customer_name)  
        self.current_date: str= str(date) 
        self.cart_items=[]
     
    def add_item(self,item_to_purchase):           
        """Add items to the cart. If item already in the cart, only increment the quantity.""" 
        for item in self.cart_items:
            if item.item_name.lower() ==item_to_purchase.item_name.lower():
                item.item_quantity +=item_to_purchase.item_quantity
                print(f'{item.item_name.title()} exits your cart. Quantity increased.\n')
                return
        self.cart_items.append(item_to_purchase)
        print(f'{item_to_purchase.item_name.title()} has been added to your cart.\n')

    def remove_item(self, itemName):
        removed = [i for i in self.cart_items if i.item_name.lower() == itemName.lower()]
        self.cart_items = [i for i in self.cart_items if i.item_name.lower() != itemName.lower()]

        if removed:
            print(f'{itemName.title()} removed.\n' )
        else:
            print('Item not found in cart. Nothing removed.\n')
        
    def modify_item(self,item_to_purchase):  
        found=False
        for item in self.cart_items:
            if item_to_purchase.item_name.lower() ==item.item_name.lower():
                found=True
                if item_to_purchase.item_price!=0:
                    item.item_price=item_to_purchase.item_price
                if item_to_purchase.item_quantity!=0:
                    item.item_quantity=item_to_purchase.item_quantity
                if item_to_purchase.item_description!='none':
                    item.item_description=item_to_purchase.item_description
        if not found: 
            print('Item not found in cart. Nothing modified.\n') 
            
    def get_num_items_in_cart(self) -> int:
        """ Return total of quantity of items."""
        return sum(item.item_quantity for item in self.cart_items)

    def get_cost_of_cart(self) -> float:
        """ Return total cost of items."""
        return sum(float(item.print_item_cost(print_output=False)) for item in self.cart_items)

    def print_total(self):
        """ Printing total number of items and price."""
        if not self.cart_items:
            print('SHOPPING CART IS EMPTY.')
        else:
            print(f'{self.customer_name}\'s Shopping Cart -{self.current_date}',  
                f'\nNumber of Items: {self.get_num_items_in_cart()}')
            for item in self.cart_items:                 
                print(f"{item.item_name.title()} {item.item_quantity} @ ${item.item_price:.2f} = ${item.item_quantity*item.item_price:.2f}")
            print(f'Total: ${self.get_cost_of_cart():.2f}\n')
            
        
    def print_descriptions(self):
        """ Printing distinct item description of the class instance, removing duplicates."""
        if not self.cart_items:
            print('SHOPPING CART IS EMPTY.')
        else:
            print(f'{self.customer_name}\'s Shopping Cart -{self.current_date}', 
            '\nItem Descriptions')
            distinct_descriptions = {(item.item_name.title(), item.item_description.capitalize()) for item in self.cart_items}
            for name, description in distinct_descriptions:  
                print(f"{name}: {description}" )
        print()

# Stand-alone function
def print_menu(cart):
    menuDictionary={'a':'Add item to cart','r':'Remove item from cart',
                    'c':'Change item quantity','i':'Output items\' descriptions',
                    'o':'Output shopping cart','q':'Quit'} 

    while True:
        print(  '-'*15,'\nMENU')
        for key, value in menuDictionary.items():
            print(f'{key} - {value}' ) 
        try:
            
            option=input('Choose an option: ').strip().lower()
            if option in menuDictionary:
                print(f'You have chosen {option}: {menuDictionary[option]}')
                if option =='q':
                    print('Quit menu', '\nThank you for shopping with us. Have a great day!',"\U0001F6D2","\U0001F600") #add smiling emoji
                    return None #return None
                elif option =='a':
                    item1=get_item()
                    cart.add_item(item1)
                
                elif option =='r':
                    try:
                        itemToRemove = input('Input item name to remove: ').strip()
                    except ValueError:
                        print('Input value error')
                    cart.remove_item(itemToRemove)

                elif option =='c':
                    print("CHANGE ITEM QUANTITY")
                    try:
                        item = input('Input item name to modify quantity: ').strip()
                        quantity = int(input('Input item quantity: '))
                    except ValueError:
                        print('Input value error')
                     
                    for i in cart.cart_items:
                        if i.item_name.lower()==item.lower():
                            item_to_edit=ItemToPurchase(item_name=item, item_price=i.item_price, 
                                                        item_quantity=quantity, item_description=i.item_description)
                            # maintain the price and item description and update only quantity if item name matches cart items.
                            cart.modify_item(item_to_edit)
                             
                            print (f'{i.item_name.title()} quantity is updated to: {quantity}')

                elif option =='i':
                    cart.print_descriptions()
                
                elif option =='o':
                    cart.print_total()
            else:
                print('Option not in the menu. Please choose from the menu list.')
                continue
        except ValueError as e:
            print(e)

# Stand-alone functions
def customerInfo():
    """Helper function to validate customer name and date entries. Use default date if date fails to validate."""

    try:
        customer_name = input("Enter customer's name: ").strip()
        if not customer_name:
            raise ValueError('Name input cannot be blank.')
        
        date_input = input("Enter today's date in the format July 01, 2024: ").strip()
        date = date_input if date_input else datetime.now().strftime("%B %d, %Y")

        # if not date_input:
        #     date_input=datetime.now().strftime("%B %d, %Y") 

        # date = parser.parse(date_input).strftime("%B %d, %Y")
        # if pd.to_datetime(date) > datetime.now():
        #     date= datetime.now().strftime("%B %d, %Y")
        #     print('You have entered a date in the future. Using current date instead.') 

        print(f'Customer name: {customer_name}')
        print(f'Customer input date: {date}')
        return customer_name, date
        # correct = input('Are the name and date correct? Y/N: ')
        # if correct.strip().upper() == 'Y':
        #     return customer_name, date
        # elif correct.strip().upper() == 'N':
        #     continue
        # else:
        #     print("Invalid input. Please enter 'Y' or 'N'.")
    except Exception:
        print("Using current date.")
        date = datetime.now().strftime("%B %d, %Y")
        print(f'Customer name: {customer_name}')
        print(f'Today\'s date: {date}')
        return customer_name, date

def main(num_item=2): # pass parameter for different number of items.
    #step 1 see ItemToPurchase class
    #step 2 prompt the user for two items
    print('Let\'s build our shopping cart!',"\U0001F6D2","\U0001F600") #add emoji for good customer experience.
    objectCollection = [get_item() for _ in range(num_item)]
    
    #step 3 Add the costs of the two items together and output the total cost.
    print("\nTOTAL COST")
    total = sum(item_obj.print_item_cost() for item_obj in objectCollection)
    print(f"Total: ${total:.2f}\n")

    #Step 4 see ShoppingCart class
    # Step 7:prompt the user for a customer's name and today's date. Output the name and date. Create an object of type ShoppingCart. 
    customer_name,date=customerInfo()
    cart = ShoppingCart(customer_name,date)

    # Adding the above two items to the shopping cart instance.   
    for item in objectCollection:
        cart.add_item(item )
    
    #Step 5  # Step 8 -10
    print_menu(cart)

    #Step 6 Implement Output shopping cart menu option.  
    print("-" * 20)
    print('\nOUTPUT SHOPPING CART',"\U0001F6D2")
    cart.print_total()
    
    #Step 6 Implement Output item's description menu option.
    print("-" * 20 ,"\U0001F6D2")
    print('\nOUTPUT ITEMS\' DESCRIPTIONS')
    cart.print_descriptions()

if __name__ == "__main__": main()