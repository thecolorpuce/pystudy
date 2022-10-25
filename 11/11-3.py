from cgi import test
import oneonethree

test_employee = oneonethree.Employee('Riley', 'Abbs', 20000)

test_employee.name_employee()

test_employee.give_raise()

test_employee.name_employee()

test_employee.give_raise(20000)

test_employee.name_employee()

test_print = test_employee.name_employee()

print(f"This is a test: {test_print}")