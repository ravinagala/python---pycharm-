# Accept three numbers and display the largest of three numbers

n1 = int(input("Enter the first number :"))
n2 = int(input("Enter the second number :"))
n3 = int(input("Enter the third number :"))

if n1 > n2 and n1 > n3:
    print(n1, "is the largest number")
elif n2 > n3:
    print(n2, "is the largest number")
else:
    print(n3, "is the largest nummer")
print("Done")
