class Account:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return False
        self.balance += amount
        print(f"Deposited {amount} into account {self.account_number}. New balance is {self.balance}.")
        return True
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount > self.balance:
            print(f"Insufficient funds. Current balance is {self.balance}.")
            return False
        self.balance -= amount
        print(f"Withdrew {amount} from account {self.account_number}. New balance is {self.balance}.")
        return True
    
    def get_balance(self):
        print(f"Account {self.account_number} has balance: {self.balance}")
        return self.balance

# Create an Account instance before starting the loop
account = Account(account_number="123456", balance=4000000) 

def main():
    print("Welcome to the Banking System!")
    print("Available actions: deposit, withdraw, balance, exit")
    
    while True:
        try:
            action = input("\nEnter action (deposit, withdraw, balance, exit): ").lower().strip()
            
            if action == "deposit":
                try:
                    amount = float(input("Enter amount to deposit: $"))
                    account.deposit(amount)
                except ValueError:
                    print("Please enter a valid number.")
            
            elif action == "withdraw":
                try:
                    amount = float(input("Enter amount to withdraw: $"))
                    account.withdraw(amount)
                except ValueError:
                    print("Please enter a valid number.")
            
            elif action == "balance":
                account.get_balance()
            
            elif action == "exit":
                print("Thank you for using the Banking System. Goodbye!")
                break
            
            else:
                print("Invalid action. Please choose: deposit, withdraw, balance, or exit")
        
        except KeyboardInterrupt:
            print("\n\nExiting...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

# Run the program
if __name__ == "__main__":
    main()
