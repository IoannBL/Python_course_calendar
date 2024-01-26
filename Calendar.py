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
    
    def __init__(self, organizer_cal):
        self._organizer_cal = organizer_cal
        self._calendar = {}
  
    def __str__(self):
        return f"({self._organizer_cal}, {self._calendar})"
    
    def __repr__(self):
        return f"({self._organizer_cal}, {self._calendar})"
    
    def __eq__(self, other):
        if isinstance(other, Calendar):
            return (self._organizer_cal == other._organizer_cal)
        return False
    
    def __hash__(self):
        return hash((self._organizer_cal))
    
    def get_calendar(self):
        sorted_calendar = sorted(self._calendar.items(), key=lambda x: x[0])
        return dict(sorted_calendar)
    
    def get_organizer_cal(self):
        return self._organizer_cal
    
    def add_event_cal(self, event):
        '''Метод формирут календарь на основе параметров события. Даты беруться из частоты события(frequency) формируя
         словарь {дата : событие}'''
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
        '''Метод выводит события в промежутке дат.'''
        start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
        end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
        events_in_range = []
        sorted_events = sorted(self._calendar.items(), key=lambda x: x[0])
        for date, events in sorted_events:
            if start_date <= date <= end_date:
                events_in_range.extend(events)
        return events_in_range

    def del_event(self, user):
        if user == self._organizer_cal and isinstance(user, User):
            self._calendar.remove_event(self)
        else:
            raise ValueError("Только организатор может удалить событие")
    
    def get_events_cal(self):
        return list(self._calendar.values())


        
