"""
Описывает некоторoе "событие" - промежуток времени с присвоенными характеристиками
У события должно быть описание, название и список участников
Событие может быть единожды созданым
Или периодическим (каждый день/месяц/год/неделю)

Каждый пользователь ивента имеет свою "роль"
организатор умеет изменять названия, список участников, описание, а так же может удалить событие
участник может покинуть событие

запрос на хранение в json
Уметь создавать из json и записывать в него

Иметь покрытие тестами
Комментарии на нетривиальных методах и в целом документация
"""
import json
import datetime
from dateutil import rrule
from User import User
import json

class Event:
    def __init__(self, title, organizer, description = None):
        self._title = title
        self._organizer = organizer
        self._description = description
        self._participants = set()
        if isinstance(organizer, User):
            self._participants.add(organizer)
        self._frequency = []

        
  
    # def __str__(self):
    #     return f"{self._title},{self._frequency},{self._participants},{self._description}"
    def __repr__(self):
        return f"Event('{self._title}', {self._participants}, {self._description})"
   
    def get_title(self, title):
        return title
    
    def get_organizer(self):
        return self._organizer
    def get_frequency_event(self):
        return self._frequency
    
    def create_periodic_event(self, start_date, frequency, format = "%Y,%m,%d"):
        '''Метод задает частоту события на 5 лет вперед начиная с установленной даты первого события.'''
        start_date = datetime.datetime.strptime(start_date, format)
        end_date = start_date + datetime.timedelta(days=365 * 2)
        if frequency == "once":
            self._frequency.append(start_date)
        else:
            if frequency == "daily":
                rule = rrule.DAILY
            elif frequency == "weekly":
                rule = rrule.WEEKLY
            elif frequency == "monthly":
                rule = rrule.MONTHLY
            elif frequency == "yearly":
                rule = rrule.YEARLY
            else:
                print("Неверные данные.")
                return
            for date in rrule.rrule(rule, dtstart=start_date, until=end_date):
                self._frequency.append(date)
                
    def add_part(self, admin, participant):
        if admin == self._organizer and isinstance(admin, User) and isinstance(participant, User):
            self._participants.add(participant)
        else:
            raise ValueError("Некорректные участники события.")
    def get_participants(self):
        return self._participants
    
    def del_participants(self,admin,user):
        if admin == self._organizer and user in self._participants:
            self._participants.remove(user)
        else:
            raise ValueError("Некорректные участники события")
    
    def participants_leavе(self,user):
        if user in self._participants and user != self._organizer:
            self._participants.remove(user)
            
    def change_description(self,user, new_description):
        if user == self._organizer and isinstance(user,User):
            self._description = new_description
        else:
            raise ValueError("Описание не может быть изменено")
    
    def del_description(self, user):
        if user == self._organizer and isinstance(user, User):
            self._description = None
        else:
            raise ValueError("Описание не может быть удалено")
    
    def to_dict(self):
        event_dict = {
            'title': self._title,
            'organizer': self._organizer.to_dict(),
            'description': self._description,
            'participants': [participant.to_dict() for participant in self._participants],
            'frequency': [dt.strftime("%Y-%m-%d") for dt in self._frequency]
        }
        return event_dict
    
    def write_to_json(self, filename='event_data.json'):
        event_dict = self.to_dict()
        event_json = json.dumps(event_dict, indent=2)
        with open(filename, 'w') as file:
            file.write(event_json)
    
    @classmethod
    def from_dict(cls, event_dict):
        title = event_dict.get('title')
        organizer = User.from_dict(event_dict.get('organizer'))
        description = event_dict.get('description')
        participants = {User.from_dict(participant) for participant in event_dict.get('participants', [])}
        frequency = [datetime.datetime.strptime(dt, "%Y-%m-%d").date() for dt in event_dict.get('frequency', [])]
        event = cls(title, organizer, description)
        event._participants = participants
        event._frequency = frequency
        return event
    
    @classmethod
    def read_from_json(cls, file='event_data.json'):
        with open(file, 'r') as f:
            event_dict = json.loads(f.read())
        return cls.from_dict(event_dict)
        
       


            
            
    
