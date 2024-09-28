#d
from user import User

class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password, role="admin")

    def change_user_data(self, users, username, new_data):
        for user in users:
            if user['username'] == username:
                user.update(new_data)
                return True
        return False
