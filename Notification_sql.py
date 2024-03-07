import csv
import mysql.connector
class NotificationManager:
    file_notify = 'backend_data_notification.csv'
    
    def __init__(self):
        self._notifications = []
        self._connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345",
            database="calendar"
        )
        
    def get_notifications(self):
        return self._notifications

    def notification_add_part(self, organizer, added_user, remove_user, events):
        self._notifications.append({"Organizer": organizer.get_id(), "AddedUser": added_user.get_id(),"RemoveUser": None, "Events": events})

    def notification_remove_part(self, organizer,added_user, remove_user, events):
        self._notifications.append({"Organizer": organizer.get_id(),"AddedUser": None, "RemoveUser": remove_user.get_id(), "Events": events})
        
    def save_notifications(self):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM events")
        for notification in self._notifications:
            cursor.execute(
                "INSERT INTO notify (Organizer, AddedUser, RemoveUser, Events) VALUES (%s, %s, %s, %s)",
                (notification["Organizer"], notification["AddedUser"], notification["RemoveUser"],
                 ', '.join(notification["Events"])))
        self._connection.commit()
        # cursor.close()
        # with open(self.file_notify, 'w', newline='') as file:
        #     fieldnames = ['Organizer', 'AddedUser', 'RemoveUser', 'Events']
        #     writer = csv.DictWriter(file, fieldnames=fieldnames)
        #     writer.writeheader()
        #     for notification in self._notifications:
        #         writer.writerow(notification)

    def load_notifications(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT Organizer, AddedUser, RemoveUser, Events FROM notify")
        # self._notifications = []
        for row in cursor.fetchall():
            notification = {
                "Organizer": row[0],
                "AddedUser": row[1],
                "RemoveUser": row[2],
                "Events": row[3]
            }
            self._notifications.append(notification)
        cursor.close()
        # return self._notifications
        # try:
        #     with open(self.file_notify, 'r', newline='') as file:
        #         reader = csv.DictReader(file)
        #         self._notifications = [row for row in reader]
        # except FileNotFoundError:
        #     self._notifications = []
 
    def notify_added_to_event(self, organizer, added_user, remove_user,  event):
        event_title = event.get_title()
        self.notification_add_part(organizer, added_user, remove_user, [event_title])
    
    def notify_remove_from_event(self, organizer, added_user, remove_user, event):
        event_title = event.get_title()
        self.notification_remove_part(organizer, added_user, remove_user, [event_title])
    
    def remove_notifications(self, user_id):
        self._notifications = [notification for notification in self._notifications if
                               notification.get('AddedUser') != user_id and notification.get('RemoveUser') != user_id]
        
    
    