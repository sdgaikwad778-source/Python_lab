class UserManager():

    def __init__(self):
        self.users = []

    def create_user(self, name):
        user = {
            "name": name
        }

        self.users.append(user)


manager = UserManager()

manager.create_user("santosh")

print(manager.users)

