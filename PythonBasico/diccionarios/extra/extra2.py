def group_by_department(employees_list):
    result = {}
    for employee in employees_list:
        dept = employee['department']
        result.setdefault(dept, []).append(employee)
    return result



employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]
result = group_by_department(employees)
print(result)