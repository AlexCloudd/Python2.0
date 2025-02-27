from users import Users
class Admin(Users):
    def __init__(self, username, password, role, subscription_type=None, history=None, created_at=None):
        super().__init__(username, password, role, subscription_type, history, created_at)
    