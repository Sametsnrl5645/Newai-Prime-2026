import flet as ft
from ui_display import NewaiInterface
from access_controller import AccessController 

async def main(page: ft.Page):
    page.title = "NEWAI PRIME 2026"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#000000"
    
    # Doğrudan Dashboard'u başlat (Giriş ekranı istersen buraya ekleriz)
    ui_engine = NewaiInterface(page)
    ui_engine.build()

if __name__ == "__main__":
    # ft.app yerine ft.run kullanarak DeprecationWarning hatasını siliyoruz
    ft.run(main)