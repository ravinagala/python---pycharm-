# Accept a string and display whether it is a valid mobile number
st = "8328105727a"
if len(st) == 10 and st.isdigit():
    print("It is a valid number")
else:
    print("Not a valid mobile number")
print("Done")
