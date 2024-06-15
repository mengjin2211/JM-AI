
#CSU Global Bookstore Monthly Credit Calculation 

def bookPurchased ():
    """Prompt user to input number of books purchased."""
    while True:
        try:
            number_book=int(input('Input the number of books the student purchased this month (positive integer): '))
            if number_book>=0:
                return number_book
                break
            else:
                print('You have entered negative number. Only positive integer number please.')
                continue
        except ValueError as e:
            print(e,'\n','Enter a valid positive integer number.')


def credit_cal ():
    """Evaludate book number in multi-way condition statement. 
    Pass value to credit variable. Return book number & credit."""
    books_purchased=bookPurchased ()
    credit=0 
    if 0<=books_purchased<2:
        pass
    elif 2<=books_purchased<4:
        credit=5
    elif 4<=books_purchased<6:
        credit=15   
    elif 6<=books_purchased<8:
        credit=30
    elif books_purchased>=8:
        credit=60

    return books_purchased, credit

if __name__ == "__main__": 
    books, cred=credit_cal()
    print (f'Number of books purchased this month: {books}\n'
        f'Credit(s) earned: {cred}')
     
