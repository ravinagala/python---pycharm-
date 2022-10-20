# Create withdraw method in account class
class Account:
    # Method
    def __init__(self, acno, ahname):
        # Object attribute
        self.acno = acno
        self.ahname = ahname
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def getbalance(self):
        return self.balance

    def __str__(self):
        return f"{self.acno} - {self.ahname} - {self.balance}"


a1 = Account(1, "Roberts")  # Object
a1.deposit(10000)
a1.deposit(20000)
a1.withdraw(8000)
print(a1.getbalance())
print(a1)

a2 = Account(2, "Ravi")
a2.deposit(50000)
a2.withdraw(35000)
print(a2.getbalance())
print(a2)