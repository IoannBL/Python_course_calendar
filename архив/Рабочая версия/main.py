import flet as ft
from Routes import views_handler
from Start_page import Interface


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

# class Main(ft.UserControl):
#     def __init__(self,page:ft.Page):
#         super().__init__()
#         self.page = page
#         page.window_width = 800
#         page.window_height = 1200
#         page.theme_mode = ft.ThemeMode.LIGHT
#         page.window_resizable = False
#         # app = Interface(page)
#         # page.add(app)
#
#         self.helper()
#
#     def helper(self):
#         self.page.on_route_change = self.on_route_change
#         self.page.go("/")
#
#     def on_route_change(self,route):
#         route_page_1 = {
#             "/" : Interface,
#         }[self.page.route](self.page)
#         self.page.views.clear()
#         self.page.views.append(
#             ft.View(
#                 route,
#                     [route_page_1]
#             )
#         )
#
# if __name__ == "__main__":
#     ft.app(target=Main)
        
        

    
    
   
    
    

    
    