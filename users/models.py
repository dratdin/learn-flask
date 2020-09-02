from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, data):
        self.id = data["_id"]
        self.email = data["email"]
        self.username = data["username"]
        self.password = data["password"]
