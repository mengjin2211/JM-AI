
"""Apply a “stepwise refinement approach” to develop check writer that converts a numeric dollar amount into words """
class CheckWriter:
    def __init__(self): 
        self.input_handler = InputAmount() # Composition: CheckWriter has an InputAmount
        self.converter = Converter() # Composition: CheckWriter has an Converter
        self.printer = Printer()# Composition: CheckWriter has an Printer

    def write(self):
       """1. Input dollar amount
        2. Convert amount to words
        3. Print check"""
       Amount=self.input_handler.input_amt()
       ConvertedAmt=self.converter.to_words(Amount)
       printout=self.printer.print_ck(ConvertedAmt)
       return printout
       
class InputAmount:
    def input_amt(self):
        """ 1. Prompt user for input
            1.1. Validate input
            1.2  Loop back till valid input is returned
        """
        while True:
            try:
                dollarAmt=round(float(input("Enter the dollar amount: ")),2)
                if dollarAmt>0:
                    return dollarAmt
                else:
                    raise ValueError ('Dollar amount cannot be negative.')
            except ValueError as e:
                print(e,'\nEnter a valid numeric dollar amount.')
                continue

class Converter:
    def to_words(self, amount):
        """
        1. Convert dollar to words 
        1.1 convert_hundres()
        1.2 convert_thousands()
        2. Convert cents to words
        """
        units = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        def convert_hundreds(amount):
            if amount < 10:
                return units[amount]
            elif amount < 20:
                return teens[amount - 10]
            elif amount < 100:
                return tens[amount // 10] + (" " + units[amount % 10] if amount % 10 != 0 else "")
            elif amount <1000:
                return units[amount  // 100] + " Hundred" + (" " + convert_hundreds(amount % 100) if amount % 100 != 0 else "")  
             
        def convert_thousands(amount):
            if amount < 1000:
                return convert_hundreds(amount)
            elif amount < 1000000:
                return convert_hundreds(amount // 1000) + " Thousand" + (" " + convert_hundreds(amount % 1000) if amount % 1000 != 0 else "")
            elif amount < 1000000000: 
                return convert_thousands(amount // 1000000) + " Million" + (" " + convert_thousands(amount % 1000000) if amount % 1000000 != 0 else "")
            else:
                return 'Amount is too big for a cheque. Please use wire-transfer instead.'  

        dollars = int(amount)
        cents = int(round((amount - dollars) * 100))
        result = convert_thousands(dollars) + " Dollars"
        result += ((" and " + convert_hundreds(cents) + " Cents") if cents > 0 else "")
        return result

class Printer:
    def print_ck(self, amount_in_words):
        """1. Format check text
        2. Output formatted text"""
        printout=print(amount_in_words)
        return printout
    
if __name__=="__main__":
    CheckWriter().write()