
from autorization import Autorization
from openning_menu import Openning_menu

def main():
    user = Autorization().login()
    if user:  
        if user['role'] == 'user': 
            Openning_menu.user_menu(user)  
        elif user['role'] == 'admin':
            Openning_menu.admin_menu(user)  

if __name__ == "__main__":
    main()