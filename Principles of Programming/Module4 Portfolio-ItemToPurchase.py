
# Build ItemToPurchase class with attributes and methods. 

class ItemToPurchase:
    def __init__(self,item_name='',item_price=0,item_quantity=0):
        self.item_name = str(item_name)   
        self.item_price = float(item_price)  
        self.item_quantity = int(item_quantity)   
    # calculate price. 
    def print_item_cost (self):
        price=self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${price:.2f}")
        return price
    # make the class object iterable
    def __iter__(self):
        return iter([self.item_name, self.item_price, self.item_quantity])

# create get_item function to prompt input. Use input to create class instance.         
def get_item():
    while True:
        try:
            item_name=input("Enter the item name: ")
            item_price=float(input("Enter the item price: "))
            item_quantity=int(input("Enter the item quantity: "))
            return ItemToPurchase(item_name, item_price, item_quantity)
        
        except ValueError as e:
            print ("Invalid Input.",
                '\n',
                "Item name only in text; item price fload; item quality integer.",
                '\n',"Error Message: ",str(e))
            continue

# main function loops num_item (parameter) times, get instances and print prices.
# n as input parameter. This will allow user to reuse the code and modify the number of items.
def main(num_item):
    total=0
    objectCollection=[]
    for i in range (num_item):
        item_details = get_item()
        objectCollection.append(item_details)
    
    print ("TOTAL COST")
    for item_obj in objectCollection:
        total+=item_obj.print_item_cost()
 
    print (f"Total: ${total}" )

if __name__ == "__main__": 
    while True:
        try:
            num_items = int(input("Enter the number of items in integer: "))
            break
        except ValueError as e:
            print("Invalid Value. Integer only.")
            continue    
    main(num_items)

    


        




    