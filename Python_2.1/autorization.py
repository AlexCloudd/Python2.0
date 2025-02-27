from lists import Lists

class Autorization:
    def __init__(self):
            lists = Lists()
            self.users = lists.users 
            self.services = lists.services

    def login(self):
        try:
            username = input("Логин: ")
            password = input("Пароль: ")

            user = next((u for u in self.users if u.get('username') == username and u.get('password') == password), None)

            if user:
                print(f"Добро пожаловать, {user['username']}!")
                return user
            else:
                print("Неверный логин или пароль.")
                return None
        except Exception as e:
            print(f"Ошибка при входе в систему: {e}")
            return None
