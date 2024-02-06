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
    
    def __init__(self, page: ft.Page):
        self.page = page
        self.appbar_items = [
            ft.PopupMenuItem(text="Login"),
            ft.PopupMenuItem(),  # divider
            ft.PopupMenuItem(text="Settings")
        ]
        self.appbar = ft.AppBar(
            leading=ft.Icon(ft.icons.GRID_GOLDENRATIO_ROUNDED),
            leading_width=100,
            title=ft.Text("Trolli", size=32, text_align="start"),
            center_title=False,
            toolbar_height=75,
            bgcolor=ft.colors.LIGHT_BLUE_ACCENT_700,
            actions=[
                ft.Container(
                    content=ft.PopupMenuButton(
                        items=self.appbar_items
                    ),
                    margin=ft.margin.only(left=50, right=25)
                )
            ],
        )
        self.page.appbar = self.appbar
        self.page.update()
    
    
    
    
    
    
    
    @staticmethod
    def start(page: ft.Page):
        
        page.bgcolor = ft.colors.BLUE_100
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
       
        buttons = [
            ft.Container(
                content=ft.ElevatedButton("Войти в аккаунт", on_click=Interface.entrance, bgcolor=ft.colors.GREEN_50),
                width=300,
                height=50
            ),
            ft.Container(
                ft.ElevatedButton("Создать нового пользователя", on_click=ft.app(target=Interface.create_new_user),
                                  bgcolor=ft.colors.GREEN_50),
                width=300,
                height=50
            ),
            ft.Container(
                ft.ElevatedButton("Завершить работу", on_click=Interface.finish),
                width=180,
                height=50,
                margin=ft.margin.only(top=70, left=40),
                opacity=1,
            ),
        ]
        button_column = ft.Column(buttons)
        st = ft.Stack(
            [
        #        ft.Image(
        #             src="https://pro-dachnikov.com/uploads/posts/2021-10/1633588003_41-p-foto-visotnikh-domov-foto-41.jpg",
        #             width=page.width,  # Ширина изображения равна ширине страницы
        #             height=page.height,  # Высота изображения равна высоте страницы
        #             # position_type=ft.PositionType.ABSOLUTE,  # Позиция абсолютная
        #             top=0,  # Размещаем изображение вверху
        #             left=0,  # Размещаем изображение слева
        # ),
                ft.Container(
                    content=button_column,
                    bgcolor=ft.colors.BLUE_50,
                    padding=ft.padding.all(20),
                    width=300,
                    height=300,
                    border_radius=30,
                    # opacity=0.2,
                    shadow=ft.BoxShadow(
                        spread_radius=1,
                        blur_radius=15,
                        color=ft.colors.BLUE_GREY_300,
                        offset=ft.Offset(0, 0),
                        blur_style=ft.ShadowBlurStyle.OUTER,
                    ),
                    alignment=ft.alignment.center,
                )
                
            ],
        )
        
        page.add(st)
    
    @staticmethod
    def entrance():
        login = input("Введите свой логин(id): ")
        user = Interface.backend.entrance(login)
        if user:
            Interface.current_user = user
            Interface.calendar = Calendar(user)
            Interface.main_menu()
        else:
            Interface.start()
    
    @staticmethod
    def create_new_user(page: ft.Page):
        page.bgcolor = ft.colors.BLUE_100
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        username_button = ft.TextField(label="Введите имя пользователя: ", autofocus=True)
        password_button = ft.TextField(label="Введите пароль: ", autofocus=True)
        
        buttons_column = ft.Column(
            [
                ft.Container(
                    content=username_button,
                    width=300,
                    height=50
                ),
                ft.Container(
                    content=password_button,
                    width=300,
                    height=50
                )
            ]
        )
        username = username_button.value
        password = password_button
        new_user = User(username, password)
        Interface.backend.add_users(new_user)
        Interface.backend.save_data_users()
        Interface.user = new_user
        
        
        plato = ft.Container(
            content=buttons_column,
            bgcolor=ft.colors.BLUE_50,
            padding=ft.padding.all(20),
            width=300,
            height=300,
            border_radius=30,
            # opacity=0.2,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.colors.BLUE_GREY_300,
                offset=ft.Offset(0, 0),
                blur_style=ft.ShadowBlurStyle.OUTER,
            ),
            alignment=ft.alignment.center,
        )
        page.add(plato)
        
        
        print(f"Создан новый пользователь: {new_user}")
        i = input("""
            0)Завершить работу
            1)Войти в созданный аккаунт
            """)
        if i == "0":
            Interface.finish()
        elif i == "1":
            Interface.entrance()
        
    
    @staticmethod
    def finish():
        print("Работа программы завершена.")
        Interface.backend.save_data_events()
        sys.exit(0)


# Запуск Flet-приложения
ft.app(target=Interface.start)