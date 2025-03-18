from flask_login import UserMixin
import uuid

class User(UserMixin):
    def __init__(self, first_name, last_name, email, password):
        self.user_id = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        
    def get_id(self):
        return self.user_id