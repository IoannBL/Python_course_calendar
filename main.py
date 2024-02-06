import flet as ft
from Interface_pr import Interface

if __name__ == "__main__":
    def main(page: ft.Page):
        page.title = "Flet Trello clone"
        page.padding = 0
        page.bgcolor = ft.colors.BLUE_GREY_200
        app = Interface(page)
        page.add(app)
        page.update()
    
    
    ft.app(target=main, view=ft.WEB_BROWSER)
    
    