# Accept a string how many times each character is occurring
count = 0
st = input("Enter a name :")
for c in st:
    if c.count('C'):
        count += 1
print(count)
