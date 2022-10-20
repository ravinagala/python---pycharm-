# Accept a number and display the sum of factors and if there are no factors other than one and itself display prime number

num = int(input("Enter the number :"))
sum = 0
for i in range(2, num // 2 + 1):
    if num % i == 0:
        sum = 0 + 1
        print("Not a prime number")
        break
else:
    print("Prime number")

print("Done")
