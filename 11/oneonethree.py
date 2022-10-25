"""
11-3. Employee: Write a class called Employee. The __init__() method should
take in a first name, a last name, and an annual salary, and store each of these
as attributes. Write a method called give_raise() that adds $5,000 to the
annual salary by default but also accepts a different raise amount.
Write a test case for Employee. Write two test methods, test_give_default
_raise() and test_give_custom_raise(). Use the setUp() method so you don’t
have to create a new employee instance in each test method. Run your test
case, and make sure both tests pass.
"""

class Employee:
    def __init__(self, fname, lname, salary):
        """Store first name, last name, and salary"""
        self.fname = fname
        self.lname = lname
        self.salary = salary
    
    def name_employee(self):
        """Print name and current salary of employee"""
        print(f"{self.fname.title()}, {self.lname.title()} {self.salary}")
        return f"{self.fname.title()}, {self.lname.title()} {self.salary}"
    
    def give_raise(self, sraise=5000):
        """Add 5000 to salary by default"""
        self.salary = self.salary + sraise
