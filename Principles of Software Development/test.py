"""Apply a “stepwise refinement approach” to develope check writer that converts a numeric dollar amount into words """
class CheckWriter:
    def __init__(self): 
        self.input_handler = InputAmount() # Composition: CheckWriter has an InputHandler
        self.amount_converter = Converter() # Composition: CheckWriter has an AmountConverter
        self.printer = Printer()# Composition: CheckWriter has an CheckPrinter

    def write(self):
       Amount=self.input_handler.input_amt()
       ConvertedAmt=self.amount_converter.to_words(Amount)
       printout=self.printer.print_ck(ConvertedAmt)
       return printout
       
class InputAmount:
    def input_amt(self):
        dollarAmt=float(input("Enter the dollar amount: "))
        return dollarAmt


class Converter:
    def to_words(self, amount):
        # Define word lists
        def convert_hundreds(amount):
            return "hundred and under converstion to be developed"
             
        def convert_thousands(amount):
            return amount//1000 + 'Thousand'+ convert_hundreds(amount%1000)
        result=convert_thousands(amount)
        return result

class Printer:
    def print_ck(self, ConvertedAmt):
        printout=print(ConvertedAmt)
        return printout
    
if __name__=="__main__":
    CheckWriter().write()