# Accept basic salary and display net salary by calculating hra@ 30% and da@ 20%

basic_salary = int(input("Enter basic salary :"))
house_rent_allowance = basic_salary * 0.30
dearness_allowance = basic_salary * 0.20
net_salary = basic_salary + house_rent_allowance + dearness_allowance

print(f"Basic Salary         {basic_salary:8.2f}")
print(f"House Rent Allowance {house_rent_allowance:8.2f}")
print(f"Dearness Allowance   {dearness_allowance:8.2f}")
print(f"Net Salary           {net_salary:8.2f}")
