employees = {
    "HR": [(101, 30000), (102, 32000)],
    "IT": [(201, 50000), (202, 55000)],
    "Sales": [(301, 40000), (302, 42000)]
}

for dept, records in employees.items():
    salaries = [sal for _, sal in records]
    print(f"{dept}: Min = {min(salaries)}, Max = {max(salaries)}")
