
class Employee:

  'Common base class for all employees'
  empCount = 0

  def __init__(self, name, salary):
    self.name = name
    self.salary = salary
    Employee.empCount += 1

  def displayCount(self):
    print 'Total employee: %d' % Employee.empCount

  def displayEmployee(self):
    print 'Employee %s, salary $%d' % (self.name, self.salary)

# print number of employees

def printEmployees():
  print 'Total of employees:', Employee.empCount

emp1 = Employee('Alex', 2000)
emp1.displayEmployee()
printEmployees()

emp2 = Employee('Valks', 5000)
emp2.displayEmployee()
printEmployees()

# attributes manipulation

emp1.age = 31
emp1.age = 32
del emp1.age

hasattr(emp1, 'age') # False
setattr(emp1, 'age', 40)
getattr(emp1, 'age') # 40
delattr(emp1, 'age')
