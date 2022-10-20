# Accept 5 names from user and display unique characters
names = "roger, ronaldo, virat, tendulkar, rahul"
words = names.split(" ")
chars = set()
for n in names:
    chars = chars | set(n)
print(chars)