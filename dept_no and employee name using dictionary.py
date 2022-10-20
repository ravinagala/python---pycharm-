# Accept input from user which is dept_no,employee names

data = ["1,BILL", "2,ELON", "3,LARRY", "1,SUNDAR", "2,SATYA", "3,PARAG"]
employees = {}
for entry in data:
    parts = entry.split(",")
    dept_no = int(parts[0])
    emp_names = parts[1]

    if dept_no in employees:
        employees[dept_no] = employees[dept_no], (emp_names)
    else:
        employees[dept_no] = emp_names

for dept_no, emp_names in employees.items():
    print(f'{dept_no}  {", ".join(emp_names)}')
