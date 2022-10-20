# Accept a string and how many upper case letters the string contains
upper_case = 0
st = input("Enter name :")
for c in st:
    if c.isupper():
        upper_case += 1
print(f"Upper case letters :", c["UPPER_CASE"])
