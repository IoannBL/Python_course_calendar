
import  flet as ft
#
#
# def main(page: Page):
#     # CREATE FAKE DATA
#     data = ["@Илона0", "@Иоанн0", "@Денис", "@Николай"]
#
#     resultdata = ListView()
#
#     resultcon = Container(
#         bgcolor="red200",
#         padding=10,
#         margin=10,
#         offset=transform.Offset(-2, 0),
#         animate_offset=animation.Animation(600, curve="easeIn"),
#         content=Column([resultdata])
#     )
#
#     def searchnow(e):
#         mysearch = e.control.value
#
#         # Clear previous results
#         resultdata.controls.clear()
#
#         # Search logic
#         if mysearch:
#             search_terms = [term.strip() for term in mysearch.split(",")]
#             for item in data:
#                 for term in search_terms:
#                     if term and term in item:
#                         resultdata.controls.append(
#                             Text(item, size=20, color="white")
#                         )
#             # Show/hide result container based on search results
#             resultcon.visible = bool(resultdata.controls)
#             if resultcon.visible:
#                 resultcon.offset = transform.Offset(0, 0)
#             else:
#                 resultcon.offset = transform.Offset(-2, 0)
#
#         else:
#             resultcon.visible = False
#
#         page.update()
#
#     def on_submit(e):
#         searchnow(e)
#
#     txtsearch = TextField(label="Search now", on_change=searchnow, on_submit=on_submit)
#
#     page.add(
#         Column([
#             Text("Search Anything", size=30, weight="bold"),
#             txtsearch,
#             resultcon
#         ])
#     )
#
#
# app(target=main)

def main (page:ft.Page):
    def __init__(self, app_layout, page):
        super().__init__()
        
        self.app_layout = app_layout
        self.page = page
        self.top_nav_items = [
            ft.NavigationRailDestination(
                label_content=ft.Text("Boards"),
                label="Boards",
                icon=ft.icons.BOOK_OUTLINED,
                selected_icon=ft.icons.BOOK_OUTLINED
            ),
            ft.NavigationRailDestination(
                label_content=ft.Text("Members"),
                label="Members",
                icon=ft.icons.PERSON,
                selected_icon=ft.icons.PERSON
            ),
        
        ]
        self.top_nav_rail = ft.NavigationRail(
            selected_index=None,
            label_type="all",
            on_change=self.top_nav_change,
            destinations=self.top_nav_items,
            bgcolor=ft.colors.BLUE_GREY,
            extended=True,
            expand=True
        )
    
    def build(self):
        self.view = ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Text("Workspace"),
                ]),
                # divider
                ft.Container(
                    bgcolor=ft.colors.BLACK26,
                    border_radius=ft.border_radius.all(30),
                    height=1,
                    alignment=ft.alignment.center_right,
                    width=220
                ),
                self.top_nav_rail,
                # divider
                ft.Container(
                    bgcolor=ft.colors.BLACK26,
                    border_radius=ft.border_radius.all(30),
                    height=1,
                    alignment=ft.alignment.center_right,
                    width=220
                ),
            ], tight=True),
            padding=ft.padding.all(15),
            margin=ft.margin.all(0),
            width=250,
            bgcolor=ft.colors.BLUE_GREY,
        )
        return self.view
    
    def top_nav_change(self, e):
        self.top_nav_rail.selected_index = e.control.selected_index
        self.update()


ft.app(target=main)