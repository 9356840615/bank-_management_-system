class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} successfully.")
        else:
            print("Deposit amount should be greater than zero.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount} successfully.")
        else:
            print("Insufficient funds.")

    def transfer(self, amount, recipient_account):
        if 0 < amount <= self.balance:
            self.balance -= amount
            recipient_account.balance += amount
            print(f"Transferred {amount} successfully to account {recipient_account.account_number}.")
        else:
            print("Insufficient funds.")

    def view_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")


# Example usage
if __name__ == "__main__":
    # Creating accounts
    account1 = BankAccount("123456", "John Doe")
    account2 = BankAccount("654321", "Jane Doe")

    # Depositing funds
    account1.deposit(1000)
    account2.deposit(500)

    # Withdrawing funds
    account1.withdraw(200)
    account2.withdraw(100)

    # Transferring funds
    account1.transfer(300, account2)

    # Viewing balances
    account1.view_balance()
    account2.view_balance()
