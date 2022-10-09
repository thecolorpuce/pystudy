import my_users

class Privileges:
    """An attempt to model privilege levels"""
    
    def __init__(self):
        """Initialize privilege attributes"""
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    
    def show_privileges(self):
        for i in self.privileges:
            print(f"{i}")

class Admin(my_users.User):
    def __init__(self, first_name, last_name, address, age):
        """Initialize the admin userInerit the items from User"""
        
        super().__init__(first_name, last_name, address, age)
        self.privileges = Privileges()
