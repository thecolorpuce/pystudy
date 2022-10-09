"""
9-11. Imported Admin: Start with your work from Exercise 9-8 (page 173).
Store the classes User, Privileges, and Admin in one module. Create a sepa-
rate file, make an Admin instance, and call show_privileges() to show that
everything is working correctly.
"""

import my_users as MU

admin1 = MU.Admin('Riley', 'Abbs', '9 3/4', 28)
user1 = MU.User('Sam', 'Dbs', '123 Winchester', 18)

admin1.privileges.show_privileges()
user1.describe_user()
user1.greet_user()