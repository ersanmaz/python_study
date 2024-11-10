class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class SalaryEmployee(Employee):
    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name)
        self.salary = salary

    def calculate_paycheck(self):
        return self.salary/52
    
class HourlyEmployee(Employee):
    def __init__(self, first_name, last_name, hourly_rate):
        super().__init__(first_name, last_name)
        self.hourly_rate = hourly_rate

    def calculate_paycheck(self):
        return self.hourly_rate * 40
    
class CommissionEmployee(SalaryEmployee):
    def __init__(self, first_name, last_name, salary, commission):
        super().__init__(first_name, last_name, salary)
        self.commission = commission

    def calculate_paycheck(self):
        return super().calculate_paycheck() + self.commission