# CRETE A CLASS EMPLOYEE AND USE SETTER TO INCREMENT THE SALARY ACCORDING TO BONUS
class Employee:
    company="Ford"
    salary=10000
    increment=1.3

    @property
    def totalSalary(self):
     return self.salary*self.increment

    @totalSalary.setter
    def totalSalary(self,inc):
      self.increment=inc/self.salary

a=Employee()
print(a.totalSalary)
a.totalSalary=122
print(a.increment)