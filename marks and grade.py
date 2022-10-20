# accept marks and display grade
marks = int(input("Enter marks :"))

if marks < 50:
    print("Fail")
elif 50 <= marks <= 60:
    print("Grade C")
elif 60 <= marks <= 80:
    print("Grade B")
else:
    print("Grade A")
print("Done")
