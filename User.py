"""
Пользователь - имеет логин и пароль, а так же календарь.
у пользователя есть итендифекатор начинающийся с @
"""
import hashlib

class User:
    id_count = 0
    def __init__(self, login, password, *args, **kwargs):
        self._login = login
        self._password = hashlib.sha256(password.encode()).hexdigest()
        self._id = f"@{str(self._login)}{str(User.id_count)}"
        User.id_count +=1

    
    # def __str__(self):
    #     return f"name:{self._name}, password:{self._password}, id:{self._id}"
    
    def __repr__(self):
        return f"name:{self._login},password:{self._password},id:{self._id}"
    
    @classmethod
    def create_user(cls):
        username = input("Введите имя пользователя: ")
        password = input("Введите пароль: ")
        return cls(username, password)
    
    def add_name(self, username):
        self._login = username
        return self._login
    def get_name(self):
        return self._login
    
    def get_password(self):
        return self._password
    
    def get_id(self):
        return self._id
    
    def to_dict(self):
        return {'name': self._login, "id": self._id, 'password': self._password}
    
    @classmethod
    def from_dict(cls, user_dict):
        return cls(user_dict['name'], user_dict['password'], user_dict['id'])
    def check_password(entered_password, saved_password_hash):
        return bcrypt.checkpw(entered_password.encode('utf-8'), saved_password_hash.encode('utf-8'))
    # def check_password(self, input_password):
    #     return self._password == hashlib.sha256(input_password.encode()).hexdigest()
    
    # def check_password(self, entered_password):
    #     try:
    #         entered_password_hash = self._password_hasher.hash(entered_password)
    #         self._password_hasher.verify(self._password, entered_password)
    #         return True
    #     except argon2.exceptions.VerifyMismatchError:
    #         return False
     
    
    


    
