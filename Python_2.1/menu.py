from working_file import FileManager  
from abc import ABC, abstractmethod

class TextOutput(ABC):
    @abstractmethod
    def display_text(self, text: str):
        pass

class UserTextOutput(TextOutput):
    def display_text(self, text: str):
        print(f"Пользовательский вывод: {text}")

class AdminTextOutput(TextOutput):
    def display_text(self, text: str):
        print(f"Административный вывод: {text}")

class Menu:
    def __init__(self, user, services, text_output: TextOutput):
        self.user = user
        self.services = services
        self.text_output = text_output
        self.file_manager = FileManager()  
    def display_services(self):
        try:
            for i, service in enumerate(self.services, start=1):
                self.text_output.display_text(f"{i}. {service['name']} | Цена: {service['price']} | Время: {service['duration']} мин | Популярность: {service['popularity']}")
        except KeyError as e:
            self.text_output.display_text(f"Ошибка: отсутствует ключ в словаре услуг: {e}")
        except Exception as e:
            self.text_output.display_text(f"Ошибка при отображении услуг: {e}")

    def sort_services_by_price(self):
        try:
            sorted_services = sorted(self.services, key=lambda x: x['price'])
            self.services.clear()
            self.services.extend(sorted_services)
            self.display_services()
        except KeyError as e:
            self.text_output.display_text(f"Ошибка: отсутствует ключ 'price' в словаре услуг: {e}")
        except Exception as e:
            self.text_output.display_text(f"Ошибка при сортировке по цене: {e}")

    def sort_services_by_popularity(self):
        try:
            sorted_services = sorted(self.services, key=lambda x: x['popularity'], reverse=True)
            self.services.clear()
            self.services.extend(sorted_services)
            self.display_services()
        except KeyError as e:
            self.text_output.display_text(f"Ошибка: отсутствует ключ 'popularity' в словаре услуг: {e}")
        except Exception as e:
            self.text_output.display_text(f"Ошибка при сортировке по популярности: {e}")

    def new_password(self):
        try:
            new_password = input("Введите новый пароль: ")
            self.user['password'] = new_password
            self.text_output.display_text("Пароль успешно изменен!")
        except Exception as e:
            self.text_output.display_text(f"Ошибка при изменении пароля: {e}")

    def map_services_price_in_euros(self, exchange_rate=0.011):
        try:
            converted_services = [
                {
                    'name': service['name'],
                    'price': round(service['price'] * exchange_rate, 2),
                    'duration': service['duration'],
                    'popularity': service['popularity']
                }
                for service in self.services
            ]
            self.services.clear()
            self.services.extend(converted_services)
            self.display_services()
        except KeyError as e:
            self.text_output.display_text(f"Ошибка: отсутствует ключ в словаре услуг: {e}")
        except Exception as e:
            self.text_output.display_text(f"Ошибка при конвертации цен: {e}")

class UserMenu(Menu):
    def display_services(self):
        self.text_output.display_text("Доступные услуги для пользователя:")
        super().display_services()

class AdminMenu(Menu):
    def __init__(self, admin, services, users, text_output: TextOutput):
        super().__init__(admin, services, text_output)
        self.users = users
        self.file_manager = FileManager()  

    def new_service(self):
        try:
            name = input("Введите название услуги: ")
            price = int(input("Введите цену: "))
            duration = int(input("Введите продолжительность (в минутах): "))
            popularity = int(input("Введите популярность: "))
            new_service = {'name': name, 'price': price, 'duration': duration, 'popularity': popularity}
            self.services.append(new_service)
            self.file_manager.export_services(self.services)  
            self.text_output.display_text("Услуга успешно добавлена.")
        except ValueError:
            self.text_output.display_text("Ошибка: введите корректные числовые значения.")
        except Exception as e:
            self.text_output.display_text(f"Ошибка при добавлении услуги: {e}")

    def delete_service(self):
        try:
            name = input("Введите название услуги для удаления: ")
            service_to_delete = next((s for s in self.services if s['name'] == name), None)
            if service_to_delete:
                self.services.remove(service_to_delete)
                self.file_manager.export_services(self.services)  
                self.text_output.display_text(f"Услуга '{name}' успешно удалена.")
            else:
                self.text_output.display_text("Услуга не найдена.")
        except Exception as e:
            self.text_output.display_text(f"Ошибка при удалении услуги: {e}")

    def edit_service(self):
        try:
            name = input("Введите название услуги для редактирования: ")
            service_to_edit = next((s for s in self.services if s['name'] == name), None)
            if service_to_edit:
                new_price = int(input("Введите новую цену: "))
                new_duration = int(input("Введите новую продолжительность: "))
                new_popularity = int(input("Введите новую популярность: "))
                service_to_edit['price'] = new_price
                service_to_edit['duration'] = new_duration
                service_to_edit['popularity'] = new_popularity
                self.file_manager.export_services(self.services)  
                self.text_output.display_text(f"Услуга '{name}' успешно обновлена.")
            else:
                self.text_output.display_text("Услуга не найдена.")
        except ValueError:
            self.text_output.display_text("Ошибка: введите корректные числовые значения.")
        except Exception as e:
            self.text_output.display_text(f"Ошибка при редактировании услуги: {e}")

    def static_service(self):
        try:
            total_services = len(self.services)
            total_price = sum(service['price'] for service in self.services)
            average_price = total_price / total_services if total_services > 0 else 0
            most_popular_service = max(self.services, key=lambda x: x['popularity'])
            self.text_output.display_text(f"Всего услуг: {total_services}")
            self.text_output.display_text(f"Средняя цена услуги: {average_price:.2f}")
            self.text_output.display_text(f"Самая популярная услуга: {most_popular_service['name']} (популярность: {most_popular_service['popularity']})")
        except Exception as e:
            self.text_output.display_text(f"Ошибка при выводе статистики: {e}")

    def manage_users(self):
        "Управление пользователями для администратора"
        try:
            while True:
                self.text_output.display_text("\nУправление пользователями:")
                self.text_output.display_text("1. Создать пользователя")
                self.text_output.display_text("2. Удалить пользователя")
                self.text_output.display_text("3. Редактировать пользователя")
                self.text_output.display_text("4. Вернуться в меню администратора")

                choice = input("Введите номер действия: ")
                if choice == '1':
                    username = input("Введите имя пользователя: ")
                    password = input("Введите пароль: ")
                    role = input("Введите роль (user/admin): ")
                    subscription_type = input("Введите тип подписки (если есть): ")
                    new_user = {
                        'username': username,
                        'password': password,
                        'role': role,
                        'subscription_type': subscription_type,
                        'history': [],
                        'created_at': '2024-01-01'
                    }
                    self.users.append(new_user)
                    self.file_manager.export_users(self.users)  
                    self.text_output.display_text(f"Пользователь {username} успешно создан.")
                elif choice == '2':
                    username = input("Введите имя пользователя для удаления: ")
                    user_to_delete = next((u for u in self.users if u['username'] == username), None)
                    if user_to_delete:
                        self.users.remove(user_to_delete)
                        self.file_manager.export_users(self.users)  
                        self.text_output.display_text(f"Пользователь {username} успешно удален.")
                    else:
                        self.text_output.display_text("Пользователь не найден.")
                elif choice == '3':
                    username = input("Введите имя пользователя для редактирования: ")
                    user_to_edit = next((u for u in self.users if u['username'] == username), None)
                    if user_to_edit:
                        new_password = input("Введите новый пароль: ")
                        new_role = input("Введите новую роль (user/admin): ")
                        new_subscription = input("Введите новый тип подписки: ")
                        user_to_edit['password'] = new_password
                        user_to_edit['role'] = new_role
                        user_to_edit['subscription_type'] = new_subscription
                        self.file_manager.export_users(self.users)  
                        self.text_output.display_text(f"Пользователь {username} успешно обновлен.")
                    else:
                        self.text_output.display_text("Пользователь не найден.")
                elif choice == '4':
                    break
                else:
                    self.text_output.display_text("Неверный ввод.")
        except Exception as e:
            self.text_output.display_text(f"Ошибка при управлении пользователями: {e}")
