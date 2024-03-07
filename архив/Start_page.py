import flet as ft
import datetime
import sys
from Calendar import Calendar
from Backend import Backend
from User import User
from Event import Event
from Notification import NotificationManager
# from Notification_pr import Notification_pr




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


class Notification_pr(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.notify = None
        self.notify_1 = ft.Row(
            scroll='always'
        )
        notifications = Notification_pr.view_notifications()
        for i in notifications:
            self.notify_1.controls.append(
                ft.Container(
                    padding=10,
                    width=175,
                    bgcolor='#55cc3333',
                    expand=False,
                    border_radius=10,
                    alignment=ft.alignment.top_center,
                    on_click=lambda e: print("Clickable without Ink clicked!"),
                    content=ft.Column(
                        horizontal_alignment=ft.alignment.top_center,
                        # alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Container(
                                width=175,
                                height=20,
                                padding=ft.padding.only(right=130),
                                content=ft.Icon(name=ft.icons.CIRCLE_NOTIFICATIONS_OUTLINED,
                                                color=ft.colors.BLUE_800)
                            ),
                            ft.Text(i, size=15, color=ft.colors.BLUE_900),
                        
                        ]
                    )
                )
            )
        # return notify
    
    def build(self):
        self.notify = ft.Container(
            margin=ft.margin.only(top=0, left=10, right=10),
            height=150,
            border_radius=10,
            visible=True,
            content=
            self.notify_1)
        return self.notify
    
    @staticmethod
    def view_notifications():
        notify = []
        notifications = Interface.notify.get_notifications()
        # user_to_find = Interface.current_user.get_id()
        user_to_find = "@Денис3"
        found_notifications = False
        for notification in notifications:
            added_user = notification.get('AddedUser')
            if added_user == user_to_find:
                found_notifications = True
                organizer = notification.get('Organizer')
                events = notification.get('Events')
                notify.append(f"Пользователь {organizer} добавил вас в событие {events}.")
            remove_user = notification.get('RemoveUser')
            if remove_user == user_to_find:
                found_notifications = True
                organizer = notification.get('Organizer')
                events = notification.get('Events')
                notify.append(f"Пользователь {organizer} удалил вас из события {events}.")
        if not found_notifications:
            notify.append("Новых уведомлений нет")
        return notify
    # def add_control_to_page(self):
    #     control = Notification_pr(self)
    #     self.page.add(control)
    def set_visibility(self, visibility):
        """Метод для установки видимости контейнера."""
        if self.notify:
            self.notify.visible = visibility
            self.build().update()
class Main_page(ft.Container):
    def __init__(self,page:ft.Page,*args,**kwargs):
        super().__init__(*args, **kwargs)
        # self.app = app
        self.page = page
        self.notification = Notification_pr()
        # self.notification.add_control_to_page()
        self.resultdata = ft.ListView()
        self.resultcon = ft.Container(
            bgcolor="red200",
            padding=10,
            margin=10,
            offset=ft.transform.Offset(-2, 0),
            animate_offset=ft.animation.Animation(600, curve="easeIn"),
            content=ft.Column([self.resultdata])
        )

        # self.notify = ft.Container(
        #     margin=ft.margin.only(top=0, left=10, right=10),
        #     height=150,
        #     border_radius=10,
        #     visible=True,
        #     content=
        #     Main_page.show_notify(),
        # )
        self.content = (ft.Container(
            height=1500,
            expand=True,
            alignment=ft.alignment.center_left,
            content=
            ft.Row(
                [
                    ft.Container(
                        # bgcolor=ft.colors.LIME_100,
                        content=
                        ft.Column(
                            spacing=0,
                            controls = [
                            ft.Divider(height=1, color=ft.colors.BLUE_GREY_300),
                            ft.TextButton(
                                on_click = self.animate_container_event,
                                width=200,
                                height=40,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=1),),
                                content=ft.Row([
                                        ft.Icon(name=ft.icons.CREATE, color=ft.colors.BLUE_800),
                                        ft.Text("Создать")],
                                )
                            ),
                            ft.TextButton(
                                on_click = self.animate_container_show_all_event,
                                width=200,
                                height=40,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=1)),
                                content=ft.Row([
                                    ft.Icon(name=ft.icons.EMOJI_EVENTS_OUTLINED, color=ft.colors.BLUE_800),
                                    ft.Text("Все события")],
                                )
                            ),
                            ft.TextButton(
                                width=200,
                                height=40,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=1), ),
                                content=ft.Row([
                                    ft.Icon(name=ft.icons.CALENDAR_VIEW_MONTH_ROUNDED, color=ft.colors.BLUE_800),
                                    ft.Text("Календарь")],
                                )
                            ),
                            ft.TextButton(
                                # on_click = self.animate_container,
                                on_click=lambda _: self.notification.set_visibility(False),
                                width=200,
                                height=40,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=1), ),
                                content=ft.Row([
                                    ft.Icon(name=ft.icons.NOTIFICATIONS, color=ft.colors.BLUE_800),
                                    ft.Text("Уведомления")],

                                )
                            ),
                            ft.TextButton(
                                width=200,
                                height=40,
                                on_click= lambda _: self.page.go('/'),
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=1), ),
                                content=ft.Row([
                                    ft.Icon(name=ft.icons.EXIT_TO_APP, color=ft.colors.BLUE_800),
                                    ft.Text("Выход")],
                                )
                            ),]
                        ),
                        width=200,
                        expand=False,
                    ),
                    ft.VerticalDivider(width=1, color=ft.colors.BLUE_GREY_300),
                    ft.Container(
                        alignment=ft.alignment.center,
                        expand=True,
                        # bgcolor=ft.colors.LIGHT_BLUE_200,
                        bgcolor=ft.colors.WHITE10,
                        content=
                        ft.Column([
                            ft.Divider(height=1, color=ft.colors.BLUE_GREY_300),
                            self.notification.build(),
                            
                            ft.Container(
                                margin=ft.margin.only(left=10,right=10),
                                height=500,
                                # width=100,
                                expand=False,
                                # bgcolor=ft.colors.RED_200,
                                border_radius=10,
                                content=
                                
                                ft.Row(
                                    scroll="alwais",
                                    controls=[
                                        self.con_create_event,
                                        self.show_all_event,
                                        self.show_calendar

                                    ]
                                )
                            ),
                        ]),
                    )
                ],
                spacing=0,
                expand=True,
            )
        ))




    def searchnow(self, e):
        mysearch = e.control.value
        self.resultdata.controls.clear()
        if mysearch:
            for item in Interface.backend.get_users():
                self.resultdata.controls.append(
                    ft.Text(item, size=20, color="white")
                )
            self.resultcon.visible = bool(self.resultdata.controls)
            if self.resultcon.visible:
                self.resultcon.offset = ft.transform.Offset(0, 0)
            else:
                self.resultcon.offset = ft.transform.Offset(-2, 0)

                ft.page.update()
    def on_submit(self,e):
        self.searchnow(e)

    name_event = ft.TextField(label="Название: ", autofocus=True)
    description_event = ft.TextField(
            label="Описание: ",
            multiline=True,
            min_lines=1,
            max_lines=3,
        )
    participants_event = ft.TextField(label="Участники: ",on_change=on_submit,on_submit=on_submit)
    date_event = ft.TextField(label="Дата : ")
    periodic_event = ft.TextField(label="Периодичность : ")
    date_button = ft.ElevatedButton(
        "Pick date",
        icon=ft.icons.CALENDAR_MONTH,
        on_click=lambda _: date_picker.pick_date(),
    )


    con_create_event = ft.Container(
        width=500,
        # height=500,
        bgcolor='#443366ff',
        expand=True,
        alignment=ft.alignment.center,
        border_radius=10,
        content=ft.Column(
            expand=True,
            controls = [
                ft.Column([
                    ft.Container(
                        height=50,
                        width=1000,
                        bgcolor=ft.colors.LIGHT_BLUE_900,
                        content=ft.Container(
                            bgcolor=ft.colors.LIGHT_BLUE_900,
                            alignment=ft.alignment.center,
                            content=ft.Text("Создать событие",color="white",size=15)
                        ),
                    ),
                    ft.Container(
                        margin=ft.margin.all(20),
                        content= ft.Column([
                            name_event,
                            description_event,
                            participants_event,
                            date_button,
                            date_event,
                            periodic_event
                        ]
                        )
                    )

                ])

            ]
        )

    )

    show_all_event = ft.Container(
        width=500,
        height=500,
        bgcolor='#443366ff',
        expand=True,
        alignment=ft.alignment.center,
        border_radius=10
    )

    show_calendar = ft.Container(
        width=500,
        height=500,
        bgcolor='#443366ff',
        expand=True,
        alignment=ft.alignment.center,
        border_radius=10
    )


    def animate_container_event(self,e):
        if self.con_create_event.expand == True:
            self.con_create_event.expand = False
        elif self.con_create_event.expand == False:
            self.con_create_event.expand = True
        self.con_create_event.update()

    def animate_container_show_all_event(self, e):
        if self.show_all_event.expand == True:
            self.show_all_event.expand = False
        elif self.show_all_event.expand == False:
            self.show_all_event.expand = True
        self.show_all_event.update()

    def animate_container(self,e):
        # if self.notification.visible == True:
        #     self.notification.visible = False
        # elif self.notification.visible == False:
        #     self.notification.visible = True
        # self.notification.update()
        self.notification.build().visible = not self.notification.build().visible
        # self.toggle_nav_rail_button.selected = not self.toggle_nav_rail_button.selected
        self.notification.build().update()
        self.page.update()
    

    # @staticmethod
    # def view_notifications():
    #     notify = []
    #     notifications = Interface.notify.get_notifications()
    #     # user_to_find = Interface.current_user.get_id()
    #     user_to_find = "@Денис3"
    #     found_notifications = False
    #     for notification in notifications:
    #         added_user = notification.get('AddedUser')
    #         if added_user == user_to_find:
    #             found_notifications = True
    #             organizer = notification.get('Organizer')
    #             events = notification.get('Events')
    #             notify.append(f"Пользователь {organizer} добавил вас в событие {events}.")
    #         remove_user = notification.get('RemoveUser')
    #         if remove_user == user_to_find:
    #             found_notifications = True
    #             organizer = notification.get('Organizer')
    #             events = notification.get('Events')
    #             notify.append(f"Пользователь {organizer} удалил вас из события {events}.")
    #     if not found_notifications:
    #         notify.append("Новых уведомлений нет")
    #     return notify

    
    
    
    
    
    
    
    
    # txtsearch = ft.TextField(label="Search now", on_change=searchnow)
    # page.add(txtsearch)
    #
    # page.add(
    #     Column([
    #         Text("Search Anything", size=30, weight="bold"),
    #         txtsearch,
    #         resultcon
    #     ])
    # )