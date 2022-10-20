# Accept numbers until 0 is given and display the avg of integers without using continue statement

total = count = 0
while True:
    num = int(input("Enter number [0 to stop] :"))
    if num == 0:
        break
    total += num
    count += 1

print(total / count)