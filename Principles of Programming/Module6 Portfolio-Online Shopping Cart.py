#re-using the code from Module4
class ItemToPurchase:
    def __init__(self,item_name='',item_price=0,item_quantity=0,item_description=''):
        self.item_name = str(item_name)   
        self.item_price = float(item_price)  
        self.item_quantity = int(item_quantity)   
        self.item_description=str(item_description)
    # calculate price. 
    def item_cost (self):
        price=self.item_price * self.item_quantity
        #print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${price:.2f}")
        return price
    # make the class object iterable
    def __iter__(self):
        return iter([self.item_name, self.item_price, self.item_quantity])

#helper function to create ItemToPurchse class instance       
def get_item():
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
                '\n',
                "Item name only in text; item price fload; item quality integer; item description only in text.",
                '\n',"Error Message: ",str(e))
            continue

"""ShoppingCart class creation with attributes (customer_name, date and cart_items) 
and methods (add_item, remove_item, modify_item, get_num_items_in_cart, 
get_cost_of_cart, print_total, print_descriptions)"""

class ShoppingCart:
    def __init__(self,customer_name='none',date='January 1, 2020'):
        self.customer_name=str(customer_name)  
        self.date= str(date) 
        self.cart_items=[]
     
    def add_item(self,item_to_purchase):   # call get_item() as argument        
        self.cart_items.append(item_to_purchase)
        print(f'{item_to_purchase.item_name} has been added to your cart.')

    def remove_item(self, itemName):

        removed=[i for i in self.cart_items if i.item_name==itemName] 
        self.cart_items=[i for i in self.cart_items if i.item_name!=itemName]
        if removed:
            print('Item not found in cart. Nothing removed.')
        else:
            print(f'{itemName} removed.')
        
    def modify_item(self,item_to_purchase): # call get_item() as argument  
        found=False
        for item in self.cart_items:
            if item_to_purchase.item_name ==item.item_name:
                found=True
                if item_to_purchase.item_price!=0:
                    item.item_price=item_to_purchase.item_price
                if item_to_purchase.item_quantity!=0:
                    item.item_quantity=item_to_purchase.item_quantity
                if item_to_purchase.item_description!='':
                    item.item_description=item_to_purchase.item_description
        if not found: 
            print('Item not found in cart. Nothing modified.') 
            
    def get_num_items_in_cart(self) -> int:

        return sum(item.item_quantity for item in self.cart_items)

    def get_cost_of_cart(self) -> float:

        return sum(item.item_cost for item in self.cart_items)

    def print_total(self):
        if not self.cart_items:
            print('SHOPPING CART IS EMPTY.')
        else:
            print(f'{self.customer_name}\'s Shopping Cart -{self.date}',  
                f'\nNumber of Items: {self.get_num_items_in_cart()}')
            for item in self.cart_items:                 
                print(f"{item.item_name} {item.item_quantity} @ ${item.item_price:.2f} = ${item.item_quantity*item.item_price:.2f}")
            print(f'Total: ${self.get_cost_of_cart():.2f}')
            
        
    def print_descriptions(self):
        if not self.cart_items:
            print('SHOPPING CART IS EMPTY.')
        else:
            print(f'{self.customer_name}\'s Shopping Cart -{self.date}', 
            '\nItem Descriptions')
            for item in self.cart_items:  
                print(f"{item.item_name}: {item.item_description}" )

""" #testing the above
item1=get_item()
#item2=get_item()
item3=get_item()
cart = ShoppingCart('Jin','June 7 2024')
cart.add_item(item1)
#cart.add_item(item2)
cart.print_total()
cart.print_descriptions()
cart.modify_item(item3)
cart.print_total()
cart.print_descriptions()
cart.remove_item('Apple')
cart.print_total()
cart.print_descriptions()
"""
 
def print_menu(cart):
    menuDictionary={'a':'Add item to cart','r':'Remove item from cart',
                    'c':'Change item quantity','i':'Output items\' descriptions',
                    'o':'Output shopping cart','q':'Quit'}
    print(  'MENU')
    for key, value in menuDictionary.items():
            print(f'{key} - {value}' )    

    while True:
        try:
            option=str(input('Choose an option: '))
            if option in menuDictionary:
                print(f'You have chosen {option}: {menuDictionary[option]}')
                if option =='q':
                    print('Quit menu')
                    return None
                elif option =='a':
                    item1=get_item()
                    cart.add_item(item1)
                elif option =='r':
                    try:
                        itemToRemove = input('Input item name to remove: ')
                    except ValueError:
                        print('Input value error')
                    cart.remove_item(itemToRemove)

                elif option =='c':
                    try:
                        item = input('Input item name to modify quantity: ')
                        quantity = int(input('Input item quantity: '))
                    except ValueError:
                        print('Input value error')

                    found=False
                    for i in cart.cart_items:
                        if i.item_name==item:
                            i.item_quantity=quantity
                            print (f'{i.item_name} quantity is updated to: {quantity}')
                            found=True
                            break
                    if not found:
                        print('Item not found in cart. Quantity not changed.')

                elif option =='i':
                    cart.print_descriptions()
                elif option =='o':
                    cart.print_total()
            else:
                print('Option not in the menu. Please choose from the menu list.')
                continue
        except ValueError as e:
            print(e)


def main():
    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")
    cart = ShoppingCart(customer_name,current_date)
    print_menu(cart)
    print("-" * 20)
    print('OUTPUT SHOPPING CART')
    cart.print_total()
    print("-" * 20)
    print('OUTPUT ITEMS\' DESCRIPTIONS')
    cart.print_descriptions()

if __name__ == "__main__": main()