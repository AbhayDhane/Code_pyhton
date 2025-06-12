# Base class representing a general Bank Account
class BankAccount:
    def __init__(self, account_number, holder_name, initial_balance):
        self.account_number = account_number       # Public attribute
        self._holder_name = holder_name            # Protected attribute (accessible in subclass)
        self.__balance = initial_balance           # Private attribute (encapsulated)

    # Method to deposit money into the account
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited. New balance: ₹{self.__balance}")
        else:
            print("Invalid deposit amount.")  # Error message for invalid amount

    # Method to withdraw money from the account
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} withdrawn. Remaining balance: ₹{self.__balance}")
        else:
            print("Insufficient balance or invalid amount.")  # Error for low balance or invalid input

    # Getter method to access private balance
    def get_balance(self):
        return self.__balance

    # Protected method to display the account holder's name
    def _display_holder(self):
        print(f"Account holder: {self._holder_name}")


# Subclass representing a Savings Account with added interest feature
class SavingsAccount(BankAccount):
    def __init__(self, account_number, holder_name, initial_balance, interest_rate):
        # Initialize base class using super()
        super().__init__(account_number, holder_name, initial_balance)
        self.interest_rate = interest_rate  # Public attribute to store interest rate

    # Method to apply interest to the account balance
    def apply_interest(self):
        interest = self.get_balance() * (self.interest_rate / 100)  # Calculate interest
        print(f"Applying interest: ₹{interest}")
        self.deposit(interest)  # Add interest to the balance

    # Method to display full account information
    def display_info(self):
        self._display_holder()  # Accessing protected method from parent class
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ₹{self.get_balance()}")
        print(f"Interest Rate: {self.interest_rate}%")


# --- Usage Example ---

# Create an object of SavingsAccount
acc = SavingsAccount("1234567890", "Amit Verma", 10000, 4.5)

# Display account details
acc.display_info()

# Deposit money
acc.deposit(5000)

# Withdraw money
acc.withdraw(3000)

# Apply interest to current balance
acc.apply_interest()

# Trying to access private attribute directly (will cause error)
# print(acc.__balance)  # ❌ Not allowed, as __balance is private

# Accessing private attribute using name mangling (not recommended)
print("Accessing private balance using name mangling:", acc._BankAccount__balance)
