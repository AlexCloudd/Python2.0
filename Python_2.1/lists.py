from working_file import FileManager

class Lists:
    def __init__(self):
        self.file_manager = FileManager()  
        self.__users = self.file_manager.import_users()
        self.__services = self.file_manager.import_services()

        if not self.__users:
            self.__users = [
                {'username': 'alex_user', 'password': 'password123', 'role': 'user', 'subscription_type': 'Premium', 'history': [], 'created_at': '2024-01-15'},
                {'username': 'admin_user', 'password': 'adminpass', 'role': 'admin', 'subscription_type': '', 'history': [], 'created_at': '2024-01-10'}
            ]
            self.__save_users()

        if not self.__services:
            self.__services = [
                {'name': 'Йога', 'price': 1000, 'duration': 60, 'popularity': 5},
                {'name': 'Силовая тренировка', 'price': 1200, 'duration': 90, 'popularity': 4},
                {'name': 'Плавание', 'price': 800, 'duration': 60, 'popularity': 3}
            ]
            self.__save_services()

    @property
    def users(self):
        return self.__users

    @property
    def services(self):
        return self.__services

    def add_user(self, user):
        self.__users.append(user)
        self.__save_users()

    def add_service(self, service):
        self.__services.append(service)
        self.__save_services()

    def __save_users(self):
        self.file_manager.export_users(self.__users)

    def __save_services(self):
        self.file_manager.export_services(self.__services)
