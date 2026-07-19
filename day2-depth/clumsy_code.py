def generate_report(file_name, department=None, result=[]):
    file = open(file_name)

    data = file.readlines()

    total_salary = 0
    employee_count = 0

    highest_salary = 0
    highest_employee = ""

    report = {}

    for line in data:

        line = line.strip()

        if line != "":

            parts = line.split(",")

            if len(parts) == 3:

                name = parts[0]
                dept = parts[1]
                salary = int(parts[2])

                if department is None:

                    total_salary += salary
                    employee_count += 1

                    if salary > highest_salary:
                        highest_salary = salary
                        highest_employee = name

                    if dept in report:
                        report[dept].append(name)
                    else:
                        report[dept] = [name]

                else:

                    if dept == department:

                        total_salary += salary
                        employee_count += 1

                        if salary > highest_salary:
                            highest_salary = salary
                            highest_employee = name

                        if dept in report:
                            report[dept].append(name)
                        else:
                            report[dept] = [name]

    file.close()

    if employee_count > 0:
        average = total_salary / employee_count
    else:
        average = 0

    result.append({
        "average_salary": average,
        "highest_paid": highest_employee,
        "departments": report
    })

    print(result)

generate_report("employees.txt","HR")