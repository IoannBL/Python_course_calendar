"""
Сущность, отвечающая за храние и предоставление данных
Оно хранит пользователей, календари и события.
Хранение в том числе означает сохранение между сессиями в csv файлах
(пароли пользователей хранятся как hash)

Должен быть статическим или Синглтоном

*) Нужно хранить для каждого пользователя все события которые с нима произошли но ещё не были обработаны.
"""
import datetime
from Event import Event
from User import User
import csv
class Backend:
    _instance = None
    file_users = 'backend_data_users.csv'
    file_events = 'backend_data_events.csv'
    file_calendar = 'backend_data_calendar.csv'
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Backend, cls).__new__(cls, *args, **kwargs)
            cls._instance._users = []
            cls._instance._events = []
            cls._instance._calendar = []
        return cls._instance
    
    def __repr__(self):
        return f"Users:{self._users}"
    
    def __str__(self):
        return f"Users:{self._users},{self._calendar}"
    
    def add_users(self, user):
        self._instance._users.append(user)
    
    def get_users(self):
        return self._users
    
    def get_events(self):
        return self._events
    def add_events(self, event):
        return self._instance._events.append(event)
    
    def get_calendar(self):
        return self._calendar
    def add_calendar(self, calendar):
        self._instance._calendar.append(calendar)
    def save_data_users(self):
        with open(self.file_users, mode='w', newline='') as file:
            fieldnames = ['Login', 'Password', 'Id']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for user in self._users:
                writer.writerow({'Login': user.get_name(), 'Password': user.get_password(), 'Id': user.get_id()})

    def save_data_events(self):
        with open(self.file_events, mode='w', newline='') as file:
            fieldnames = ['title', 'organizer', 'description', 'participants', 'frequency']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for event in self._events:
                writer.writerow({
                    'title': event.get_title(),
                    'organizer': event.get_organizer().get_name(),
                    'description': event.get_description() if True else None,
                    'participants': ', '.join(user.get_name() for user in event.get_participants()),
                    'frequency': ', '.join(date.strftime("%Y-%m-%d") for date in event.get_frequency_event())
                })
    
    def write_to_csv(self, filename):
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Variable', 'Date', 'Events']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for sublist in self._calendar:
                variable, dictionary = sublist
                for date, events in dictionary.items():
                    formatted_date = date.strftime("%Y-%m-%d")
                    events_data = ', '.join([str(event.name) for event in events])
                    writer.writerow({'Variable': variable, 'Date': formatted_date, 'Events': events_data})

    # def save_data_calendar(self):
    #     with open(self.file_calendar, 'w', newline='') as file:
    #         fieldnames = ['Организатор', 'Дата', 'События']
    #         writer = csv.DictWriter(file, fieldnames=fieldnames)
    #         writer.writeheader()
    #
    #         for title, (organizer, date, events) in self._calendar:
    #             formatted_date = date.strftime("%Y-%m-%d")
    #             events_data = ', '.join([str(event) for event in events])
    #             writer.writerow({'Организатор': organizer,
    #                              'Дата': formatted_date,
    #                              'События': events_data})
    
    # def save_data_calendar(self):
    #     with open(self.file_calendar, 'w', newline='') as file:
    #         fieldnames = ['organizer', 'date', 'events']
    #         writer = csv.DictWriter(file, fieldnames=fieldnames)
    #         writer.writeheader()
    #         for organizer,(date, events) in self._calendar:
    #             formatted_date = date.strftime("%Y-%m-%d")
    #             events_data = ', '.join([str(event) for event in events])
    #             writer.writerow({'Организатор': organizer,
    #                              'Дата': formatted_date,
    #                              'События': events_data})
    
    def load_data_users(self):
        try:
            with open(self.file_users, mode='r') as file:
                reader = csv.DictReader(file)
                self._users = []
                for row in reader:
                    login = row['Login']
                    password_hash = row['Password']
                    user_id = row['Id']
                    user = User(login, password_hash, user_id)
                    self._users.append(user)
        except FileNotFoundError:
            pass
    
    def load_data_events(self):
        try:
            with open(self.file_events, mode='r') as file:
                reader = csv.DictReader(file)
                self._events = []
                for row in reader:
                    title = row['title']
                    organizer_name = row['organizer']
                    description = row['description']
                    organizer = next((user for user in self._users if user.get_name() == organizer_name), None)
                    if organizer:
                        event = Event(title, organizer, description)
                        participants = row['participants'].split(', ')
                        for participant_name in participants:
                            participant = next((user for user in self._users if user.get_name() == participant_name),
                                               None)
                            if participant:
                                event.add_part(organizer, participant)

                        frequencies = row['frequency'].split(', ')
                        for date_str in frequencies:
                            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                            event.create_periodic_event(date, "once")
                        self._events.append(event)
        except FileNotFoundError:
            pass
    def load_data_calendar(self):
        try:
            with open(self.file_calendar, 'r') as file:
                reader = csv.DictReader(file)
                self._calendar = {}
                for row in reader:
                    date = datetime.datetime.strptime(row['date'], "%Y-%m-%d").date()
                    event_titles = row['events'].split(', ')
                    for title in event_titles:
                        # Создаем событие и добавляем его в календарь
                        event = Event(self.calendar.get_organizer(), title)
                        self.calendar.add_event(event)
        except FileNotFoundError:
            pass

    

  