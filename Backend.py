"""
Сущность, отвечающая за храние и предоставление данных
Оно хранит пользователей, календари и события.
Хранение в том числе означает сохранение между сессиями в csv файлах
(пароли пользователей хранятся как hash)

Должен быть статическим или Синглтоном

*) Нужно хранить для каждого пользователя все события которые с нима произошли но ещё не были обработаны.
"""

from User import User
import csv
class Backend:
    _instance = None
    file = 'backend_data.csv'
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Backend, cls).__new__(cls, *args, **kwargs)
            cls._instance._users = []
        return cls._instance
    
    def __repr__(self):
        return f"Users:{self._users}"
    
    def __str__(self):
        return f"Users:{self._users}"
    
    
    def add_users(self, user):
        self._instance._users.append(user)
    
    def get_users(self):
        return self._users
    
    def save_data(self):
        with open(self.file, mode='w', newline='') as file:
            fieldnames = ['Login', 'Password', 'Id']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for user in self._users:
                writer.writerow({'Login': user.get_name(), 'Password': user.get_password(), 'Id': user.get_id()})
    
    def load_data(self):
        try:
            with open(self.file, mode='r') as file:
                reader = csv.DictReader(file)
                self._users = []
                for row in reader:
                    login = row['Login']
                    password_hash = row['Password']
                    user_id = row['Id']
                    self._users.append(User(login, password_hash, user_id))
        except FileNotFoundError:
            pass


        
  