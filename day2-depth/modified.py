from functools import wraps

def load_function(fun):
    @wraps(fun) #this helps in preserving meta data
    def wrapper(*args,**kwargs):
        print(f"{fun.__name__} is starting")
        return fun(*args,**kwargs)
    return wrapper

def division(fun):
    def wrapper(a,b):
        if(b==0):
            raise ValueError("There is no employee in this department")
        return fun(a,b)
    return wrapper

def load_employee(file_name):
    with open(file_name,"r") as file:
        return file.readlines()

def parse_employee(file):
    employee_list = []
    for line in file:
        temp = line.strip().split(",")
        temp[2]=int(temp[2])
        employee_list.append(temp)
    return employee_list
    
def group_by(employee_list,Role):
    return [employee for employee in employee_list if employee[1]==Role]

@load_function
def total_salary(employee_list):
    total = sum(temp[2] for temp in employee_list)
    return total

@division
def average_salary(total,count):
    return total/count

def highest_salary(employees):
    if not employees:
        return None
    return max(employees, key=lambda emp: emp[2])

def display(employees, salary_total, salary_avg, highest_sal):
    print("List of employees \n")
    print(employees)
    print("\n")
    print(f"total salary is {salary_total}\n")
    print(f"average salary is {salary_avg}\n")
    print(f"highest salary is {highest_sal}\n")

def generate_report(file_name,*,department=None):
    
    file = load_employee(file_name)
    employee_list = parse_employee(file)
    employees = group_by(employee_list,department)

    """computing total salary for seperate department"""
    salary_total = total_salary(employees)
    
    """computing avg salaries for seperate departments"""
    salary_avg = average_salary(salary_total, len(employees))
    
    highest_sal = highest_salary(employees)
    display(employees, salary_total, salary_avg, highest_sal)

generate_report("employees.txt",department="HR")
generate_report("employees.txt",department="IT")
generate_report("employees.txt",department="Sales")