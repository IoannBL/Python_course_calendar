from User import User
from Event import Event
from Calendar import Calendar

# c = Event("Собрание",dmitriy)
# c.delete_event(dmitriy)
# print(c.get_organizer())
# print(c)

ivan = User("Иван", "123lf8j*j")
petr = User("Петр", "12hd7u3g9")
denis = User("Денис", "jsdkjfgh8734")
vitaliy = User("Виталий", "kjsdfhg7874")
event_1 = Event("Собрание", petr, "описание")
event_2 = Event("День рождения", petr, "описание")

event_2.create_periodic_event("2023-11-23", "yearly")
event_1.create_periodic_event("2023-11-23", "yearly")

# print(event_2.get_frequency)

event_2.add_part(petr, ivan)
event_2.add_part(petr, denis)
event_2.add_part(petr, vitaliy)

# print(d)
event_2.participants_leavе(denis)
# print(d)
# event_2.del_participants(petr, ivan)
# print(d)
event_2.del_description(petr)
# print(d)
event_2.change_description(petr, "новое описание")
# print(d)
cal_1 = Calendar(petr, "Рабочий")
cal_1.add_event(event_2)
cal_1.add_event(event_1)
# print(cal_1)
event_2.write_to_json()
print(event_2.read_from_json())
print(cal_1.get_calendar())
# print(cal_1.search_event("2021-11-12", "2025-11-12"))

