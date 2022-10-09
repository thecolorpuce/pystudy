"""
9-12. Multiple Modules: Store the User class in one module, and store the
Privileges and Admin classes in a separate module. In a separate file, create
an Admin instance and call show_privileges() to show that everything is still
working correctly.
"""

import my_admin as MA

admin1 = MA.Admin('riley', 'abbs', '123 Winchester Ave', 28)

admin1.privileges.show_privileges()