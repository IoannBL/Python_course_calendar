import math
import flet as ft
#
# def main(page: ft.Page):
#
#     page.add(
#         ft.Container(
#             alignment=ft.alignment.center,
#             gradient=ft.LinearGradient(
#                 begin=ft.alignment.top_left,
#                 end=ft.Alignment(0.8, 1),
#                 colors=[
#                     "0xff1f005c",
#                     "0xff5b0060",
#                     "0xff870160",
#                     "0xffac255e",
#                     "0xffca485c",
#                     "0xffe16b5c",
#                     "0xfff39060",
#                     "0xffffb56b",
#                 ],
#                 tile_mode=ft.GradientTileMode.MIRROR,
#                 rotation=math.pi / 3,
#             ),
#             expand=True,
            # width="100%",
            # height="100%",
#             border_radius=5,
#         )
#     )
#
#
#
#
def main(page: ft.Page):
    page.title = "Routes Example"
    
    
    
    def start(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/entrance",
                [
                    ft.AppBar(title=ft.Text("КАЛЕНДАРЬ", color=ft.colors.BLUE_800),
                              bgcolor=ft.colors.BLUE_50,
                              leading=ft.Icon(ft.icons.CALENDAR_MONTH, color=ft.colors.BLUE_800),
                              leading_width=100,
                              toolbar_height=60,
                              ),
                    ft.Container(
                        alignment=ft.alignment.center,
                        content=ft.Column([
                            ft.Container(
                                content=(ft.Text("Calendar", color=ft.colors.BLUE_800, scale=2, size=10)),
                                width=300,
                                height=30,
                                # margin=ft.margin.only(left=70),
                                alignment=ft.alignment.center
                            ),
                            ft.Container(
                                content=ft.ElevatedButton("Войти", on_click=lambda _: page.go("/store"),
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
                                                          on_click=show_bs, bgcolor=ft.colors.LIGHT_GREEN_ACCENT_200,
                                                          style=ft.ButtonStyle(
                                                              shape=ft.RoundedRectangleBorder(radius=10),
                                                          ), ),
                                width=300,
                                height=50,
                            ),
                            ft.Container(
                                content=ft.TextButton("Завершить работу", on_click=lambda _: page.go("/entrance")),
                                width=180,
                                height=50,
                                margin=ft.margin.only(top=20, left=40),
                                opacity=1
                            ),
                        ]
                        ),
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
                        
                        visible=True,
                        expand=False,
                        # margin = 100
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                vertical_alignment=ft.MainAxisAlignment.CENTER,
            )
        )
        
        if page.route == "/store":
            page.views.append(def menu
                
                # ft.View(
                #     "/store",
                #     [
                #         ft.AppBar(title=ft.Text("Store"), bgcolor=ft.colors.GREEN_50),
                #         ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/entrance")),
                #         ft.Container(content=ft.Column(), )
                #     ],
                # )
            )
        page.update()
        
    def menu():
        return ft.View(
            "/store",
            [
                ft.AppBar(title=ft.Text("Store"), bgcolor=ft.colors.GREEN_50),
                ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/entrance")),
                ft.Container(content=ft.Column(), )
            ],
        )

        
    
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
    
    def bs_dismissed(e):
        print("Dismissed!")
    
    def show_bs(e):
        bs.open = True
        bs.update()
    
    def close_bs(e):
        bs.open = False
        bs.update()
    
    bs = ft.BottomSheet(
        ft.Container(
            ft.Column(
                [
                    ft.IconButton(
                        icon=ft.icons.CLOSE,
                        icon_color="blue700",
                        icon_size=30,
                        tooltip="Закрыть",
                        on_click=close_bs),
                    ft.Container(
                        content=(
                            ft.Column(
                                [
                                    ft.Container(
                                        content=ft.TextField(label="Введите имя пользователя: ", autofocus=True),
                                        width=300,
                                        height=50
                                    ),
                                    ft.Container(
                                        content=ft.TextField(label="Придумайте пароль: ", autofocus=True),
                                        width=300,
                                        height=50
                                    )
                                ]
                            )
                        ),
                        margin=ft.margin.only(top=0),
                        bgcolor=ft.colors.BLUE_50,
                        padding=ft.padding.all(40),
                        width=1000,
                        height=800,
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
                tight=True,
            ),
            padding=0,
        ),
        open=False,
        on_dismiss=bs_dismissed,
    )
    
    
    page.on_route_change = start
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)

