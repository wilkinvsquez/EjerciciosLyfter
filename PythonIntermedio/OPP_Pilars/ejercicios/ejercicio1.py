class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def add_money(self, amount):
        self.balance += amount
        return self.balance

    def withdraw_money(self, amount):
        self.balance -= amount
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, balance, min_balance):
        super().__init__(balance)
        self.min_balance = min_balance

    def withdraw_money(self, amount):
        if self.balance - amount < self.min_balance:
            raise ValueError(f"El retiro dejaría el balance ({self.balance - amount}) por debajo del mínimo permitido ({self.min_balance})")
        return super().withdraw_money(amount)


acc = SavingsAccount(balance=100, min_balance=50)
acc.withdraw_money(40)
print(acc.balance)

acc.withdraw_money(10) 