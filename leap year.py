# Accept a month and display how many days which includes whether it is a leap year

month = int(input("Enter the month :"))

if month == 2:
    year = int(input("Enter year :"))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(29)
    else:
        print(28)
elif month in [4, 6, 9, 11]:
    print(30)
else:
    print(31)
