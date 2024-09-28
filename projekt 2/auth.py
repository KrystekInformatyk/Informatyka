import json
from data_manager import DataManager

class Auth:
    def __init__(self, users_file):
        self.data_manager = DataManager(users_file)
        self.users = self.data_manager.load_data()

    def login(self, username, password):
        for user in self.users:
            if user['username'] == username and user['password'] == password:
                return user
        return None
