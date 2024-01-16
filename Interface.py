"""
Позволяет зайти по логину-паролю или создать нового пользователя (а так же выйти из аккаунта)
Позволяет выбрать календарь, узнать ближайшие события, события из промежутка времени а так же
Создать событие или удалить событие
После создания события можно добавить туда пользователей
Если нас добавили в событие или удалили мы получаем уведомление.

в main можно использовать ТОЛЬКО interface
"""
import bcrypt
import sys
from Backend import Backend
from User import User

class Interface:
    user = None
    state = "start"
    backend = Backend()
    backend.load_data()
    
    
    @staticmethod
    def start():
        ret = input("""Начало работы
        0)Войти в аккаунт
        1)Создать нового пользователя
        2)Завершить работу
        """)
        if ret == "0":
            Interface.entrance()
        elif ret == "1":
            Interface.create_new_user()
        elif ret == "2":
            Interface.finish()
    def read():
        ret = input("""
        0)Завершить работу
        1)Создать событие
        2)Добавить в событие пользователей
        3)Удалить пользователей из события
        3)Удалить событие
        4)Просмотреть все свои события из промежутка времени
        """)
        if ret == "0":
            Interface.finish()
        elif ret == "1":
            pass
            
        
    
    # @staticmethod
    # def entrance():
    #     login = input("Введите свой логин: ")
    #     user_exists = False
    #     for user in Interface.backend.get_users():
    #         if user.get_name() == login:
    #             user_exists = True
    #             password = input("Введите пароль: ")
    #             print(f"Введенный пароль: {password}")
    #             print(f"Сохраненный хэш пароля: {user.get_password()}")
    #             if user.check_password(password):
    #                 print("Добро пожаловать")
    #             else:
    #                 print("Логин или пароль введены неверно, выполните вход заново")
    #                 Interface.start()
    #     if not user_exists:
    #         print("Пользователя не существует")
    #         Interface.entrance()
    @staticmethod
    def entrance():
        login = input("Введите свой логин: ")
        user_exists = False
        for user in Interface.backend.get_users():
            if user.get_name() == login:
                user_exists = True
                password = input("Введите пароль: ")
                print(f"Введенный пароль: {password}")
                print(f"Сохраненный хэш пароля: {user.get_password()}")
                if user.check_password(password):
                    print("Добро пожаловать")
                else:
                    print("Логин или пароль введены неверно, выполните вход заново")
                    Interface.start()
        if not user_exists:
            print("Пользователя не существует")
            Interface.entrance()
    @staticmethod
    def get_user_by_login(login):
        users = Interface.backend.get_users()
        for user_obj in users:
            if user_obj.get_name() == login:
                return user_obj
        return None
    @staticmethod
    def create_event():
        pass
    @staticmethod
    def add_user_in_event():
        pass
    @staticmethod
    def remove_user_from_event():
        pass
    @staticmethod
    def remove_event():
        pass
    @staticmethod
    def view_events():
        pass
    @staticmethod
    def create_new_user():
        new_user = User.create_user()
        Interface.backend.add_users(new_user)
        Interface.user = new_user
        Interface.backend.save_data()
        print(f"Создан новый пользователь: {new_user}")
        i = input("""
        0)Завершить работу
        1)Войти в созданный аккаунт
        """)
        if i == "0":
            Interface.finish()
        elif i == "1":
            Interface.entrance()
    @staticmethod
    def request():
        pass
    @staticmethod
    def finish():
        print("Работа программы завершена.")
        sys.exit(0)
 
Interface.start()
print(Interface.backend.get_users())



    
    