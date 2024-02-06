import flet as ft

class Interface:
    @staticmethod
    def start(page: ft.Page):
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        # page.theme = ft.Theme(
        #     color_scheme_seed=ft.colors.WHITE)
        # Создаем кнопки для опций меню
        buttons = [
            ft.Container(
                content=ft.ElevatedButton("Войти в аккаунт", on_click=Interface.entrance,bgcolor=ft.colors.GREEN_50),
                width=300,
                height=50
                
            ),
            ft.Container(
                ft.ElevatedButton("Создать нового пользователя", on_click=Interface.create_new_user,bgcolor=ft.colors.GREEN_50),
                width=300,
                height=50
            ),
            ft.Container(
                ft.ElevatedButton("Завершить работу", on_click=Interface.finish),
                width=180,
                height=50,
                margin=ft.margin.only(top=70,left=40),
 
            ),
        ]
        button_column = ft.Column(buttons)
        st = ft.Stack(
            [
                ft.Container(
                    content=button_column,
                    bgcolor=ft.colors.BLUE_50,
                    padding=ft.padding.all(20),
                    width=300,
                    height=300,
                    border_radius=30,
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
    def create_new_user():
        # Ваш код для создания нового пользователя
        pass

    @staticmethod
    def finish():
        # Ваш код для завершения работы
        pass

# Запуск Flet-приложения
ft.app(target=Interface.start)

# import flet as ft
#
#
# def main(page: ft.Page):
#     # Yellow page theme with SYSTEM (default) mode
#     page.theme = ft.Theme(
#         color_scheme_seed=ft.colors.BLUE,
#     )
#
#     page.add(
#         # Page theme
#         ft.Container(
#             content=ft.ElevatedButton("Page theme button"),
#             bgcolor=ft.colors.SURFACE_VARIANT,
#             padding=20,
#             width=300,
#         ),
#
#         # Inherited theme with primary color overridden
#         ft.Container(
#             theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.PINK)),
#             content=ft.ElevatedButton("Inherited theme button"),
#             bgcolor=ft.colors.SURFACE_VARIANT,
#             padding=20,
#             width=300,
#         ),
#
#         # Unique always DARK theme
#         ft.Container(
#             theme=ft.Theme(color_scheme_seed=ft.colors.INDIGO),
#             theme_mode=ft.ThemeMode.DARK,
#             content=ft.ElevatedButton("Unique theme button"),
#             bgcolor=ft.colors.SURFACE_VARIANT,
#             padding=20,
#             width=300,
#         ),
#     )
#
#
# ft.app(main)