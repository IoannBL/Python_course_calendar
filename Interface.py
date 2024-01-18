"""
Позволяет зайти по логину-паролю или создать нового пользователя (а так же выйти из аккаунта)
Позволяет выбрать календарь, узнать ближайшие события, события из промежутка времени а так же
Создать событие или удалить событие
После создания события можно добавить туда пользователей
Если нас добавили в событие или удалили мы получаем уведомление.

в main можно использовать ТОЛЬКО interface
"""
import datetime
import sys
from Calendar import Calendar
from Backend import Backend
from User import User
from Event import Event
class Interface:
    user = None
    event = None
    calendar = None
    current_user = None
    state = "start"
    backend = Backend()
    backend.load_data_users()
    backend.load_data_events()
    backend.load_data_calendar()
    
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
        4)Удалить событие
        5)Просмотреть все свои события
        6)Создать Календарь
        7)Просмотр Календаря
        8)Добавить событие в Календарь
        9)Выйти из аккаунта
        """)
        if ret == "0":
            Interface.finish()
        elif ret == "1":
            Interface.create_event()
        elif ret == "5":
            print(Interface.get_events())
            Interface.read()
        elif ret == "6":
            Interface.create_calengar()
        elif ret == "7":
            print(Interface.backend.get_calendar())
        elif ret == "8":
            Interface.add_event_to_cal()
        elif ret == "9":
            Interface.start()
    @staticmethod
    def create_calengar():
        organizer = Interface.current_user
        title = input("Введите название календаря: ")
        new_calendar = Calendar(organizer, title)
        Interface.calendar = new_calendar
        Interface.backend.save_data_calendar()
        print("Создан календарь: ",Interface.calendar.get_calendar())
        
        Interface.read()
        
    @staticmethod
    def add_event_to_cal():
        
        Interface.calendar.add_event_cal()
        print(Interface.backend.get_calendar())
    
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
                    Interface.current_user = user
                    print("Добро пожаловать, ", Interface.current_user)
                    for i in Interface.backend.get_calendar():
                        if i.get_organizer_cal == Interface.current_user:
                            Interface.calendar = i
                    print("Ваш календарь: ", Interface.calendar)
                    Interface.read()
                else:
                    print("Логин или пароль введены неверно, выполните вход заново")
                    Interface.start()
        if not user_exists:
            print("Пользователя не существует")
            Interface.entrance()
            
      
    @staticmethod
    def create_event():
        if not Interface.current_user:
            print("Вы должны войти в систему, прежде чем создавать события.")
            return
        
        title = input("Введите название события: ")
        organizer = Interface.current_user
        description = input("Введите описание события (или оставьте пустым): ")
        new_event = Event(title, organizer, description)
        Interface.event = new_event
        Interface.backend.add_events(new_event)
        Interface.backend.save_data_events()
 
        print("Участники доступные для добавления в событие: ", Interface.backend.get_users())
        participants_str = input("Введите имена участников (разделяйте запятыми): ")
        participants_names = [name.strip() for name in participants_str.split(',')]

        for participant_name in participants_names:
            participant = next((user for user in Interface.backend.get_users() if user.get_name() == participant_name), None)
            if participant:
                new_event.add_part(organizer, participant)
            else:
                print(f"Пользователь {participant_name} не найден.")

        start_date = input("Введите дату начала события (гггг-мм-дд): ")
        frequency = input("Введите частоту события (once, daily, weekly, monthly, yearly): ")
        new_event.create_periodic_event(start_date, frequency)
        Interface.backend.save_data_events()
        print(f"Событие {new_event.get_title} создано.")
        print("Список всех ваших событий: ", Interface.get_events())
        Interface.calendar.add_event_cal(new_event)
        Interface.backend.save_data_calendar()
        Interface.read()
        
  
    @staticmethod
    def get_events():
        'Метод выдает список всех событий пользователя'
        events = []
        for event in Interface.backend.get_events():
            if Interface.current_user in event.get_participants():
                events.append(event)
        return events
    
    @staticmethod
    def get_calendar():
        for i in Interface.backend.get_calendar():
            if Interface.current_user == i.get_organizer_cal:
                return i

    @staticmethod
    def add_user_in_event():
        admin = Interface.current_user
        name_events = [event.get_title() for event in Interface.get_events()]
        print("Введите название события из списка для удаления из него участников", name_events)
        name_event = input()
        selected_event = next((event for event in Interface.get_events() if event.get_title() == name_event), None)
        if selected_event:
            participants = selected_event.get_participants()
            print(f"Участники события {name_event}: {participants}")
            
            # Ваша логика добавления пользователя к событию здесь
        
        else:
            print(f"Событие с названием {name_event} не найдено.")
    @staticmethod
    def remove_user_from_event():
        pass
    @staticmethod
    def remove_event():
         event.get_frequency_event()
    @staticmethod
    def view_events():
        pass
    @staticmethod
    def create_new_user():
        new_user = User.create_user()
        Interface.backend.add_users(new_user)
        Interface.user = new_user
        Interface.backend.save_data_users()
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
print(Interface.current_user)
print(Interface.get_events)



    
    