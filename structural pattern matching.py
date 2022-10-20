# Accept a month and display how many days with year
month = int(input("Enter the month :"))
match month:
    case 2:
        year = int(input("Enter the year :"))
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            print(29)
        else:
            print(28)
    case 4 | 6 | 9 | 11:
        print(30)
    case _:
        print(31)
