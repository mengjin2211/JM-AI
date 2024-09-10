class ATM:
    def __init__(self):
        self.pin_attempts = 0
        self.max_attempts = 3

    def initiate(self):
        
        print("ATM Operation:\n",'*'*10)
        self.idle_state()

    def idle_state(self):
        self.pin_attempts=0
        print("\n1. Idle: Waiting for card insertion or exit")
        action = input("   Insert card or exit? (insert/exit): ").lower()
        if action == "exit":
            print("Exit")
            return "exit"
        elif action == "insert":
            print("2. Card Inserted")
            return self.card_inserted_state()
        else:
            print("Invalid input. Please try again.")
            return self.idle_state() 

    def card_inserted_state(self):
        print("3. Authenticating: Enter PIN")
        while self.pin_attempts <= self.max_attempts:
            pin_correct = input("   Is PIN correct? (y/n): ").lower() == 'y'
            if pin_correct:
                print("4. PIN Authenticated")
                self.authenticated_state()
                return
            else:
                self.pin_attempts += 1
                remaining_attempts = self.max_attempts - self.pin_attempts
                print(f"   Incorrect PIN. Attempt {self.pin_attempts}/{self.max_attempts}. {remaining_attempts} attempt(s) remaining.")

        print("5. PIN Rejected: Exceeded maximum attempts")
        print("6. Card Locked")
        self.idle_state()
        

    def authenticated_state(self):
        print("7. Select Option")
        print("8. Withdrawal selected")
        self.check_balance_state()

    def check_balance_state(self):
        print("9. Checking Balance")
        balance_sufficient = input("   Is balance sufficient? (y/n): ").lower() 
        if balance_sufficient == 'y':
            self.process_withdrawal_state()
        else:
            print("10. Insufficient Balance")
            self.account_closed_state()

    def process_withdrawal_state(self):
        print("11. Processing Withdrawal")
        print("12. Bill selection")
        print("13. Confirm button pressed")
        self.dispense_cash_state()

    def dispense_cash_state(self):
        print("14. Dispensing Cash")
        print("15. Take Cash")
        self.update_balance_state()

    def update_balance_state(self):
        print("16. Updating Balance.")
        print("Transaction Complete. Return to idle state.")
        self.idle_state()

    def account_closed_state(self):
        print("17. Account Closed")
        print("18. Transaction Complete")
        print("18. Transaction Complete")
        print("19. Ejecting Card")
        self.idle_state()

if __name__ == "__main__":
    atm = ATM()
    atm.initiate()