# Accept two strings and display the common characters between strings

str1 = input("Enter first string :")
str2 = input("Enter second string :")
s1 = set(str1)
s2 = set(str2)
print(s1 & s2)
