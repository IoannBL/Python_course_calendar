# import asyncio as asinc
import flet as ft
import sys
from Calendar import Calendar
from Backend import Backend
from User import User
from Event import Event
from Notification import NotificationManager
class Interface:
    user = None
    event = None
    calendar = None
    current_user = None
    state = "start"
    backend = Backend()
    notify = NotificationManager()
    backend.load_data_users()
    backend.load_data_events()
    backend.load_data_calendar()
    notify.load_notifications()
  
    
    def create_new_user(self,username,password,e):
        new_user = User(self,username.value, password.value)
        Interface.backend.add_users(new_user)
        Interface.backend.save_data_users()
        Interface.user = new_user
        show_user = ft.AlertDialog(
            title=ft.Text(f"Создан новый пользователь - {new_user} "), on_dismiss=lambda e: print("Dialog dismissed!")
        )
        show_user.open = True
        self.page.update()
        e.page.show_dialog(show_user)
    def entrance(self,log,passw,e):
        login = log.value
        user_exists = False
        for user in Interface.backend.get_users():
            if user.get_id() == login:
                user_exists = True
                password = passw.value
                if user.check_password(password):
                    Interface.current_user = user
                    Interface.calendar = Calendar(user)
                    self.page.go("/main")
                else:
                    show_user_password = ft.AlertDialog(
                        title=ft.Text("Пароль введен неверно"),
                        on_dismiss=lambda e: print("Dialog dismissed!")
                    )
                    show_user_password.open = True
                    self.page.update()
                    e.page.show_dialog(show_user_password)
        if not user_exists:
            show_user = ft.AlertDialog(
                title=ft.Text("Пользователя не существует"),
                on_dismiss=lambda e: print("Dialog dismissed!")
            )
            show_user.open = True
            self.page.update()
            e.page.show_dialog(show_user)

        
    
    



