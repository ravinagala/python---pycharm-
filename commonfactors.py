# Accept two numbers and display common factors

n1 = int(input("Enter first number :"))
n2 = int(input("Enter second number :"))
for i in range(2, n1 and n2 // 2):
    if n1 % i == 0 and n2 % i == 0:
        print("CommonFactors =", i)
