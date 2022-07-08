'''ALSO KNOWN AS GETTER AND SETTER'''

class Employee:
    company="Tata"
    salary=10000
    bonus=1000

    @property
    def totalSalary(self):
        return self.salary+self.bonus

    @totalSalary.setter
    def totalSalary(self,inp):
        self.bonus=inp-self.salary



mayank=Employee()
print(mayank.company)
print(mayank.totalSalary)
mayank.totalSalary=180000
print(mayank.bonus)
print(Employee.salary)