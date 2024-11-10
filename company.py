from employee import CommissionEmployee, Employee, HourlyEmployee, SalaryEmployee


class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_employees(self):
        for employee in self.employees:
            print(employee.first_name, employee.last_name)

    def pay_employees(self):
        for employee in self.employees:
            print('Paycheck for: ', employee.first_name, employee.last_name)
            print(f'Amount: ${employee.calculate_paycheck():,.2f}')
            print('----------------------------')

def main():
    company = Company()
    company.add_employee(SalaryEmployee('John', 'Doe', 50000))
    company.add_employee(HourlyEmployee('Jane', 'Doe', 50))
    company.add_employee(HourlyEmployee('Bob', 'Smith', 70))
    company.add_employee(CommissionEmployee('Jane', 'Smith', 45000, 7800))

    company.display_employees()

    company.pay_employees()

main()

s = """text"""

s.join()