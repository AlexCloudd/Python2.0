from functools import reduce
from lists import Lists
from menu import UserMenu, AdminMenu, UserTextOutput, AdminTextOutput

class Openning_menu:

    @staticmethod
    def user_menu(user):
        lists = Lists()  
        um = UserMenu(user, lists.services, UserTextOutput())  

        while True:
            print("\nВыберите действие:")
            print("1. Просмотреть доступные услуги")
            print("2. Посмотреть историю записей")
            print("3. Сортировать услуги по цене")
            print("4. Сортировать услуги по популярности")
            print("5. Преобразовать цену в евро")
            print("6. Изменить пароль")
            print("7. Выйти")

            choice = input("Введите номер действия: ")
            if choice == '1':
                um.display_services()
            elif choice == '2':
                print("История ваших записей:", ", ".join(user['history']))
            elif choice == '3':
                um.sort_services_by_price()
            elif choice == '4':
                um.sort_services_by_popularity()
            elif choice == '5':
                um.map_services_price_in_euros()
            elif choice == '6':
                um.new_password()
            elif choice == '7':
                break
            else:
                print("Неверный ввод.")

    @staticmethod
    def admin_menu(admin_user):
        lists = Lists() 
        am = AdminMenu(admin_user, lists.services, lists.users, AdminTextOutput())  

        while True:
            print("\nВыберите действие:")
            print("1. Добавить услугу")
            print("2. Удалить услугу")
            print("3. Редактировать услугу")
            print("4. Управление пользователями")
            print("5. Просмотр статистики")
            print("6. Выйти")

            choice = input("Введите номер действия: ")
            if choice == '1':
                am.new_service()
            elif choice == '2':
                am.delete_service()
            elif choice == '3':
                am.edit_service()
            elif choice == '4':
                am.manage_users()
            elif choice == '5':
                am.static_service()
            elif choice == '6':
                break
            else:
                print("Неверный ввод.")