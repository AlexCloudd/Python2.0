class Users:
    def __init__(self, username, password, role, subscription_type = None, history = None, created_at = None ):
        self.username = username
        self.password = password
        self.role = role
        self.subscription_type = subscription_type
        self.history = history if history else []
        self.created_at = created_at
        