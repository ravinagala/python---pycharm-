# Give a discount of 10% substract that from amount and print

price = int(input("Enter price :"))
qty = int(input("Enter qty :"))

amount = price * qty
discount = amount * 0.10
net_amount = amount - discount
print("Net Amount =", net_amount)
