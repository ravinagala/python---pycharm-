# Display a message saying there are no common factors
num1, num2 = 20, 10
small = min(num1, num2)

for i in range(2, small // 2 + 1):
    if num1 % i == 0 and num2 % i == 0:
        print(i)
    else:
        "No common factors"
print("Done")
