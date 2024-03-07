import flet as ft
from Interface_pr import Interface

class Notification_pr(ft.Container):
    def __init__(self,app_layout,page:ft.Page):
        super().__init__()
        self._notification = Notification_pr.view_notifications()
        self.app_layout = app_layout
       
        
        
            
    # @staticmethod
    # def show_notify():
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
        self.notify = ft.Container(
            margin=ft.margin.only(top=0, left=10, right=10),
            height=150,
            border_radius=10,
            visible=True,
            content=
            self.notify_1)
    
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