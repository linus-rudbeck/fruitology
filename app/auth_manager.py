import json
import bcrypt

class AuthManager:
    def __init__(self, users_file="users.json"):
        self.users_file = users_file

    def load_users(self):
        try:
            with open(self.users_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
        

    def save_users(self, users):
        with open(self.users_file, "w") as file:
            json.dump(users, file, indent=2)

    def register(self, username, password):
        users = self.load_users()
        if username in users:
            raise Exception("Användaren finns redan")
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode(), salt).decode()
        users[username] = hashed_password
        self.save_users(users)

    def login(self, username, password):
        users = self.load_users()
        saved_hash = users.get(username)

        if not saved_hash:
            raise Exception("Fel användaruppgifter")

        if not bcrypt.checkpw(password.encode(), saved_hash.encode()):
            raise Exception("Fel användaruppgifter")
