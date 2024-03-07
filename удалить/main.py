import flet as ft
from Routes import views_handler
from Entrance import Interface




class Main(ft.UserControl):
    
    def __init__(self,page:ft.Page):
        super().__init__()
        self.page = page
        page.theme_mode = ft.ThemeMode.LIGHT
        page.window_width = 800
        page.window_height = 1000
        page.window_resizable = True
        page.window_maximizable = True
        page.appbar = Interface.navbar(page)
        
        def route_change(route):
            print(page.route)
            page.views.clear()
            page.views.append(
                views_handler(page)[page.route]
            )
        
        page.on_route_change = route_change
        page.go('/')

ft.app(target=Main)

    
    
    

        
        

    
    
   
    
    

    
    