class FileManager:
    def __init__(self, user_file="users.txt", service_file="services.txt"):
        self.user_file = user_file
        self.service_file = service_file

    def import_users(self):
        users = []
        try:
            with open(self.user_file, "r", encoding="utf-8") as file:
                for line in file:
                    parts = line.strip().split(":")
                    if len(parts) == 6:
                        username, password, role, subscription_type, history, created_at = parts
                        history = history.split(",") if history else []
                        user = {
                            'username': username,
                            'password': password,
                            'role': role,
                            'subscription_type': subscription_type,
                            'history': history,
                            'created_at': created_at
                        }
                        users.append(user)
            return users
        except FileNotFoundError:
            print(f"Файл {self.user_file} не найден. Создан новый пустой список пользователей.")
            return []
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            return []

    def export_users(self, users):
        try:
            with open(self.user_file, "w", encoding="utf-8") as file:
                for user in users:
                    history_str = ",".join(user['history']) if user['history'] else ""
                    file.write(f"{user['username']}:{user['password']}:{user['role']}:{user['subscription_type']}:{history_str}:{user['created_at']}\n")
            print(f"Пользователи успешно экспортированы в файл {self.user_file}.")
        except Exception as e:
            print(f"Ошибка при экспорте пользователей: {e}")

    def import_services(self):
        services = []
        try:
            with open(self.service_file, "r", encoding="utf-8") as file:
                for line in file:
                    parts = line.strip().split(":")
                    if len(parts) == 4:
                        name, price, duration, popularity = parts
                        service = {
                            'name': name,
                            'price': int(price),
                            'duration': int(duration),
                            'popularity': int(popularity)
                        }
                        services.append(service)
            return services
        except FileNotFoundError:
            print(f"Файл {self.service_file} не найден. Создан новый пустой список услуг.")
            return []
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            return []

    def export_services(self, services):
        try:
            with open(self.service_file, "w", encoding="utf-8") as file:
                for service in services:
                    file.write(f"{service['name']}:{service['price']}:{service['duration']}:{service['popularity']}\n")
            print(f"Услуги успешно экспортированы в файл {self.service_file}.")
        except Exception as e:
            print(f"Ошибка при экспорте услуг: {e}")
