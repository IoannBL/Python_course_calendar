import flet as ft
import datetime
import sys
from Calendar import Calendar
from Backend import Backend
from User import User
from Event import Event
from Notification import NotificationManager


class Interface(ft.Container):
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
    
    def __init__(self, page: ft.Page):
        super().__init__()
        self.content = ft.Container(
            expand=True,
            gradient=ft.LinearGradient([ft.colors.INDIGO_500, ft.colors.RED_200]),
            alignment=ft.alignment.Alignment(0, 0),
            content=
            ft.Container(
                ft.Stack([
                    ft.Container(
                        margin=ft.margin.only(top=300, bottom=700),
                        # alignment=ft.alignment.center,
                        # expand= True,
                        padding=ft.padding.all(20),
                        border_radius=11,
                        width=300,
                        height=300,
                        bgcolor='#33ffffff',
                        shadow=ft.BoxShadow(
                            spread_radius=1,
                            blur_radius=100,
                            color=ft.colors.BLUE_GREY_300,
                            offset=ft.Offset(0, 0),
                            blur_style=ft.ShadowBlurStyle.OUTER,
                        ),
                        content=
                        ft.Column([
                            ft.Container(
                                content=(ft.Text("Calendar", color=ft.colors.BLUE_800, scale=2, size=10)),
                                width=300,
                                height=30,
                                alignment=ft.alignment.center
                            ),
                            ft.Container(
                                content=ft.ElevatedButton("Войти", on_click=self.show_entrance,
                                                          style=ft.ButtonStyle(
                                                              shape=ft.RoundedRectangleBorder(radius=10), ),
                                                          bgcolor=ft.colors.BLUE_50,
                                                          ),
                                width=300,
                                height=50,
                                margin=ft.margin.only(top=30),
                            
                            ),
                            ft.Container(
                                content=ft.ElevatedButton("Создать пользователя", color=ft.colors.BLACK,
                                                          on_click=self.show_create_new_user,
                                                          bgcolor=ft.colors.LIGHT_GREEN_ACCENT_200,
                                                          style=ft.ButtonStyle(
                                                              shape=ft.RoundedRectangleBorder(radius=10),
                                                          ), ),
                                width=300,
                                height=50,
                            ),
                            ft.Container(
                                content=ft.TextButton("Завершить работу", on_click=lambda _: self.page.go("/entrance")),
                                width=180,
                                height=50,
                                margin=ft.margin.only(top=20, left=40),
                                opacity=1
                            ),
                        ],
                        ),
                    )
                
                ]),
                
                # alignment=ft.alignment.center,
                # expand=True
            ),
        
        )
        # self.alignment = ft.alignment.center
        # self.expand = True
        Interface.navbar(None)
    
    @staticmethod
    def navbar(page):
        navbar = ft.AppBar(
            leading=ft.Icon(ft.icons.CALENDAR_MONTH, color=ft.colors.BLUE_800),
            leading_width=100,
            title=ft.Text("КАЛЕНДАРЬ", color=ft.colors.BLUE_800),
            center_title=False,
            # bgcolor=ft.colors.LIME_100,
            toolbar_height=60,
            actions=[
                ft.IconButton(ft.icons.HOME, on_click=lambda _: page.go('/')),
                ft.IconButton(ft.icons.PERSON_ROUNDED, on_click=lambda _: page.go('/profile')),
                ft.IconButton(ft.icons.SETTINGS_ROUNDED, on_click=lambda _: page.go('/settings'))
            ]
        )
        return navbar
    
    def show_create_new_user(self, e):
        username = ft.TextField(label="Введите имя пользователя: ", autofocus=True)
        password = ft.TextField(label="Придумайте пароль: ", autofocus=True)
        username_con = (ft.Container(
            content=username,
            width=300,
            height=50
        ))
        password_con = ft.Container(
            content=password,
            width=300,
            height=50
        )
        dlg_modal = ft.AlertDialog(
            modal=False,
            content=ft.Container(
                ft.Column(
                    [
                        ft.IconButton(
                            icon=ft.icons.CLOSE,
                            icon_color="blue700",
                            icon_size=20,
                            tooltip="Закрыть",
                            on_click=lambda x: x.page.close_dialog()),
                        ft.Container(
                            width=300,
                            height=200,
                            content=(
                                ft.Column(
                                    [
                                        ft.Container(content=username_con),
                                        ft.Container(content=password_con),
                                    ]
                                )
                            ),
                        )
                    ],
                    tight=True,
                ),
                padding=0,
            ),
            actions=[
                ft.ElevatedButton("Сохранить данные", on_click=lambda x: self.create_new_user(username, password, e))
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda x: print("Modal dialog dismissed!"),
        
        )
        
        e.page.show_dialog(dlg_modal)
    
    def create_new_user(self, username, password, e):
        new_user = User(username.value, password.value)
        Interface.backend.add_users(new_user)
        Interface.backend.save_data_users()
        Interface.user = new_user
        show_user = ft.AlertDialog(
            title=ft.Text(f"Создан новый пользователь - {new_user} "), on_dismiss=lambda e: print("Dialog dismissed!")
        )
        show_user.open = True
        self.page.update()
        e.page.show_dialog(show_user)
    
    def show_entrance(self, e):
        login = ft.TextField(label="Введите id пользователя: ", autofocus=True)
        password = ft.TextField(label="Введите пароль: ", autofocus=True)
        dlg_modal = ft.AlertDialog(
            modal=False,
            content=ft.Container(
                ft.Column(
                    [
                        ft.IconButton(
                            icon=ft.icons.CLOSE,
                            icon_color="blue700",
                            icon_size=20,
                            tooltip="Закрыть",
                            on_click=lambda x: x.page.close_dialog()),
                        ft.Container(
                            width=300,
                            height=200,
                            content=(
                                ft.Column(
                                    [
                                        ft.Container(content=login),
                                        ft.Container(content=password),
                                    ]
                                )
                            ),
                        )
                    ],
                    tight=True,
                ),
                padding=0,
            ),
            actions=[
                ft.ElevatedButton("Войти", on_click=lambda x: self.entrance(login, password, e))
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda x: print("Modal dialog dismissed!"),
        )
        
        e.page.show_dialog(dlg_modal)
    
    def entrance(self, log, passw, e):
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