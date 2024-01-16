"""
Класс календаря - хранит события.
он умеет искать все события из промежутка (в том числе повторяющиеся)
он умеет добавлять/удалять события.
У каждого календаря ровно один пользователь.
"""
from User import User
from Event import Event
import datetime
class Calendar:
    
    def __init__(self):
        self._calendar = {}
  
    def __str__(self):
        return f"{self._calendar}"
    def add_event(self, event):
        if not isinstance(event, Event):
            raise ValueError("event не является экземпляром класса Event или его подкласса.")
        event_dat = event.get_frequency_event()
        for date in event_dat:
            if date in self._calendar:
                self._calendar[date].append(event)
            else:
                self._calendar[date] = [event]
            
    def rm_event(self,i):
        if i in self._calendar:
            self._calendar.pop(i,None)
    
    def search_event(self, start_date, end_date):
        start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
        end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
        events_in_range = []
        for date, events in self._calendar.items():
            if start_date <= date.date() <= end_date:
                events_in_range.extend(events)
        return events_in_range

    # def search_event(self, start, end):
    #     start = datetime.datetime.strptime(start, "%Y-%m-%d").date()
    #     end = datetime.datetime.strptime(end, "%Y-%m-%d").date()
    #     result = [key for key, i in self._calendar if start <= i.date() <= end]
    #     if len(result) == 0:
    #         raise ValueError("В данном диапозоне дат события отсутствуют")
    #     return result
    
    # result = [i for i in self._calendar if start <= i.date() <= end]

    def del_event(self, user):
        if user == self._organizer and isinstance(user, User):
            self._calendar.remove_event(self)
        else:
            raise ValueError("Только организатор может удалить событие")
        
        
    

        
