class Bank:
    bank_name = "Default Bank"

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display(self):
        print(f"Account Holder: {self.account_holder}, Bank Name: {Bank.bank_name}")


# Creating instances
acc1 = Bank("Alice")
acc2 = Bank("Bob")

# Displaying initial bank names
acc1.display()
acc2.display()

# Changing bank name using class method
Bank.change_bank_name("Future Bank")

# Displaying bank names after the change
acc1.display()
acc2.display()
