# Create a class counter
class Counter:
    def __init__(self, value=1):
        self.value = value

    def increament(self, number):
        self.value += number

    def decreament(self, number):
        self.value -= number

    def getvalue(self):
        return self.getvalue

    def __str__(self):
        return f"{self.value}"


c = Counter(100)
c.increament(3)
c.decreament(2)
print(c.getvalue())
print(c)

c1 = Counter()
c1.increament(5)
c1.decreament(2)
print(c1.getvalue)
print(c1)